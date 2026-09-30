#!/usr/bin/env python3
"""
단계 A 편입 처리기 회귀 테스트 (표준 라이브러리 unittest)

실행:  python3 -m unittest discover -s tests -v   (저장소 루트에서)

모든 테스트는 임시 폴더에 만든 가짜 Vault 에서 돈다. 운영 Vault 는 건드리지 않는다.
검사 대상은 함수 반환값이 아니라 '저장된 본문·출처·상태·처리 기록'이다.
"""

import importlib.util
import json
import os
import shutil
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
import ingest_state as st  # noqa: E402
import stage_a_ingest as sa  # noqa: E402

SRC_CONFLICT = """---
type: briefing
date: 2026-08-27
title: "HR Tech 브리핑 — 신뢰의 비대칭성"
tags:
  - trust-ladder
processed: false
processed: true
processed_date: 2026-08-31
processed_note: INGEST 프로토콜에 따라 MERGE 편입됨

---
# HR Tech 브리핑

## 신호 1
후보자의 AI 면접 신뢰도는 26% 에 그쳤다. 2026 년 조사.
"""

SRC_PLAIN = """---
type: briefing
date: 2026-07-01
title: "알고리즘 불안과 일의 의미"
tags: [algorithmic-anxiety, meaningful-work]
---
# 알고리즘 불안과 일의 의미

## 인사이트 A
bullshitness 1 SD 증가 → AI 위임 욕구 0.39 점 증가 (N=202, 2026).
"""

TARGET = """---
type: signal
title: "자율 채용의 역설"
status: growing
_organized: true
related_to:
  - "[[hr-conceptual-atoms]]"
---
# 자율 채용의 역설

## Compiled Truth
채용 자동화는 신뢰 사다리를 따라 진행된다.

---

## Timeline

### 2026-07-22
- 초기 생성 (출처: [[BRIEFING_OLD]])
"""

UNRELATED = """---
type: signal
title: "2026 반도체 수출"
---
# 2026 반도체 수출

2026 년 수출 26% 증가.
"""


def merge_decision(content="bullshitness 가 높은 과업일수록 AI 위임을 원한다: 1 SD 증가 시 위임 욕구 0.39 점 상승 (N=202). 무의미한 일부터 자동화 수요가 생긴다는 신호."):
    return {"decision": "merge", "reason": "같은 개념(알고리즘 위임과 일의 의미)에 새 통계 추가",
            "source_quote_lines": "L9-L10",
            "targets": [{"path": "wiki/signals/autonomous-hiring.md",
                         "heading": "### 2026-07-01 — 알고리즘 불안 브리핑 편입",
                         "content": content}]}


class VaultCase(unittest.TestCase):
    """임시 Vault + 상태 폴더 + 잠금 폴더를 매 테스트마다 새로 만든다."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="stage-a-test-"))
        self.vault = self.tmp / "vault"
        for d in ("inbox/articles/deep", "outputs/briefings", "wiki/signals", "wiki/concepts"):
            (self.vault / d).mkdir(parents=True)
        self.state = self.tmp / "state"
        self.locks = self.tmp / "locks"
        self.out = self.tmp / "out"
        self.out.mkdir()
        self.write("outputs/briefings/BRIEFING_A_2026-07-01.md", SRC_PLAIN)
        self.write("wiki/signals/autonomous-hiring.md", TARGET)
        self.write("wiki/signals/_index.md", "# Signal Index\n\n- [[autonomous-hiring]]\n")
        os.environ.pop("STAGE_A_FAULT", None)

    def tearDown(self):
        os.environ.pop("STAGE_A_FAULT", None)
        shutil.rmtree(self.tmp, ignore_errors=True)

    # 도우미
    def write(self, rel, text):
        p = self.vault / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p

    def read(self, rel):
        return (self.vault / rel).read_text(encoding="utf-8")

    def plan(self, decisions=None, only=None):
        scan = sa.do_scan(st.resolve_vault(self.vault))
        plan = sa.do_plan(st.resolve_vault(self.vault), scan,
                          {"reviewer": "test", "items": decisions or {}}, only)
        path = self.out / f"plan-{len(list(self.out.glob('plan-*')))}.json"
        sa.write_json(path, plan)
        return plan, path

    def apply(self, plan_path, max_items=None):
        return sa.do_apply(st.resolve_vault(self.vault), plan_path, self.state, self.locks, max_items)

    def verify(self):
        return sa.do_verify(st.resolve_vault(self.vault), self.state)

    def db(self):
        return sqlite3.connect(str(self.state / st.DB_NAME))


# ──────────────────────────────────────────────────────────────────────────
class TestStateParsing(VaultCase):
    def test_duplicate_processed_is_conflict_not_done(self):
        a = st.analyze_source_text(SRC_CONFLICT)
        self.assertEqual(a["marker_state"], "conflict")
        # PyYAML 기본 동작(마지막 값 채택)으로 완료 처리되지 않았는지
        self.assertNotEqual(a["marker_state"], "marked_true")

    def test_body_only_processed_true_is_not_marker(self):
        text = "---\ntype: note\n---\n# 본문\n\nprocessed: true\n"
        self.assertEqual(st.analyze_source_text(text)["marker_state"], "unmarked")
        text2 = "# 제목 없음\nprocessed: true\n"
        self.assertEqual(st.analyze_source_text(text2)["marker_state"], "no_frontmatter")

    def test_ambiguous_values_and_formats_held(self):
        self.assertEqual(st.analyze_source_text("---\nprocessed: yes\n---\n")["marker_state"],
                         "invalid_value")
        self.assertEqual(st.analyze_source_text('---\nprocessed: "true"\n---\n')["marker_state"],
                         "invalid_value")
        self.assertEqual(st.analyze_source_text("---\nprocessed_note: |\n  a\n  b\n---\n")["marker_state"],
                         "unsupported")
        self.assertEqual(st.analyze_source_text("---\ntitle: a\ntitle: b\n---\n")["marker_state"],
                         "unsupported")
        self.assertEqual(st.analyze_source_text("---\ntitle: [a\n---\n")["marker_state"], "yaml_error")
        self.assertEqual(st.analyze_source_text("---\ntitle: a\n")["marker_state"], "yaml_error")

    def test_marker_rewrite_preserves_metadata(self):
        text = ('---\ntype: Note  # 타입 주석\n_organized: true\nrelated_to:\n  - "[[tolaria]]"\n'
                'belongs_to: "[[csp]]"\nprocessed: false\n\nprocessed: true\n---\n# 제목\n본문\n')
        new = st.set_processed_marker(text, True, "stage-a test", "2026-09-30")
        a = st.analyze_source_text(new)
        self.assertEqual(a["marker_state"], "marked_true")
        for line in ('type: Note  # 타입 주석', '_organized: true', '  - "[[tolaria]]"',
                     'belongs_to: "[[csp]]"'):
            self.assertIn(line, new)
        self.assertEqual(new.count("processed:"), 1)
        self.assertTrue(new.endswith("# 제목\n본문\n"))

    def test_revision_ignores_processor_keys_only(self):
        a = st.analyze_source_text(SRC_CONFLICT)
        b = st.analyze_source_text(st.set_processed_marker(SRC_CONFLICT, True, "x", "2026-09-30"))
        self.assertEqual(a["revision_sha256"], b["revision_sha256"])
        self.assertNotEqual(a["file_sha256"], b["file_sha256"])
        c = st.analyze_source_text(SRC_CONFLICT.replace("26%", "27%"))
        self.assertNotEqual(a["revision_sha256"], c["revision_sha256"])
        d = st.analyze_source_text(SRC_CONFLICT.replace("trust-ladder", "trust"))
        self.assertNotEqual(a["revision_sha256"], d["revision_sha256"])


class TestScanAndPaths(VaultCase):
    def test_scan_includes_past_dates_and_nested_inbox(self):
        self.write("inbox/articles/deep/old-note.md", "---\ntype: note\n---\n# 오래된 메모\n")
        self.write("outputs/briefings/BRIEFING_X_2025-01-01.md", SRC_PLAIN)
        paths = {r["path"] for r in sa.do_scan(st.resolve_vault(self.vault))["sources"]}
        self.assertIn("inbox/articles/deep/old-note.md", paths)
        self.assertIn("outputs/briefings/BRIEFING_X_2025-01-01.md", paths)

    def test_scan_skips_symlinks_and_reports_missing_roots(self):
        outside = self.tmp / "outside.md"
        outside.write_text("---\ntype: note\n---\n# 밖\n", encoding="utf-8")
        os.symlink(outside, self.vault / "inbox" / "link.md")
        shutil.rmtree(self.vault / "outputs")
        res = sa.do_scan(st.resolve_vault(self.vault))
        self.assertNotIn("inbox/link.md", {r["path"] for r in res["sources"]})
        self.assertTrue(any(e["root"] == "outputs/briefings" for e in res["input_errors"]))

    def test_path_escape_and_symlink_rejected(self):
        v = st.resolve_vault(self.vault)
        for bad in ("../x.md", "/etc/passwd.md", "wiki/signals/../../x.md", "inbox/a.md",
                    "wiki/signals/a.txt", ""):
            with self.assertRaises(st.StageAError):
                st.safe_rel_path(v, bad, st.TARGET_ROOTS)
        (self.tmp / "ext").mkdir()
        os.symlink(self.tmp / "ext", self.vault / "wiki/signals/linkdir")
        with self.assertRaises(st.StageAError):
            st.safe_rel_path(v, "wiki/signals/linkdir/x.md", st.TARGET_ROOTS)

    def test_plan_output_inside_vault_refused(self):
        code = sa.main(["scan", "--vault", str(self.vault),
                        "--output", str(self.vault / "scan.json")])
        self.assertEqual(code, 2)
        self.assertFalse((self.vault / "scan.json").exists())

    def test_linked_vault_path_resolves_to_real(self):
        link = self.tmp / "dev-link"
        os.symlink(self.vault, link)
        self.assertEqual(st.resolve_vault(link), st.resolve_vault(self.vault))


class TestPlanSafety(VaultCase):
    def test_default_plan_holds_everything_and_writes_nothing(self):
        before = {p: p.read_bytes() for p in self.vault.rglob("*") if p.is_file()}
        plan, _ = self.plan()
        self.assertTrue(all(it["decision"] == "hold" and not it["applicable"] for it in plan["items"]))
        after = {p: p.read_bytes() for p in self.vault.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        self.assertFalse(self.state.exists())

    def test_common_number_does_not_recommend_unrelated(self):
        self.write("wiki/signals/semiconductor-2026.md", UNRELATED)
        self.write("outputs/briefings/BRIEFING_EMPTY.md", "---\ntype: briefing\n---\n2026 26%\n")
        plan, _ = self.plan()
        for it in plan["items"]:
            self.assertNotIn("wiki/signals/semiconductor-2026.md",
                             [c["target"] for c in it["candidates"]])
            self.assertEqual(it["decision"], "hold")

    def test_year_glued_to_word_is_not_a_token(self):
        self.assertEqual(sa.tokens("BRIEFING_HR-TECH_2026-09-15 tech_2026 v2 신뢰"), {"신뢰"})

    def test_empty_content_or_todo_not_applicable(self):
        plan, _ = self.plan({"outputs/briefings/BRIEFING_A_2026-07-01.md": merge_decision("TODO")})
        it = plan["items"][0]
        self.assertFalse(it["applicable"])
        self.assertEqual(it["decision"], "hold")
        plan2, _ = self.plan({"outputs/briefings/BRIEFING_A_2026-07-01.md": {
            "decision": "new", "reason": "r", "new_note": {"h1": "x", "content": "TODO: 작성"}}})
        self.assertFalse(plan2["items"][0]["applicable"])

    def test_already_reflected_needs_real_evidence(self):
        dec = {"decision": "already_reflected", "reason": "중복",
               "targets": [{"path": "wiki/signals/autonomous-hiring.md",
                            "evidence_quote": "알고리즘 불안과 일의 의미"}]}
        plan, _ = self.plan({"outputs/briefings/BRIEFING_A_2026-07-01.md": dec})
        self.assertFalse(plan["items"][0]["applicable"])

    def test_conflict_requires_state_repair(self):
        self.write("outputs/briefings/BRIEFING_C.md", SRC_CONFLICT)
        dec = merge_decision()
        plan, _ = self.plan({"outputs/briefings/BRIEFING_C.md": dec})
        it = [i for i in plan["items"] if i["source"].endswith("BRIEFING_C.md")][0]
        self.assertFalse(it["applicable"])
        self.assertIn("state_repair", " ".join(it["validation_errors"]))


class TestApply(VaultCase):
    SRC = "outputs/briefings/BRIEFING_A_2026-07-01.md"

    def test_merge_writes_content_source_and_marker(self):
        _, path = self.plan({self.SRC: merge_decision()})
        res = self.apply(path)
        self.assertEqual(res["summary"].get("verified"), 1)
        target = self.read("wiki/signals/autonomous-hiring.md")
        self.assertIn("위임 욕구 0.39 점 상승", target)
        self.assertIn("- 출처: [[BRIEFING_A_2026-07-01]]", target)
        # Timeline 섹션 안(기존 항목 뒤)에 들어갔는지
        self.assertGreater(target.index("stage-a:begin"), target.index("## Timeline"))
        self.assertIn('_organized: true', target)
        src = st.analyze_source_text(self.read(self.SRC))
        self.assertEqual(src["marker_state"], "marked_true")
        v = self.verify()
        self.assertEqual(v["effective_counts"]["verified"], 1)
        self.assertEqual(v["failures"], [])

    def test_rerun_same_version_and_after_marker_change_no_duplicates(self):
        _, path = self.plan({self.SRC: merge_decision()})
        self.apply(path)
        snap = self.read("wiki/signals/autonomous-hiring.md")
        res2 = self.apply(path)  # 같은 수정안 재실행 (원문 파일 해시는 표시 때문에 달라짐)
        self.assertEqual(res2["summary"], {"already_verified": 1})
        self.assertEqual(self.read("wiki/signals/autonomous-hiring.md"), snap)
        # 새 scan/plan 으로 다시 해도(원문 버전 동일) 내용 중복 없음
        _, path3 = self.plan({self.SRC: merge_decision()})
        self.apply(path3)
        self.assertEqual(self.read("wiki/signals/autonomous-hiring.md").count("stage-a:begin"), 1)

    def test_new_note_valid_and_no_overwrite(self):
        self.write("wiki/signals/algorithmic-anxiety.md", "---\ntype: signal\n---\n# 기존\n")
        dec = {"decision": "new", "reason": "기존 신호 없음",
               "new_note": {"dir": "wiki/signals", "slug": "algorithmic-anxiety",
                            "h1": "알고리즘 불안과 위임 욕구", "tags": ["ai"],
                            "related_to": ["[[autonomous-hiring]]"],
                            "content": "무의미한 과업일수록 AI 위임 욕구가 크다 (β=0.39, N=202). [[autonomous-hiring]] 의 신뢰 사다리와 연결된다."}}
        plan, path = self.plan({self.SRC: dec})
        new_path = plan["items"][0]["targets"][0]["path"]
        self.assertEqual(new_path, "wiki/signals/algorithmic-anxiety-2.md")
        res = self.apply(path)
        self.assertEqual(res["summary"].get("verified"), 1)
        self.assertEqual(self.read("wiki/signals/algorithmic-anxiety.md"),
                         "---\ntype: signal\n---\n# 기존\n")
        note = self.read(new_path)
        a = st.analyze_source_text(note)
        self.assertEqual(a["meta"]["type"], "signal")
        self.assertNotIn("title", a["meta"])
        self.assertEqual(a["h1"], "알고리즘 불안과 위임 욕구")
        self.assertIn("- 출처: [[BRIEFING_A_2026-07-01]]", note)
        self.assertNotIn("TODO", note)
        idx = self.read("wiki/signals/_index.md")
        self.assertEqual(idx.count("[[algorithmic-anxiety-2]]"), 1)
        self.apply(path)  # 재실행 — 인덱스 중복 없음
        self.assertEqual(self.read("wiki/signals/_index.md").count("[[algorithmic-anxiety-2]]"), 1)

    def test_new_plus_merge_mixed_targets(self):
        dec = {"decision": "new", "reason": "주제 둘: 신규 개념 + 기존 신호 보강",
               "new_note": {"dir": "wiki/concepts", "slug": "meaningless-work-delegation",
                            "h1": "무의미한 일의 위임", "related_to": ["[[autonomous-hiring]]"],
                            "content": "bullshitness 1 SD 증가 → AI 위임 욕구 0.39 점 증가 (N=202). 위임 수요는 일의 의미가 낮은 곳에서 먼저 생긴다."},
               "targets": merge_decision()["targets"]}
        plan, path = self.plan({self.SRC: dec})
        kinds = sorted(t["kind"] for t in plan["items"][0]["targets"])
        self.assertEqual(kinds, ["merge", "new"])
        res = self.apply(path)
        self.assertEqual(res["results"][0]["result"], "verified")
        self.assertIn("stage-a:begin", self.read("wiki/signals/autonomous-hiring.md"))
        self.assertTrue((self.vault / "wiki/concepts/meaningless-work-delegation.md").is_file())
        self.assertEqual(self.verify()["failures"], [])

    def test_korean_title_slug_unique(self):
        self.assertEqual(sa.slugify("알고리즘 불안: 일의 의미!"), "알고리즘-불안-일의-의미")
        self.assertEqual(sa.slugify("!!!"), "signal")

    def test_already_reflected_repairs_state_only(self):
        self.write("outputs/briefings/BRIEFING_C.md", SRC_CONFLICT)
        evidence = "- 후보자의 AI 면접 신뢰도는 26% 에 그쳤다는 조사가 신뢰 사다리 1단을 뒷받침한다."
        tgt = TARGET + "\n### 2026-08-31\n출처: BRIEFING_C\n" + evidence + "\n"
        self.write("wiki/signals/autonomous-hiring.md", tgt)
        dec = {"decision": "already_reflected", "reason": "실제 문단 확인", "state_repair": True,
               "targets": [{"path": "wiki/signals/autonomous-hiring.md", "evidence_quote": evidence}]}
        _, path = self.plan({"outputs/briefings/BRIEFING_C.md": dec},
                            only=["outputs/briefings/BRIEFING_C.md"])
        res = self.apply(path)
        self.assertEqual(res["summary"], {"verified": 1})
        self.assertEqual(self.read("wiki/signals/autonomous-hiring.md"), tgt)  # 대상 무변경
        src = self.read("outputs/briefings/BRIEFING_C.md")
        self.assertEqual(src.count("processed:"), 1)
        self.assertEqual(st.analyze_source_text(src)["marker_state"], "marked_true")
        self.assertEqual(res["state_only"], 1)
        self.assertEqual(res["new_content_applied"], 0)

    def test_reset_pending_for_unreflected_conflict(self):
        self.write("outputs/briefings/BRIEFING_C.md", SRC_CONFLICT)
        dec = {"decision": "reset_pending", "reason": "대상에 제목·출처만 있음", "state_repair": True}
        _, path = self.plan({"outputs/briefings/BRIEFING_C.md": dec},
                            only=["outputs/briefings/BRIEFING_C.md"])
        self.apply(path)
        a = st.analyze_source_text(self.read("outputs/briefings/BRIEFING_C.md"))
        self.assertEqual(a["marker_state"], "marked_false")
        self.assertEqual(self.verify()["effective_counts"]["pending"], 2)
        # 새 scan/plan 으로 같은 결정을 재실행해도 보류로 바뀌지 않고 대기 유지, 파일 무변경
        snap = self.read("outputs/briefings/BRIEFING_C.md")
        plan2, path2 = self.plan({"outputs/briefings/BRIEFING_C.md": dec},
                                 only=["outputs/briefings/BRIEFING_C.md"])
        self.assertTrue(plan2["items"][0]["applicable"])
        self.apply(path2)
        self.assertEqual(self.read("outputs/briefings/BRIEFING_C.md"), snap)
        self.assertEqual(self.verify()["effective_counts"]["pending"], 2)

    def test_ambiguous_is_held_no_marker(self):
        before = self.read(self.SRC)
        _, path = self.plan({self.SRC: {"decision": "hold", "reason": "대상 불명확"}})
        res = self.apply(path)
        self.assertEqual(res["summary"], {"held": 1})
        self.assertEqual(self.read(self.SRC), before)

    def test_source_change_after_plan_needs_review(self):
        _, path = self.plan({self.SRC: merge_decision()})
        self.write(self.SRC, SRC_PLAIN.replace("0.39", "0.41"))
        res = self.apply(path)
        self.assertEqual(res["results"][0]["result"], "needs_review")
        self.assertNotIn("stage-a:begin", self.read("wiki/signals/autonomous-hiring.md"))
        self.assertEqual(st.analyze_source_text(self.read(self.SRC))["marker_state"], "unmarked")

    def test_target_change_after_plan_stops(self):
        _, path = self.plan({self.SRC: merge_decision()})
        self.write("wiki/signals/autonomous-hiring.md", TARGET + "\n사용자 편집\n")
        res = self.apply(path)
        self.assertEqual(res["results"][0]["result"], "failed")
        self.assertIn("target_changed", res["results"][0]["reason"])
        self.assertEqual(st.analyze_source_text(self.read(self.SRC))["marker_state"], "unmarked")

    def test_bad_target_path_in_plan_rejected(self):
        _, path = self.plan({self.SRC: merge_decision()})
        plan = json.loads(path.read_text(encoding="utf-8"))
        plan["items"][0]["targets"][0]["path"] = "../escape.md"
        path.write_text(json.dumps(plan, ensure_ascii=False), encoding="utf-8")
        res = self.apply(path)
        self.assertEqual(res["results"][0]["result"], "failed")
        self.assertFalse((self.tmp / "escape.md").exists())
        self.assertEqual(st.analyze_source_text(self.read(self.SRC))["marker_state"], "unmarked")

    def test_plan_for_other_vault_refused(self):
        _, path = self.plan({self.SRC: merge_decision()})
        other = self.tmp / "other"
        shutil.copytree(self.vault, other)
        with self.assertRaises(st.StageAError):
            sa.do_apply(st.resolve_vault(other), path, self.state, self.locks, None)


class TestFailuresAndRecovery(VaultCase):
    SRC = "outputs/briefings/BRIEFING_A_2026-07-01.md"
    TGT = "wiki/signals/autonomous-hiring.md"

    def crash(self, point, path):
        os.environ["STAGE_A_FAULT"] = point
        with self.assertRaises(SystemExit):
            self.apply(path)
        os.environ.pop("STAGE_A_FAULT", None)

    def test_crash_after_write_recovers_without_duplicate(self):
        _, path = self.plan({self.SRC: merge_decision()})
        self.crash("after_target_write", path)
        self.assertEqual(self.read(self.TGT).count("stage-a:begin"), 1)
        self.assertEqual(st.analyze_source_text(self.read(self.SRC))["marker_state"], "unmarked")
        res = self.apply(path)
        self.assertEqual(res["results"][0]["result"], "verified")
        self.assertTrue(res["results"][0]["recovered"])
        self.assertEqual(self.read(self.TGT).count("stage-a:begin"), 1)

    def test_record_failure_no_marker(self):
        _, path = self.plan({self.SRC: merge_decision()})
        self.crash("before_verified_record", path)
        self.assertEqual(st.analyze_source_text(self.read(self.SRC))["marker_state"], "unmarked")
        self.assertEqual(self.verify()["effective_counts"]["verified"], 0)
        self.apply(path)
        self.assertEqual(self.read(self.TGT).count("stage-a:begin"), 1)
        self.assertEqual(self.verify()["effective_counts"]["verified"], 1)

    def test_marker_failure_repaired_without_readding(self):
        _, path = self.plan({self.SRC: merge_decision()})
        self.crash("marker_write", path)
        self.assertEqual(st.analyze_source_text(self.read(self.SRC))["marker_state"], "unmarked")
        v = self.verify()
        self.assertEqual(v["effective_counts"]["verified"], 0)  # 표시 없으면 완료 아님
        snap = self.read(self.TGT)
        res = self.apply(path)
        self.assertEqual(res["results"][0]["result"], "verified")
        self.assertEqual(self.read(self.TGT), snap)
        self.assertEqual(st.analyze_source_text(self.read(self.SRC))["marker_state"], "marked_true")

    def test_marker_oserror_reported_not_counted(self):
        _, path = self.plan({self.SRC: merge_decision()})
        os.environ["STAGE_A_FAULT"] = "marker_write:oserror"
        res = self.apply(path)
        os.environ.pop("STAGE_A_FAULT", None)
        self.assertEqual(res["results"][0]["result"], "verified_marker_failed")
        self.assertEqual(self.verify()["effective_counts"]["verified"], 0)
        snap = self.read(self.TGT)
        self.assertEqual(self.apply(path)["results"][0]["result"], "verified")
        self.assertEqual(self.read(self.TGT), snap)

    def test_block_deleted_or_modified_detected_but_unrelated_edit_ok(self):
        _, path = self.plan({self.SRC: merge_decision()})
        self.apply(path)
        txt = self.read(self.TGT)
        self.write(self.TGT, txt.replace("채용 자동화는", "채용 자동화는 (편집)"))
        self.assertEqual(self.verify()["failures"], [])
        self.write(self.TGT, txt.replace("0.39 점 상승", "0.5 점 상승"))
        v = self.verify()
        self.assertTrue(any(f.get("reason") == "block_modified" for f in v["failures"]))
        self.write(self.TGT, TARGET)
        v = self.verify()
        self.assertTrue(any(f.get("reason") == "block_missing" for f in v["failures"]))
        self.assertEqual(v["effective_counts"]["verified"], 0)

    def test_marker_only_block_is_failure(self):
        op = "0123456789abcdef"
        inner = "- 출처: [[S]] (`outputs/briefings/S.md`)"
        text = (f"<!-- stage-a:begin id={op} source=outputs/briefings/S.md rev={'a'*12} "
                f"sha={st.sha256_text(inner)} -->\n{inner}\n<!-- stage-a:end id={op} -->")
        ok, why, _ = st.verify_block(text, op, "outputs/briefings/S.md")
        self.assertFalse(ok)
        self.assertEqual(why, "block_empty")

    def test_concurrent_run_blocked_by_lock(self):
        _, path = self.plan({self.SRC: merge_decision()})
        with st.vault_lock(st.resolve_vault(self.vault), self.locks):
            code = sa.main(["apply", "--vault", str(self.vault), "--plan", str(path),
                            "--state-dir", str(self.state), "--report", str(self.out / "r.json"),
                            "--lock-dir", str(self.locks)])
        self.assertEqual(code, 3)
        self.assertNotIn("stage-a:begin", self.read(self.TGT))

    def test_restore_and_refuse_after_user_edit(self):
        _, path = self.plan({self.SRC: merge_decision()})
        before_t, before_s = self.read(self.TGT), self.read(self.SRC)
        res = self.apply(path)
        rr = sa.do_restore(st.resolve_vault(self.vault), self.state, self.locks, res["run_id"])
        self.assertEqual(rr["conflicts"], 0)
        self.assertEqual(self.read(self.TGT), before_t)
        self.assertEqual(self.read(self.SRC), before_s)
        # 다시 적용한 뒤 사용자가 편집하면 복구가 덮어쓰지 않아야 함
        _, path2 = self.plan({self.SRC: merge_decision()})
        res2 = self.apply(path2)
        edited = self.read(self.TGT) + "\n사용자 추가 문단\n"
        self.write(self.TGT, edited)
        rr2 = sa.do_restore(st.resolve_vault(self.vault), self.state, self.locks, res2["run_id"])
        self.assertGreaterEqual(rr2["conflicts"], 1)
        self.assertEqual(self.read(self.TGT), edited)

    def test_max_items_limits_apply_not_discovery(self):
        self.write("outputs/briefings/BRIEFING_B.md", SRC_PLAIN.replace("0.39", "0.40"))
        d = {self.SRC: merge_decision(),
             "outputs/briefings/BRIEFING_B.md": merge_decision()}
        plan, path = self.plan(d)
        self.assertEqual(len(plan["items"]), 2)
        res = self.apply(path, max_items=1)
        self.assertEqual(res["summary"].get("deferred"), 1)


class TestDashboard(VaultCase):
    def load_dashboard(self):
        spec = importlib.util.spec_from_file_location(
            "update_dashboard_under_test", REPO / "_ops/scripts/update_dashboard.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def test_marker_vs_verified_and_missing_db(self):
        dash = self.load_dashboard()
        self.write("inbox/legacy.md", "---\nprocessed: true\n---\n# 기존 표시\n")
        self.write("inbox/body-only.md", "---\ntype: note\n---\nprocessed: true\n")
        self.write("outputs/briefings/BRIEFING_C.md", SRC_CONFLICT)
        res = dash.ingest_status_summary(self.vault, self.state)
        self.assertFalse(res["available"])
        self.assertIsNone(res["effective"])  # 기록 없으면 검증 완료를 추정하지 않음
        self.assertEqual(res["marker"].get("marked_true"), 1)
        self.assertEqual(res["marker"].get("conflict"), 1)
        self.assertEqual({p.name for p in res["inbox_not_marked"]}, {"body-only.md"})
        _, path = self.plan({"outputs/briefings/BRIEFING_A_2026-07-01.md": merge_decision()})
        self.apply(path)
        res = dash.ingest_status_summary(self.vault, self.state)
        self.assertTrue(res["available"])
        self.assertEqual(res["effective"].get("verified"), 1)
        self.assertEqual(res["effective"].get("legacy_unverified"), 1)
        self.assertEqual(res["effective"].get("conflict"), 1)


if __name__ == "__main__":
    unittest.main()
