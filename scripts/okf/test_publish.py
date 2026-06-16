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


if __name__ == "__main__":
    unittest.main()
