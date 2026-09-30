#!/usr/bin/env python3
"""
단계 A 편입 처리기 — 명시적 실행 진입점

  scan    : 원문 탐색 + 상태 판정 (읽기 전용, Vault 에 아무것도 만들지 않음)
  plan    : 수정안 생성 (읽기 전용). 기본 판정은 '보류'.
            검토자(AI/사람)가 작성한 결정 파일(--decisions)이 있을 때만 적용 가능 항목이 생긴다.
  apply   : 수정안에 명시된 파일만 변경. 반영 → 다시 읽기 검증 → 기록 → 완료 표시 순서.
  verify  : 처리 기록과 실제 본문을 대조 (읽기 전용)
  restore : apply 가 남긴 복구본으로 되돌리기 (이후 편집이 있으면 덮어쓰지 않음)

비유하자면, scan/plan 은 '입고 예정 목록', apply 는 '서가에 꽂기',
verify 는 '서가에 실제로 책이 있는지 대조'다. 입고 도장(processed: true)은
대조가 끝난 뒤에만 찍는다.

종료 코드: 0 정상 / 1 예기치 못한 오류 / 2 입력·경로 오류 / 3 잠금 충돌·상태 DB 없음
          / 4 적용 또는 검증 실패 항목 존재
"""

from __future__ import annotations

import argparse
import difflib
import json
import math
import re
import shutil
import sys
import uuid
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_state as st  # noqa: E402

PLAN_VERSION = 1
DECISIONS = ("new", "merge", "already_reflected", "hold", "reset_pending")
MIN_EVIDENCE_CHARS = 30

STOPWORDS = {
    "briefing", "브리핑", "hr", "tech", "io", "psych", "money", "flow", "the", "and",
    "of", "in", "for", "to", "a", "an", "summary", "signal", "신호", "그리고", "시대",
    "i/o", "심리학", "시장", "md", "on", "with", "is", "ai",
}


# ──────────────────────────────────────────────────────────────────────────
# 공통 도우미
# ──────────────────────────────────────────────────────────────────────────

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def load_json(path: Path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise st.StageAError(f"JSON 읽기 실패: {path}: {exc}")


def tokens(text: str) -> set[str]:
    """후보 추천용 토큰. 숫자·연도·한 글자·불용어는 제외한다 (2026 같은 공통 숫자 병합 방지)."""
    out = set()
    # 밑줄도 구분자로 본다: 'tech_2026' 처럼 연도가 단어에 붙어 공통 토큰이 되는 것을 막기 위해
    for t in re.split(r"[^0-9a-z가-힣]+", (text or "").lower()):
        if len(t) < 2 or any(ch.isdigit() for ch in t) or t in STOPWORDS:
            continue
        out.add(t)
    return out


def doc_signature(analysis: dict, path: Path) -> set[str]:
    meta = analysis.get("meta") or {}
    parts = [str(meta.get("title") or ""), analysis.get("h1") or "", path.stem.replace("-", " ")]
    tags = meta.get("tags")
    if isinstance(tags, list):
        parts += [str(t) for t in tags]
    elif tags:
        parts.append(str(tags))
    return tokens(" ".join(parts))


def outline(text: str, limit=40):
    """원문 제목 구조 (행 번호 포함) — 검토자가 전체 원문을 읽을 때 길잡이."""
    out = []
    for i, line in enumerate(st.normalize_text(text).split("\n"), 1):
        if re.match(r"^#{1,4} ", line):
            out.append(f"L{i}: {line.strip()[:120]}")
        if len(out) >= limit:
            break
    return out


# ──────────────────────────────────────────────────────────────────────────
# scan
# ──────────────────────────────────────────────────────────────────────────

def do_scan(vault: Path, state_dir: Path | None = None) -> dict:
    files, input_errors = st.iter_markdown(vault, st.SOURCE_ROOTS)
    conn = st.open_db_readonly(state_dir) if state_dir else None
    rows = []
    for p in files:
        rel = str(p.relative_to(vault))
        row = {"path": rel}
        try:
            text = read_text(p)
            a = st.analyze_source_text(text)
            meta = a.get("meta") or {}
            row.update(
                file_sha256=a["file_sha256"], revision_sha256=a["revision_sha256"],
                marker_state=a["marker_state"], marker_detail=a["marker_detail"],
                processed_raw=a["processed_raw"],
                title=str(meta.get("title") or a.get("h1") or ""),
                date=str(meta.get("date") or ""), size=len(text),
            )
            if state_dir is not None:
                if conn is None:
                    row["effective_status"] = None  # 기록 없음 → 추정하지 않음
                else:
                    row["effective_status"], row["status_reason"] = st.effective_status(
                        vault, rel, a, conn)
        except (OSError, UnicodeError) as exc:
            row.update(marker_state="read_error", marker_detail=str(exc))
            input_errors.append({"root": rel, "error": f"읽기 실패: {exc}"})
        rows.append(row)
    if conn is not None:
        conn.close()
    counts = {}
    for r in rows:
        counts[r["marker_state"]] = counts.get(r["marker_state"], 0) + 1
    eff = None
    if state_dir is not None:
        eff = ({"available": False, "reason": "처리 기록(SQLite) 없음 — 검증 완료 집계 불가"}
               if conn is None else
               {"available": True, **{s: sum(r.get("effective_status") == s for r in rows)
                                      for s in st.EFFECTIVE_STATES}})
    return {
        "kind": "stage-a-scan", "scanned_at": st.now_iso(), "vault": str(vault),
        "roots": list(st.SOURCE_ROOTS), "input_errors": input_errors,
        "total": len(rows), "marker_counts": counts, "effective_counts": eff,
        "sources": rows,
    }


# ──────────────────────────────────────────────────────────────────────────
# plan
# ──────────────────────────────────────────────────────────────────────────

def load_targets(vault: Path):
    files, _ = st.iter_markdown(vault, st.TARGET_ROOTS)
    targets = []
    for p in files:
        try:
            text = read_text(p)
        except (OSError, UnicodeError):
            continue
        a = st.analyze_source_text(text)
        targets.append({"path": str(p.relative_to(vault)), "text": text,
                        "sig": doc_signature(a, p), "sha": st.sha256_text(st.normalize_text(text))})
    return targets


def existing_references(source_rel: str, targets):
    """원문 파일명을 언급하는 대상과, 그 절이 '제목·출처만 있는 빈 껍데기'인지 판정."""
    stem = Path(source_rel).stem
    refs = []
    for t in targets:
        lines = st.normalize_text(t["text"]).split("\n")
        for i, line in enumerate(lines):
            if stem not in line:
                continue
            # 해당 행이 속한 절(가장 가까운 위 제목 ~ 다음 제목)의 실질 행 수를 센다
            start = next((j for j in range(i, -1, -1) if re.match(r"^#{2,4} ", lines[j])), 0)
            end = next((j for j in range(i + 1, len(lines)) if re.match(r"^#{2,4} ", lines[j])),
                       len(lines))
            section = [ln for ln in lines[start + 1:end]
                       if ln.strip() and ln.strip() != "---"]
            substantive = [ln for ln in section
                           if stem not in ln and not ln.strip().startswith("- 편입일")
                           and not re.fullmatch(r'"[^"]*"', ln.strip())]
            refs.append({"target": t["path"], "line": i + 1,
                         "section_heading": lines[start].strip()[:120],
                         "section_lines": len(section),
                         "stub_like": len(substantive) < 2})
            break
    return refs


def recommend(sig: set[str], targets, top=3):
    """후보 추천 전용 (자동 병합 근거로 쓰지 않음). 공통 비숫자 토큰 2개 이상만."""
    scored = []
    for t in targets:
        common = sig & t["sig"]
        if len(common) < 2:
            continue
        score = len(common) / math.sqrt(max(len(sig), 1) * max(len(t["sig"]), 1))
        scored.append({"target": t["path"], "score": round(score, 3),
                       "common_tokens": sorted(common)[:8]})
    scored.sort(key=lambda x: -x["score"])
    return scored[:top]


def slugify(text: str) -> str:
    """kebab-case 파일명. 한글은 보존(한국어 제목도 충돌 없이 고유 이름 생성)."""
    s = re.sub(r"[^0-9a-z가-힣]+", "-", (text or "").lower()).strip("-")
    s = re.sub(r"-{2,}", "-", s)
    return s[:60].strip("-") or "signal"


def free_new_path(vault: Path, directory: str, slug: str, taken: set[str]) -> str:
    base = f"{directory.rstrip('/')}/{slugify(slug)}"
    cand, n = f"{base}.md", 2
    while (vault / cand).exists() or cand in taken:
        cand, n = f"{base}-{n}.md", n + 1
    return cand


def render_new_note(item: dict, op_id: str, date_str: str) -> str:
    nn = item["new_note"]
    rel = item["source"]
    fm = ["---", f"type: {nn.get('type', 'signal')}", f"created: {date_str}",
          f"updated: {date_str}", f"status: {nn.get('status', 'seed')}"]
    tags = nn.get("tags") or []
    fm.append("tags: [" + ", ".join(json.dumps(t, ensure_ascii=False) for t in tags) + "]")
    rel_links = nn.get("related_to") or []
    if rel_links:
        fm.append("related_to:")
        fm += [f'  - "{link}"' for link in rel_links]
    fm.append(f'source: "{rel}"')
    fm.append("---")
    block = st.render_block(op_id, rel, item["source_revision_sha256"], "", nn["content"])
    body = [f"# {nn['h1'].strip()}", "", "## Compiled Truth", "", block, "", "---", "",
            "## Timeline", "", f"### {date_str}", "",
            f"- stage-a 편입으로 신규 생성 (원문: [[{Path(rel).stem}]])", ""]
    return "\n".join(fm) + "\n" + "\n".join(body)


def validate_decision(vault: Path, item: dict, dec: dict, src_text: str,
                      targets_by_path: dict, taken: set[str], date_str: str):
    """
    검토자 결정을 현재 파일과 대조해 적용 가능한 수정안으로 만든다.
    하나라도 부족하면 hold 로 되돌리고 이유를 남긴다 (빈 내용·빈 출처는 적용 금지).
    """
    errors = []
    decision = dec.get("decision", "hold")
    if decision not in DECISIONS:
        errors.append(f"알 수 없는 판정: {decision}")
        decision = "hold"
    item["decision"] = decision
    item["reason"] = (dec.get("reason") or "").strip()
    item["source_quote_lines"] = dec.get("source_quote_lines", "")
    item["reviewer"] = dec.get("reviewer", "")
    item["state_repair"] = bool(dec.get("state_repair"))
    if not item["reason"]:
        errors.append("판정 이유(reason) 없음")
    ms = item["marker_state"]
    if ms in ("yaml_error", "unsupported", "invalid_value", "read_error"):
        errors.append(f"원문 상태 해석 불가({ms}) — 보류")
    if ms == "conflict" and decision != "hold" and not item["state_repair"]:
        errors.append("충돌 문서는 state_repair: true 인 증거 기반 복구안만 적용 가능")
    # marked_false 는 이전 실행에서 이미 대기로 정리된 경우 — 재실행 시 변경 없이 대기 유지
    if decision == "reset_pending" and ms not in ("conflict", "marked_false"):
        errors.append("reset_pending 은 상태 충돌 문서(또는 이미 대기로 정리된 문서)에만 사용")

    item["targets"] = []
    item["coverage"] = dec.get("coverage") or []  # 인사이트별 반영 위치·제외 이유 (검토 기록)

    def plan_merges(tlist):
        """병합 대상 목록을 검증해 반영 블록과 차이를 만든다 (merge·new 공용)."""
        for t in tlist:
            try:
                st.safe_rel_path(vault, t.get("path", ""), st.TARGET_ROOTS)
            except st.StageAError as exc:
                errors.append(str(exc))
                continue
            cur = targets_by_path.get(t["path"])
            if cur is None:
                errors.append(f"대상 파일 없음: {t['path']}")
                continue
            content = (t.get("content") or "").strip()
            if len(re.sub(r"\s+", "", content)) < 40 or "TODO" in content:
                errors.append(f"반영 내용이 비었거나 TODO 뿐임: {t['path']}")
                continue
            op_id = st.make_op_id(item["source"], item["source_revision_sha256"], t["path"], "merge")
            block = st.render_block(op_id, item["source"], item["source_revision_sha256"],
                                    t.get("heading", ""), content)
            after = st.insert_into_timeline(cur["text"], block)
            item["targets"].append({
                "kind": "merge", "path": t["path"], "op_id": op_id,
                "target_sha256": cur["sha"], "heading": t.get("heading", ""),
                "content": content,
                "diff": "".join(difflib.unified_diff(
                    st.normalize_text(cur["text"]).splitlines(True), after.splitlines(True),
                    fromfile=f"a/{t['path']}", tofile=f"b/{t['path']}")),
            })

    if decision == "merge":
        if not dec.get("targets"):
            errors.append("merge 대상 없음")
        plan_merges(dec.get("targets") or [])
    elif decision == "new":
        nn = dict(dec.get("new_note") or {})
        directory = nn.get("dir", "wiki/signals")
        if directory.rstrip("/") not in st.TARGET_ROOTS:
            errors.append(f"신규 노트 폴더 허용 범위 밖: {directory}")
        content = (nn.get("content") or "").strip()
        if not nn.get("h1") or len(re.sub(r"\s+", "", content)) < 40 or "TODO" in content:
            errors.append("신규 노트의 H1 또는 실제 내용이 없음 (TODO 노트 금지)")
        links = nn.get("related_to") or []
        known_stems = {Path(p).stem for p in targets_by_path}
        missing = []
        for ln in links:
            stem = re.sub(r"^\[\[|\]\]$", "", ln).split("|")[0]
            if stem not in known_stems and not any((vault / "wiki").rglob(f"{stem}.md")):
                missing.append(ln)
        if missing:
            item["warnings"] = [f"링크 대상 미존재: {missing}"]
        if not errors:
            path = free_new_path(vault, directory, nn.get("slug") or nn["h1"], taken)
            taken.add(path)
            op_id = st.make_op_id(item["source"], item["source_revision_sha256"], path, "new")
            nn.update(dir=directory, content=content)
            item["new_note"] = nn
            rendered = render_new_note(item, op_id, date_str)
            item["targets"].append({
                "kind": "new", "path": path, "op_id": op_id, "target_sha256": None,
                "diff": "".join(difflib.unified_diff([], rendered.splitlines(True),
                                                     fromfile="/dev/null", tofile=f"b/{path}")),
            })
            idx = f"{directory.rstrip('/')}/_index.md"
            item["index_path"] = idx if (vault / idx).is_file() else None
        # 서로 다른 인사이트는 기존 문서 병합으로 나눠 반영할 수 있다 (신규 + 병합 혼합)
        plan_merges(dec.get("targets") or [])
    elif decision == "already_reflected":
        tlist = dec.get("targets") or []
        if not tlist:
            errors.append("반영 증거 대상 없음 — '중복'만으로 완료 표시 불가")
        stem = Path(item["source"]).stem
        title = (item.get("title") or "").strip()
        for t in tlist:
            try:
                st.safe_rel_path(vault, t.get("path", ""), st.TARGET_ROOTS)
            except st.StageAError as exc:
                errors.append(str(exc))
                continue
            cur = targets_by_path.get(t["path"])
            quote = st.normalize_text(t.get("evidence_quote") or "").strip()
            if cur is None:
                errors.append(f"대상 파일 없음: {t['path']}")
            elif len(quote) < MIN_EVIDENCE_CHARS or (title and quote.strip('"') in title):
                errors.append(f"증거 인용이 너무 짧거나 제목뿐임: {t['path']}")
            elif quote not in st.normalize_text(cur["text"]):
                errors.append(f"증거 인용이 대상 본문에 없음: {t['path']}")
            elif stem not in cur["text"]:
                errors.append(f"대상에 원문 출처 표기 없음: {t['path']}")
            else:
                item["targets"].append({
                    "kind": "evidence", "path": t["path"],
                    "op_id": st.make_op_id(item["source"], item["source_revision_sha256"],
                                           t["path"], "evidence"),
                    "target_sha256": cur["sha"], "evidence_quote": quote})
    if decision in ("new", "merge", "already_reflected", "reset_pending"):
        after_marker = st.set_processed_marker(
            src_text, decision != "reset_pending",
            "stage-a (plan preview)", date_str)
        item["marker_diff"] = "".join(difflib.unified_diff(
            st.normalize_text(src_text).splitlines(True)[:40],
            after_marker.splitlines(True)[:40],
            fromfile=f"a/{item['source']}", tofile=f"b/{item['source']}"))
    if errors:
        item["validation_errors"] = errors
        item["applicable"] = False
        if decision != "hold":
            item["proposed_decision"] = decision
        item["decision"] = "hold"
    else:
        item["applicable"] = decision != "hold"


def do_plan(vault: Path, manifest: dict, decisions: dict | None, only: list[str] | None):
    if Path(manifest.get("vault", "")).resolve() != vault:
        raise st.StageAError(f"manifest 의 Vault({manifest.get('vault')}) 와 실행 Vault({vault}) 불일치")
    targets = load_targets(vault)
    targets_by_path = {t["path"]: t for t in targets}
    date_str = datetime.now().strftime("%Y-%m-%d")
    dec_items = (decisions or {}).get("items", {})
    taken: set[str] = set()
    items = []
    selected = only or [r["path"] for r in manifest["sources"]]
    known = {r["path"]: r for r in manifest["sources"]}
    for rel in selected:
        if rel not in known:
            raise st.StageAError(f"manifest 에 없는 원문: {rel}")
        src = st.safe_rel_path(vault, rel, st.SOURCE_ROOTS)
        text = read_text(src)  # 미리보기가 아니라 원문 전체를 읽는다
        a = st.analyze_source_text(text)
        item = {
            "source": rel,
            "source_file_sha256": a["file_sha256"],
            "source_revision_sha256": a["revision_sha256"],
            "changed_since_scan": a["file_sha256"] != known[rel].get("file_sha256"),
            "marker_state": a["marker_state"], "marker_detail": a["marker_detail"],
            "title": str((a.get("meta") or {}).get("title") or a.get("h1") or ""),
            "source_lines": len(st.normalize_text(text).split("\n")),
            "source_outline": outline(text),
            "existing_references": existing_references(rel, targets),
            "candidates": recommend(doc_signature(a, src), targets),
            "decision": "hold", "applicable": False,
            "reason": "검토 전 기본값 — 보류",
        }
        if rel in dec_items:
            validate_decision(vault, item, dec_items[rel], text, targets_by_path, taken, date_str)
        items.append(item)
    counts = {}
    for it in items:
        counts[it["decision"]] = counts.get(it["decision"], 0) + 1
    return {
        "kind": "stage-a-plan", "plan_version": PLAN_VERSION, "created_at": st.now_iso(),
        "vault": str(vault), "reviewer": (decisions or {}).get("reviewer", ""),
        "decision_counts": counts,
        "applicable": sum(1 for it in items if it["applicable"]),
        "items": items,
    }


# ──────────────────────────────────────────────────────────────────────────
# apply
# ──────────────────────────────────────────────────────────────────────────

class Applier:
    """수정안 1건씩 적용. 각 단계를 SQLite 에 먼저 기록해 중단 후 재실행으로 복구한다."""

    def __init__(self, vault: Path, state_dir: Path, plan: dict, plan_sha: str):
        self.vault, self.state_dir, self.plan, self.plan_sha = vault, state_dir, plan, plan_sha
        self.run_id = datetime.now().strftime("%Y%m%dT%H%M%S") + "-" + uuid.uuid4().hex[:6]
        self.conn = st.open_db(state_dir)
        self.date_str = datetime.now().strftime("%Y-%m-%d")
        self.results = []

    # ── 유틸 ──
    def backup(self, path: Path) -> str:
        rel = path.relative_to(self.vault)
        dest = self.state_dir / "backups" / self.run_id / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            shutil.copy2(path, dest)
            return str(dest)
        return "NEW"

    def event(self, rel, op_id, stage, detail=""):
        st.log_event(self.conn, self.run_id, rel, op_id, stage, detail)
        self.conn.commit()

    def record_source(self, item, status, reason, **extra):
        row = {"source_path": item["source"], "source_revision": item["source_revision_sha256"],
               "decision": item.get("decision"), "status": status, "reason": reason,
               "plan_sha256": self.plan_sha, "run_id": self.run_id}
        row.update(extra)
        st.upsert_source(self.conn, row)
        self.conn.commit()

    # ── 대상 반영 ──
    def apply_block(self, item, t) -> dict:
        """merge/new 한 건. 반환: {'ok':bool, 'reason':str, 'recovered':bool}"""
        rel_src = item["source"]
        kind, op_id = t["kind"], t["op_id"]
        target = st.safe_rel_path(self.vault, t["path"], st.TARGET_ROOTS)
        rev = item["source_revision_sha256"]

        if kind == "new":
            # 같은 작업 식별자의 블록이 이미 있는 파일을 찾는다 (반영 후 중단 복구)
            prev = st.get_op(self.conn, op_id)
            candidates = [target]
            if prev is not None and prev["target_path"] != t["path"]:
                candidates.insert(0, self.vault / prev["target_path"])
            for c in candidates:
                if c.is_file() and st.find_blocks(read_text(c), op_id):
                    return self._record_verified(item, t, c, recovered=True)
            # 충돌하지 않는 경로로 생성 (기존 파일 절대 덮어쓰지 않음)
            stem, n = target.stem, 2
            while target.exists():
                target = target.with_name(f"{stem}-{n}.md")
                n += 1
            text = render_new_note(item, op_id, self.date_str)
            st.upsert_op(self.conn, {
                "op_id": op_id, "source_path": rel_src, "source_revision": rev, "kind": kind,
                "target_path": str(target.relative_to(self.vault)), "stage": "intent",
                "target_sha_before": None, "backup_path": "NEW", "run_id": self.run_id})
            self.event(rel_src, op_id, "intent", str(target.relative_to(self.vault)))
            st.fault("before_target_write")
            st.atomic_create(target, text)
            st.fault("after_target_write")
            return self._record_verified(item, t, target, recovered=False)

        # merge
        if not target.is_file():
            return {"ok": False, "reason": "target_missing", "target": t["path"], "kind": kind}
        cur = read_text(target)
        if st.find_blocks(cur, op_id):
            return self._record_verified(item, t, target, recovered=True)
        cur_sha = st.sha256_text(st.normalize_text(cur))
        if cur_sha != t["target_sha256"]:
            return {"ok": False, "reason": "target_changed_since_plan — 재검토 필요",
                    "target": t["path"], "kind": kind}
        block = st.render_block(op_id, rel_src, rev, t.get("heading", ""), t["content"])
        new_text = st.insert_into_timeline(cur, block)
        backup = self.backup(target)
        st.upsert_op(self.conn, {
            "op_id": op_id, "source_path": rel_src, "source_revision": rev, "kind": kind,
            "target_path": t["path"], "stage": "intent", "target_sha_before": cur_sha,
            "backup_path": backup, "run_id": self.run_id})
        self.event(rel_src, op_id, "intent", t["path"])
        st.fault("before_target_write")
        st.atomic_write(target, new_text)
        st.fault("after_target_write")
        return self._record_verified(item, t, target, recovered=False)

    def _record_verified(self, item, t, target: Path, recovered: bool) -> dict:
        """다시 읽어 검증한 뒤에만 verified 로 기록한다."""
        text = read_text(target)
        ok, why, block = st.verify_block(text, t["op_id"], item["source"])
        prev = st.get_op(self.conn, t["op_id"])
        op = {"op_id": t["op_id"], "source_path": item["source"],
              "source_revision": item["source_revision_sha256"], "kind": t["kind"],
              "target_path": str(target.relative_to(self.vault)),
              "stage": "verified" if ok else "failed",
              "block_sha256": block["sha"] if block else None,
              "target_sha_after": st.sha256_text(st.normalize_text(text)),
              "error": None if ok else why, "run_id": self.run_id}
        if prev is None:  # 기록 저장 전에 중단됐던 경우: 복구본 정보가 없음을 명시
            op.update(backup_path="UNKNOWN(recovered)" if t["kind"] == "merge" else "NEW")
        st.fault("before_op_record")
        st.upsert_op(self.conn, op)
        self.event(item["source"], t["op_id"], op["stage"],
                   ("recovered " if recovered else "") + why)
        return {"ok": ok, "reason": why, "recovered": recovered,
                "target": op["target_path"], "kind": t["kind"]}

    def apply_evidence(self, item, t) -> dict:
        target = st.safe_rel_path(self.vault, t["path"], st.TARGET_ROOTS)
        if not target.is_file():
            return {"ok": False, "reason": "target_missing", "target": t["path"], "kind": "evidence"}
        text = st.normalize_text(read_text(target))
        quote = t["evidence_quote"]
        ok = quote in text and Path(item["source"]).stem in text
        st.upsert_op(self.conn, {
            "op_id": t["op_id"], "source_path": item["source"],
            "source_revision": item["source_revision_sha256"], "kind": "evidence",
            "target_path": t["path"], "stage": "verified" if ok else "failed",
            "evidence_sha256": st.sha256_text(quote), "evidence_text": quote,
            "target_sha_after": st.sha256_text(text),
            "error": None if ok else "evidence_missing", "run_id": self.run_id})
        self.event(item["source"], t["op_id"], "verified" if ok else "failed", "evidence")
        return {"ok": ok, "reason": "ok" if ok else "evidence_missing", "target": t["path"],
                "kind": "evidence"}

    # ── 완료 표시 ──
    def write_marker(self, item, src: Path, value: bool, note: str) -> bool:
        """원문 frontmatter 의 processed* 를 단일 값으로 정리. 본문이 바뀌었으면 쓰지 않는다."""
        text = read_text(src)
        a = st.analyze_source_text(text)
        if a["revision_sha256"] != item["source_revision_sha256"]:
            raise st.StageAError("완료 표시 직전 원문 내용 변경 감지")
        want = "marked_true" if value else "marked_false"
        if a["marker_state"] == want and value is False:
            return True
        op_id = st.make_op_id(item["source"], item["source_revision_sha256"], item["source"], "marker")
        backup = self.backup(src)
        new_text = st.set_processed_marker(text, value, note, self.date_str)
        st.upsert_op(self.conn, {
            "op_id": op_id, "source_path": item["source"],
            "source_revision": item["source_revision_sha256"], "kind": "marker",
            "target_path": item["source"], "stage": "intent",
            "target_sha_before": a["file_sha256"], "backup_path": backup, "run_id": self.run_id})
        self.conn.commit()
        st.fault("marker_write")
        st.atomic_write(src, new_text)
        b = st.analyze_source_text(read_text(src))
        ok = b["marker_state"] == want and b["revision_sha256"] == item["source_revision_sha256"]
        st.upsert_op(self.conn, {
            "op_id": op_id, "source_path": item["source"],
            "source_revision": item["source_revision_sha256"], "kind": "marker",
            "target_path": item["source"], "stage": "verified" if ok else "failed",
            "target_sha_after": b["file_sha256"], "run_id": self.run_id,
            "error": None if ok else f"marker_state={b['marker_state']}"})
        self.conn.commit()
        return ok

    def update_index(self, item, note_rel: str) -> str:
        idx_rel = item.get("index_path")
        if not idx_rel:
            return "not_needed"
        idx = st.safe_rel_path(self.vault, idx_rel, st.TARGET_ROOTS)
        stem = Path(note_rel).stem
        text = read_text(idx)
        # 정확한 위키 링크 단위로 중복 확인 ([[stem]] 또는 [[stem|표시]])
        if re.search(r"\[\[" + re.escape(stem) + r"(\|[^\]]*)?\]\]", text):
            return "written"
        op_id = st.make_op_id(item["source"], item["source_revision_sha256"], idx_rel, "index")
        backup = self.backup(idx)
        st.fault("index_write")
        new_text = text.rstrip("\n") + f"\n- [[{stem}]]\n"
        st.atomic_write(idx, new_text)
        st.upsert_op(self.conn, {
            "op_id": op_id, "source_path": item["source"],
            "source_revision": item["source_revision_sha256"], "kind": "index",
            "target_path": idx_rel, "stage": "verified",
            "target_sha_before": st.sha256_text(st.normalize_text(text)),
            "target_sha_after": st.sha256_text(new_text), "backup_path": backup,
            "run_id": self.run_id})
        self.conn.commit()
        return "written"

    # ── 항목 1건 ──
    def apply_item(self, item) -> dict:
        rel = item["source"]
        res = {"source": rel, "decision": item["decision"]}
        try:
            src = st.safe_rel_path(self.vault, rel, st.SOURCE_ROOTS)
        except st.StageAError as exc:
            return {**res, "result": "failed", "reason": str(exc)}
        if not src.is_file():
            return {**res, "result": "failed", "reason": "원문 없음"}
        a = st.analyze_source_text(read_text(src))

        if item["decision"] == "hold" or not item.get("applicable"):
            why = "; ".join(item.get("validation_errors") or []) or item.get("reason", "")
            self.record_source(item, "held", why, marker_status="none", index_status="none")
            return {**res, "result": "held", "reason": why}

        # 1) 원문 버전 대조 — 내용이 바뀌었으면 기존 수정안 적용 중단
        if a["revision_sha256"] != item["source_revision_sha256"]:
            self.event(rel, None, "source_changed", "")
            return {**res, "result": "needs_review",
                    "reason": "수정안 이후 원문 내용 변경 — 재검토 필요 (기존 수정안 적용 안 함)"}
        marker_only_change = a["file_sha256"] != item["source_file_sha256"]
        ms = a["marker_state"]
        if ms in ("yaml_error", "unsupported", "invalid_value"):
            self.record_source(item, "held", a["marker_detail"] or ms)
            return {**res, "result": "held", "reason": a["marker_detail"] or ms}
        if ms == "conflict" and not item.get("state_repair"):
            self.record_source(item, "held", "상태 충돌 — 증거 기반 복구안 필요")
            return {**res, "result": "held", "reason": "상태 충돌 — 증거 기반 복구안 필요"}

        # 2) 상태만 대기로 정리 (반영 증거 없는 충돌 문서)
        if item["decision"] == "reset_pending":
            ok = self.write_marker(item, src, False,
                                   f"stage-a {self.date_str}: 반영 증거 없음 — 대기로 정리")
            self.record_source(item, "pending", item["reason"],
                               marker_status="written" if ok else "failed",
                               index_status="not_needed")
            return {**res, "result": "state_reset_pending" if ok else "failed",
                    "reason": item["reason"], "marker_only_change": marker_only_change}

        # 3) 대상 반영 (또는 기존 반영 증거 확인)
        outcomes = []
        for t in item["targets"]:
            if t["kind"] == "evidence":
                outcomes.append(self.apply_evidence(item, t))
            else:
                outcomes.append(self.apply_block(item, t))
        self.conn.commit()
        if not item["targets"] or not all(o["ok"] for o in outcomes):
            why = "; ".join(f"{o.get('target', '')}: {o['reason']}" for o in outcomes if not o["ok"])
            self.record_source(item, "failed", why or "대상 없음", marker_status="none")
            return {**res, "result": "failed", "reason": why, "targets": outcomes}

        # 4) 검증 기록 → 실패하면 완료 표시하지 않음
        st.fault("before_verified_record")
        self.record_source(item, "verified", item["reason"], marker_status="pending",
                           index_status="pending")

        # 5) 완료 표시 (실패해도 내용은 재추가하지 않음 — 다음 실행에서 표시만 복구)
        note = (f"stage-a {item['decision']} → "
                + ", ".join(o.get("target", "") for o in outcomes))
        try:
            marker_ok = self.write_marker(item, src, True, note)
        except (OSError, st.StageAError) as exc:
            marker_ok = False
            self.event(rel, None, "marker_failed", str(exc))
        idx_status = "not_needed"
        if item["decision"] == "new":
            try:
                new_out = next(o for o in outcomes if o.get("kind") == "new")
                idx_status = self.update_index(item, new_out["target"])
            except (OSError, st.StageAError) as exc:
                idx_status = "failed"
                self.event(rel, None, "index_failed", str(exc))
        self.record_source(item, "verified", item["reason"],
                           marker_status="written" if marker_ok else "failed",
                           index_status=idx_status)
        recovered = any(o.get("recovered") for o in outcomes)
        return {**res, "result": "verified" if marker_ok else "verified_marker_failed",
                "recovered": recovered, "index_status": idx_status,
                "new_content": item["decision"] in ("new", "merge") and not recovered,
                "targets": outcomes, "marker_only_change": marker_only_change}

    def already_done(self, item) -> bool:
        """같은 원문 버전이 이미 검증 완료이고 표시까지 맞으면 아무것도 하지 않는다."""
        row = self.conn.execute("SELECT * FROM sources WHERE source_path=? AND source_revision=?",
                                (item["source"], item["source_revision_sha256"])).fetchone()
        if row is None or row["status"] != "verified" or row["marker_status"] != "written":
            return False
        if item["decision"] == "new" and row["index_status"] not in ("written", "not_needed"):
            return False
        src = self.vault / item["source"]
        a = st.analyze_source_text(read_text(src))
        status, _ = st.effective_status(self.vault, item["source"], a, self.conn)
        return status == "verified"


def do_apply(vault: Path, plan_path: Path, state_dir: Path, lock_dir: Path, max_items: int | None):
    raw = plan_path.read_bytes()
    plan = load_json(plan_path)
    if plan.get("kind") != "stage-a-plan" or plan.get("plan_version") != PLAN_VERSION:
        raise st.StageAError("stage-a 수정안 파일이 아님")
    if Path(plan["vault"]).resolve() != vault:
        # 복사본용 수정안을 운영 Vault 에 적용하는 사고를 막는다
        raise st.StageAError(f"수정안의 Vault({plan['vault']}) 와 실행 Vault({vault}) 불일치")
    plan_sha = st.sha256_bytes(raw)
    with st.vault_lock(vault, lock_dir):
        ap = Applier(vault, state_dir, plan, plan_sha)
        results, applied = [], 0
        for item in plan["items"]:
            if item.get("applicable") and max_items is not None and applied >= max_items:
                results.append({"source": item["source"], "decision": item["decision"],
                                "result": "deferred", "reason": "--max-items 제한"})
                continue
            if item.get("applicable") and ap.already_done(item):
                results.append({"source": item["source"], "decision": item["decision"],
                                "result": "already_verified", "reason": "같은 원문 버전 — 변경 없음"})
                continue
            try:
                r = ap.apply_item(item)
            except st.StageAError as exc:
                r = {"source": item["source"], "decision": item["decision"],
                     "result": "failed", "reason": str(exc)}
            results.append(r)
            if item.get("applicable"):
                applied += 1
        ap.conn.close()
    summary = {}
    for r in results:
        summary[r["result"]] = summary.get(r["result"], 0) + 1
    return {"kind": "stage-a-apply", "run_id": ap.run_id, "vault": str(vault),
            "plan": str(plan_path), "plan_sha256": plan_sha, "finished_at": st.now_iso(),
            "summary": summary,
            "new_content_applied": sum(1 for r in results if r.get("new_content")),
            "state_only": sum(1 for r in results if r["decision"] in
                              ("already_reflected", "reset_pending")
                              and r["result"] in ("verified", "state_reset_pending")),
            "results": results}


# ──────────────────────────────────────────────────────────────────────────
# verify
# ──────────────────────────────────────────────────────────────────────────

def do_verify(vault: Path, state_dir: Path) -> dict:
    conn = st.open_db_readonly(state_dir)
    scan = do_scan(vault, state_dir)
    report = {"kind": "stage-a-verify", "checked_at": st.now_iso(), "vault": str(vault),
              "state_dir": str(state_dir), "input_errors": scan["input_errors"],
              "marker_counts": scan["marker_counts"]}
    if conn is None:
        report.update(available=False, effective_counts=None,
                      message="처리 기록(SQLite) 없음 — 검증 완료를 추정하지 않음(집계 불가)")
        return report
    failures = []
    ops = conn.execute("SELECT * FROM operations WHERE stage='verified' "
                       "AND kind IN ('merge','new','evidence')").fetchall()
    for op in ops:
        ok, why = st.verify_operation(vault, op)
        if not ok:
            failures.append({"op_id": op["op_id"], "source": op["source_path"],
                             "target": op["target_path"], "reason": why})
    rows = {r["path"]: r for r in scan["sources"]}
    for r in scan["sources"]:
        if r.get("effective_status") == "failed":
            failures.append({"source": r["path"], "reason": r.get("status_reason", "")})
    counts = scan["effective_counts"]
    src_rows = conn.execute("SELECT decision, status, marker_status, COUNT(*) n FROM sources "
                            "GROUP BY decision, status, marker_status").fetchall()
    report.update(
        available=True, effective_counts=counts,
        verified_ops=len(ops), failures=failures,
        new_content_ops=conn.execute("SELECT COUNT(*) FROM operations WHERE stage='verified' "
                                     "AND kind IN ('merge','new')").fetchone()[0],
        record_breakdown=[dict(r) for r in src_rows],
        sources={p: {"effective_status": r.get("effective_status"),
                     "reason": r.get("status_reason")} for p, r in rows.items()
                 if r.get("effective_status") not in ("legacy_unverified", "pending")},
    )
    conn.close()
    return report


# ──────────────────────────────────────────────────────────────────────────
# restore
# ──────────────────────────────────────────────────────────────────────────

def do_restore(vault: Path, state_dir: Path, lock_dir: Path, run_id: str) -> dict:
    """
    run_id 의 변경을 복구본으로 되돌린다. 현재 파일이 apply 직후 해시와 같을 때만 되돌리고,
    이후 사용자 편집이 있으면 덮어쓰지 않고 충돌로 보고한다.
    신규 파일은 삭제하지 않고 상태 폴더의 restored-removed/ 로 옮긴다.
    """
    conn = st.open_db_readonly(state_dir)
    if conn is None:
        raise st.StageAError("처리 기록 없음 — 복구 불가")
    conn.close()
    out = []
    with st.vault_lock(vault, lock_dir):
        conn = st.open_db(state_dir)
        ops = conn.execute("SELECT * FROM operations WHERE run_id=? AND backup_path IS NOT NULL "
                           "ORDER BY updated_at DESC", (run_id,)).fetchall()
        if not ops:
            raise st.StageAError(f"run_id 에 해당하는 복구 기록 없음: {run_id}")
        for op in ops:
            path = vault / op["target_path"]
            cur = st.sha256_text(st.normalize_text(read_text(path))) if path.is_file() else None
            entry = {"op_id": op["op_id"], "path": op["target_path"], "kind": op["kind"]}
            if cur != op["target_sha_after"]:
                entry.update(result="conflict", reason="apply 이후 파일이 변경됨 — 덮어쓰지 않음")
            elif op["backup_path"] == "NEW":
                dest = state_dir / "restored-removed" / run_id / op["target_path"]
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(path), str(dest))
                entry.update(result="removed_new_file", moved_to=str(dest))
            elif op["backup_path"].startswith("UNKNOWN"):
                entry.update(result="conflict", reason="복구본 없음(중단 복구 건)")
            else:
                st.atomic_write(path, read_text(Path(op["backup_path"])))
                entry.update(result="restored", from_backup=op["backup_path"])
            if entry["result"] in ("restored", "removed_new_file"):
                st.upsert_op(conn, {"op_id": op["op_id"], "source_path": op["source_path"],
                                    "source_revision": op["source_revision"], "kind": op["kind"],
                                    "target_path": op["target_path"], "stage": "restored",
                                    "run_id": op["run_id"]})
                conn.execute("UPDATE sources SET status='pending', reason='restored' "
                             "WHERE source_path=? AND source_revision=?",
                             (op["source_path"], op["source_revision"]))
            out.append(entry)
        conn.commit()
        conn.close()
    return {"kind": "stage-a-restore", "run_id": run_id, "results": out,
            "conflicts": sum(1 for e in out if e["result"] == "conflict")}


# ──────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="단계 A 편입 처리기 (scan/plan/apply/verify/restore)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("scan", help="원문 탐색 (읽기 전용)")
    s.add_argument("--vault", required=True)
    s.add_argument("--output", required=True)
    s.add_argument("--state-dir", help="지정 시 처리 기록을 읽기 전용으로 대조")

    p = sub.add_parser("plan", help="수정안 생성 (읽기 전용)")
    p.add_argument("--vault", required=True)
    p.add_argument("--manifest", required=True, help="scan 결과 JSON")
    p.add_argument("--output", required=True)
    p.add_argument("--decisions", help="검토자 결정 JSON (없으면 전부 보류)")
    p.add_argument("--only", nargs="*", help="수정안에 포함할 원문 상대 경로")
    p.add_argument("--only-file", help="원문 상대 경로 목록 파일(JSON 배열 또는 줄 단위)")

    a = sub.add_parser("apply", help="수정안 적용")
    a.add_argument("--vault", required=True)
    a.add_argument("--plan", required=True)
    a.add_argument("--state-dir", required=True)
    a.add_argument("--report", required=True)
    a.add_argument("--lock-dir", default=str(st.default_lock_dir()))
    a.add_argument("--max-items", type=int, default=None, help="이번 실행의 적용 건수 상한")

    v = sub.add_parser("verify", help="처리 기록과 본문 대조 (읽기 전용)")
    v.add_argument("--vault", required=True)
    v.add_argument("--state-dir", required=True)
    v.add_argument("--report", required=True)

    r = sub.add_parser("restore", help="복구본으로 되돌리기")
    r.add_argument("--vault", required=True)
    r.add_argument("--state-dir", required=True)
    r.add_argument("--run-id", required=True)
    r.add_argument("--report", required=True)
    r.add_argument("--lock-dir", default=str(st.default_lock_dir()))

    args = ap.parse_args(argv)
    try:
        vault = st.resolve_vault(args.vault)
        if args.cmd == "scan":
            out = st.ensure_outside(vault, Path(args.output), "scan 결과")
            sd = st.ensure_outside(vault, Path(args.state_dir), "상태 폴더") if args.state_dir else None
            res = do_scan(vault, sd)
            write_json(out, res)
            print(json.dumps({"output": str(out), "total": res["total"],
                              "marker_counts": res["marker_counts"],
                              "input_errors": len(res["input_errors"])}, ensure_ascii=False))
            return 2 if res["input_errors"] else 0
        if args.cmd == "plan":
            out = st.ensure_outside(vault, Path(args.output), "수정안")
            manifest = load_json(Path(args.manifest))
            decisions = load_json(Path(args.decisions)) if args.decisions else None
            only = list(args.only or [])
            if args.only_file:
                txt = Path(args.only_file).read_text(encoding="utf-8")
                only += json.loads(txt) if txt.lstrip().startswith("[") else \
                    [ln.strip() for ln in txt.splitlines() if ln.strip()]
            res = do_plan(vault, manifest, decisions, only or None)
            write_json(out, res)
            print(json.dumps({"output": str(out), "items": len(res["items"]),
                              "applicable": res["applicable"],
                              "decision_counts": res["decision_counts"]}, ensure_ascii=False))
            return 0
        if args.cmd == "apply":
            sd = st.ensure_outside(vault, Path(args.state_dir), "상태 폴더")
            rep = st.ensure_outside(vault, Path(args.report), "보고서")
            res = do_apply(vault, Path(args.plan), sd, Path(args.lock_dir), args.max_items)
            write_json(rep, res)
            print(json.dumps({"report": str(rep), "run_id": res["run_id"],
                              "summary": res["summary"]}, ensure_ascii=False))
            bad = {"failed", "needs_review", "verified_marker_failed"}
            return 4 if any(r["result"] in bad for r in res["results"]) else 0
        if args.cmd == "verify":
            sd = st.ensure_outside(vault, Path(args.state_dir), "상태 폴더")
            rep = st.ensure_outside(vault, Path(args.report), "보고서")
            res = do_verify(vault, sd)
            write_json(rep, res)
            print(json.dumps({"report": str(rep), "available": res["available"],
                              "effective_counts": res.get("effective_counts"),
                              "failures": len(res.get("failures") or [])}, ensure_ascii=False))
            if not res["available"]:
                return 3
            return 4 if res["failures"] else 0
        if args.cmd == "restore":
            sd = st.ensure_outside(vault, Path(args.state_dir), "상태 폴더")
            rep = st.ensure_outside(vault, Path(args.report), "보고서")
            res = do_restore(vault, sd, Path(args.lock_dir), args.run_id)
            write_json(rep, res)
            print(json.dumps({"report": str(rep), "conflicts": res["conflicts"],
                              "restored": len(res["results"]) - res["conflicts"]},
                             ensure_ascii=False))
            return 4 if res["conflicts"] else 0
    except st.StageAError as exc:
        print(f"오류: {exc}", file=sys.stderr)
        return 3 if "잠금" in str(exc) or "처리 기록" in str(exc) else 2
    return 1


if __name__ == "__main__":
    sys.exit(main())
