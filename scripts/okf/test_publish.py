"""
OKF publish 단위 테스트 (표준 라이브러리 unittest).

실행: python -m unittest scripts.okf.test_publish -v
AC1: derive_type 전체 prefix 케이스 통과 + conformance/정크 핵심 동작.
"""
import tempfile
import unittest
from pathlib import Path

from scripts.okf import publish as P


class TestDeriveType(unittest.TestCase):
    """§5 + §11 보정: 전체 prefix 케이스 + fallback."""

    def test_all_mapped_prefixes(self):
        cases = {
            "wiki/concepts/sdt.md": "Concept",
            "wiki/tools/claude-code.md": "Tool",
            "wiki/frameworks/lmx.md": "Framework",
            "wiki/skills/weekly-report.md": "Skill",
            "wiki/decisions/d-001.md": "Decision",
            "wiki/people/csp.md": "Person",
            "wiki/signals/2026-06-15.md": "Signal",      # §11 보정 2
            "wiki/protocols/ingest.md": "Protocol",       # §11 보정 2
            "wiki/projects/ex.md": "Project",
            "projects/oka/README.md": "Project",
            "references/agentic.md": "Reference",
            "research/ai-2026.md": "Research",
            "analysis/harness.md": "Analysis",
        }
        for rel, expected in cases.items():
            t, fallback = P.derive_type(rel)
            self.assertEqual(t, expected, rel)
            self.assertFalse(fallback, rel)

    def test_longest_prefix_wins(self):
        # wiki/projects 가 wiki 보다 우선(현재 wiki 단독 매핑은 없지만 규칙 검증).
        t, _ = P.derive_type("wiki/projects/foo.md")
        self.assertEqual(t, "Project")

    def test_fallback_for_unmapped(self):
        for rel in ["wiki/unknown/x.md", "outputs/draft.md", "foo.md"]:
            t, fallback = P.derive_type(rel)
            self.assertEqual(t, P.FALLBACK_TYPE)
            self.assertTrue(fallback, rel)

    def test_excluded_root_dirs_fall_back(self):
        # §11 보정 1: 루트 concepts/people/decisions 는 IN 제외 → fallback.
        for rel in ["concepts/extracted-x.md", "people/slide1.PNG.md",
                    "decisions/x.md", "permanent/x.md", "moc/x.md"]:
            _, fallback = P.derive_type(rel)
            self.assertTrue(fallback, rel)


class TestNormalizeType(unittest.TestCase):
    def test_lowercase_to_pascal(self):
        self.assertEqual(P.normalize_type("concept"), "Concept")
        self.assertEqual(P.normalize_type("framework"), "Framework")
        self.assertEqual(P.normalize_type("PROJECT"), "Project")

    def test_unknown_passthrough(self):
        self.assertEqual(P.normalize_type("CustomType"), "CustomType")


class TestParseFrontmatter(unittest.TestCase):
    def test_valid(self):
        fm, ok, body = P.parse_frontmatter("---\ntype: Concept\n---\n# Hi\n")
        self.assertTrue(ok)
        self.assertEqual(fm["type"], "Concept")
        self.assertIn("# Hi", body)

    def test_bom_tolerant(self):
        fm, ok, _ = P.parse_frontmatter("﻿---\ntype: Concept\n---\nx")
        self.assertTrue(ok)
        self.assertEqual(fm["type"], "Concept")

    def test_no_frontmatter(self):
        fm, status, _ = P.parse_frontmatter("# Extracted Knowledge\n\ntext")
        self.assertEqual(status, "none")
        self.assertEqual(fm, {})

    def test_malformed_yaml(self):
        # 실제 csp-brain 패턴: related_to 쉼표 나열은 유효 YAML 아님.
        fm, status, _ = P.parse_frontmatter(
            '---\ntype: Note\nrelated_to: "[[a]]", "[[b]]"\n---\nbody')
        self.assertEqual(status, "malformed")

    def test_status_values(self):
        self.assertEqual(P.parse_frontmatter("---\ntype: X\n---\n")[1], "ok")
        self.assertEqual(P.parse_frontmatter("# no fm")[1], "none")


class TestConformanceAndDiscover(unittest.TestCase):
    def _mk(self, root: Path, rel: str, content: str):
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def test_missing_frontmatter_is_error(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._mk(root, "wiki/concepts/no-fm.md", "# 추출 덤프\n본문")
            self._mk(root, "wiki/concepts/ok.md",
                     "---\ntype: Concept\n---\n# 정상\n[[link-a]]\n")
            concepts, idx = P.discover(root)
            findings = P.check_conformance(concepts)
            codes = {f.code for f in findings}
            self.assertIn("missing-frontmatter", codes)
            self.assertIn("legacy-dialect", codes)  # ok.md 의 위키링크
            # 전역 인덱스에 두 파일 stem 등록
            self.assertIn("no-fm", idx)
            self.assertIn("ok", idx)

    def test_malformed_frontmatter_is_error(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._mk(root, "wiki/concepts/bad.md",
                     '---\ntype: Note\nrelated_to: "[[a]]", "[[b]]"\n---\nbody')
            findings = P.check_conformance(P.discover(root)[0])
            codes = {f.code for f in findings}
            self.assertIn("malformed-frontmatter", codes)
            self.assertNotIn("missing-frontmatter", codes)

    def test_type_conflict(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            # 경로상 Tool 인데 frontmatter 는 Concept → type-conflict
            self._mk(root, "wiki/tools/x.md", "---\ntype: Concept\n---\nbody")
            findings = P.check_conformance(P.discover(root)[0])
            self.assertIn("type-conflict", {f.code for f in findings})

    def test_name_index_collision(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._mk(root, "wiki/concepts/dup.md", "---\ntype: Concept\n---\nx")
            self._mk(root, "projects/dup.md", "---\ntype: Project\n---\nx")
            _, idx = P.discover(root)
            self.assertEqual(len(idx["dup"]), 2)  # 충돌 → ambiguous(Phase 2)

    def test_root_junk_scan(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._mk(root, "무제.md", "x")
            self._mk(root, "untitled-daily-1777847579.md", "x")
            self._mk(root, "2605.md", "x")
            self._mk(root, "260506.md", "x")
            self._mk(root, "README.md", "keep")  # 정크 아님
            junk = set(P.scan_root_junk(root))
            self.assertEqual(
                junk,
                {"무제.md", "untitled-daily-1777847579.md", "2605.md", "260506.md"},
            )

    def test_clean_bundle_passes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._mk(root, "wiki/concepts/a.md", "---\ntype: Concept\n---\nbody")
            findings = P.check_conformance(P.discover(root)[0])
            errors = [f for f in findings if f.severity == "ERROR"]
            self.assertEqual(errors, [])


class TestRepairFrontmatter(unittest.TestCase):
    def test_multi_wikilink_to_list(self):
        raw = 'type: Note\nrelated_to: "[[a]]", "[[b]]"'
        fixed, changed = P.repair_frontmatter_text(raw)
        self.assertTrue(changed)
        import yaml
        data = yaml.safe_load(fixed)
        self.assertEqual(data["related_to"], ["[[a]]", "[[b]]"])

    def test_single_unquoted_wikilink(self):
        raw = "related_to: [[opq-framework]]"
        fixed, changed = P.repair_frontmatter_text(raw)
        self.assertTrue(changed)
        import yaml
        self.assertEqual(yaml.safe_load(fixed)["related_to"], "[[opq-framework]]")

    def test_no_change_for_valid(self):
        _, changed = P.repair_frontmatter_text("type: Concept\ntags: [a, b]")
        self.assertFalse(changed)


class TestSlugify(unittest.TestCase):
    def test_paren_and_space(self):
        self.assertEqual(P.slugify("Dream Cycle (주간 정리 루틴)"), "dream-cycle")
        self.assertEqual(P.slugify("Memory Save (대화 종료 기록)"), "memory-save")
        self.assertEqual(P.slugify("self-determination-theory"),
                         "self-determination-theory")


class TestWikilinkConversion(unittest.TestCase):
    def _idx(self, concepts):
        return P.build_link_index(concepts), \
            {c.rel for c in concepts} | {P.rename_index(c.rel) for c in concepts}

    def _c(self, rel, fm=None, body=""):
        return P.Concept(src=Path(rel), rel=rel, frontmatter=fm or {},
                         fm_status="ok", body=body)

    def test_name_form_resolves(self):
        cs = [self._c("wiki/concepts/foo.md")]
        idx, rels = self._idx(cs)
        out, lint = P.convert_wikilinks("see [[foo]] here", idx, rels)
        self.assertEqual(out, "see [foo](/wiki/concepts/foo.md) here")
        self.assertEqual(lint, [])

    def test_alias_form(self):
        cs = [self._c("wiki/concepts/foo.md")]
        idx, rels = self._idx(cs)
        out, _ = P.convert_wikilinks("[[foo|보이는 라벨]]", idx, rels)
        self.assertEqual(out, "[보이는 라벨](/wiki/concepts/foo.md)")

    def test_path_form_and_index(self):
        cs = [self._c("wiki/concepts/foo/_index.md")]
        idx, rels = self._idx(cs)
        out, _ = P.convert_wikilinks("[[wiki/concepts/foo/_index|개념]]", idx, rels)
        self.assertEqual(out, "[개념](/wiki/concepts/foo/index.md)")

    def test_anchor_preserved(self):
        cs = [self._c("wiki/concepts/foo.md")]
        idx, rels = self._idx(cs)
        out, _ = P.convert_wikilinks("[[foo#섹션]]", idx, rels)
        self.assertEqual(out, "[foo](/wiki/concepts/foo.md#섹션)")

    def test_alias_index_resolves_korean_title(self):
        cs = [self._c("wiki/concepts/memory-save.md",
                      fm={"aliases": ["Memory Save (대화 종료 기록)"]})]
        idx, rels = self._idx(cs)
        out, lint = P.convert_wikilinks("[[Memory Save (대화 종료 기록)]]", idx, rels)
        self.assertIn("/wiki/concepts/memory-save.md", out)
        self.assertEqual(lint, [])

    def test_ambiguous_kept(self):
        cs = [self._c("wiki/concepts/dup.md"), self._c("projects/dup.md")]
        idx, rels = self._idx(cs)
        out, lint = P.convert_wikilinks("[[dup]]", idx, rels)
        self.assertEqual(out, "[[dup]]")  # 미변환 보존
        self.assertEqual(lint[0][0], "ambiguous-link")

    def test_unresolved_kept(self):
        cs = [self._c("wiki/concepts/foo.md")]
        idx, rels = self._idx(cs)
        out, lint = P.convert_wikilinks("[[nonexistent]]", idx, rels)
        self.assertEqual(out, "[[nonexistent]]")
        self.assertEqual(lint[0][0], "unresolved-link")


class TestTimelineAndLog(unittest.TestCase):
    def test_extract_and_generate(self):
        body = (
            "## 3. 타임라인\n\n"
            "### 2026-05-16\n\n"
            "- **모델 통합**: OPQ32 이식.\n"
            "- 리포트 생성 완료.\n\n"
            "### 2026-05-31 (Planned)\n\n"
            "- 시뮬레이션 착수.\n"
        )
        entries = P.extract_timeline_entries(body)
        self.assertEqual(entries[0][0], "2026-05-16")
        self.assertEqual(entries[1][0], "2026-05-31 (Planned)")
        # 굵게 ** 보존 확인
        self.assertEqual(entries[0][1][0], "**모델 통합**: OPQ32 이식.")
        log = P.generate_log(entries)
        self.assertIn("## 2026-05-16", log)
        self.assertIn("* **Planned**: 시뮬레이션 착수.", log)
        self.assertTrue(log.startswith("# Directory Update Log"))


class TestRenameIndex(unittest.TestCase):
    def test_rename(self):
        self.assertEqual(P.rename_index("wiki/tools/_index.md"),
                         "wiki/tools/index.md")
        self.assertEqual(P.rename_index("wiki/tools/foo.md"),
                         "wiki/tools/foo.md")


class TestPublishBundleIntegration(unittest.TestCase):
    def _mk(self, root, rel, content):
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def test_end_to_end_passes_and_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._mk(root, "wiki/concepts/a.md",
                     '---\ntype: Concept\nrelated_to: "[[b]]", "[[c]]"\n---\n'
                     "본문 [[b]] 참조\n")
            self._mk(root, "wiki/concepts/b.md", "---\ntype: Concept\n---\nbody")
            self._mk(root, "wiki/concepts/_index.md", "# 색인")
            out1, out2 = root / "o1", root / "o2"
            f1, s1 = P.publish_bundle(root, out1, dry_run=False)
            f2, s2 = P.publish_bundle(root, out2, dry_run=False)
            errors = [x for x in f1 if x.severity == "ERROR"]
            self.assertEqual(errors, [])              # PASS
            # malformed 수리로 a.md 의 related_to 가 유효해졌다
            self.assertTrue((out1 / "wiki/concepts/index.md").exists())
            self.assertTrue((out1 / "index.md").exists())  # 루트 okf_version
            # 멱등: 두 발행본 동일
            txt1 = (out1 / "wiki/concepts/a.md").read_text(encoding="utf-8")
            txt2 = (out2 / "wiki/concepts/a.md").read_text(encoding="utf-8")
            self.assertEqual(txt1, txt2)
            # [[b]] → 변환됨
            self.assertIn("/wiki/concepts/b.md", txt1)


if __name__ == "__main__":
    unittest.main()
