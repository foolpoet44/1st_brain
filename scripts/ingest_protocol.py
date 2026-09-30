#!/usr/bin/env python3
"""
INGEST 프로토콜 — 읽기 전용 안내 진입점 (2026-09-30 단계 A 개편)

이전 버전은 다음 결함 때문에 '완료 표시'가 실제 편입을 증명하지 못했다.
  - 공통 숫자(예: 2026)나 제목 부분 문자열만으로 첫 후보 문서에 병합
  - 병합 시 출처·날짜 한 줄만 Timeline 에 추가하고 새 내용은 반영하지 않음
  - 'processed: false' 뒤에 'processed: true' 를 덧붙여 상태 충돌 생성
  - 오늘 날짜 브리핑만 탐색, 내용 없는 TODO 신호 노트 생성

그래서 이 파일의 자동 처리(병합·신규 생성·완료 표시)는 제거했다.
인자 없이 실행하면 Vault 를 전혀 바꾸지 않고, 현재 상태와 수정안 골격만 보여준다.
실제 편입은 검증 가능한 명시적 경로로만 한다:

    python3 scripts/stage_a_ingest.py scan   --vault PATH --output FILE
    python3 scripts/stage_a_ingest.py plan   --vault PATH --manifest FILE --output FILE [--decisions FILE]
    python3 scripts/stage_a_ingest.py apply  --vault PATH --plan FILE --state-dir PATH --report FILE
    python3 scripts/stage_a_ingest.py verify --vault PATH --state-dir PATH --report FILE
"""

import argparse
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_state as st  # noqa: E402
import stage_a_ingest as sa  # noqa: E402

VAULT_PATH = "/Users/dkmac/csp-brain"


def main():
    ap = argparse.ArgumentParser(description="읽기 전용: 편입 상태와 수정안 골격 미리보기")
    ap.add_argument("--vault", default=VAULT_PATH)
    ap.add_argument("--state-dir", default=None, help="처리 기록 폴더(읽기 전용 대조)")
    ap.add_argument("--out-dir", default=None, help="미리보기 저장 폴더 (기본: 임시 폴더, Vault 밖)")
    args = ap.parse_args()

    try:
        vault = st.resolve_vault(args.vault)
        out_dir = Path(args.out_dir) if args.out_dir else Path(tempfile.mkdtemp(prefix="stage-a-preview-"))
        out_dir = st.ensure_outside(vault, out_dir, "미리보기 폴더")
        sd = st.ensure_outside(vault, Path(args.state_dir), "상태 폴더") if args.state_dir else None
        scan = sa.do_scan(vault, sd)
        plan = sa.do_plan(vault, scan, None, None)  # 결정 파일 없음 → 전부 보류(읽기 전용)
    except st.StageAError as exc:
        print(f"오류: {exc}", file=sys.stderr)
        return 2

    out_dir.mkdir(parents=True, exist_ok=True)
    sa.write_json(out_dir / "scan.json", scan)
    sa.write_json(out_dir / "plan-skeleton.json", plan)

    print("=" * 60)
    print("INGEST 미리보기 (읽기 전용 — Vault 변경 없음)")
    print("=" * 60)
    print(f"Vault: {vault}")
    print(f"원문 {scan['total']}개 · 표시 상태: {json.dumps(scan['marker_counts'], ensure_ascii=False)}")
    if scan["effective_counts"] is not None:
        print(f"검증 상태: {json.dumps(scan['effective_counts'], ensure_ascii=False)}")
    if scan["input_errors"]:
        print(f"⚠️ 입력 오류 {len(scan['input_errors'])}건 — '전부 완료'로 보지 않음")
    print(f"\n미리보기 저장: {out_dir}")
    print("다음 단계: plan-skeleton.json 을 검토해 결정 파일을 만든 뒤 stage_a_ingest.py plan/apply/verify 실행")
    return 2 if scan["input_errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
