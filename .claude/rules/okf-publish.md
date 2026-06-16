# OKF PUBLISH 프로토콜 (7번째 프로토콜)

> 설계: `_ops/okf/OKF_ADOPTION_SPEC.md` · 실행: `_ops/okf/OKF_PUBLISH_PROTOCOL.md` · 구현: `scripts/okf/`

## 트리거

- `publish` → 옵시디언 작성본을 OKF conformant 번들로 발행(`dist/okf/`).
- `lint` / `점검` → **conformance checker로 승격**(SPEC §8). 기존 LINT 프로토콜은 이제
  `python -m scripts.okf.publish --only conformance`로 측정 가능한 게이트가 된다.

## 핵심 규칙

1. **작성본 비파괴.** 발행은 `dist/okf/`로만. 작성본(wiki/·projects/ 등) 수정 금지.
2. **기본 dry-run.** 실제 쓰기는 `--write`. 파괴적 변경(정크 이동/삭제)은 사람 확인 후.
3. **번들 IN (Phase 0 확정):** `wiki/`, `projects/`, `references/`, `research/`, `analysis/`.
   루트 `concepts/`(추출 덤프)·`people/`(슬라이드)·빈 폴더는 제외.
4. **게이트:** ERROR 0 = PASS. `--strict`면 WARN 도 실패.

## LINT 실행

```bash
python -m scripts.okf.publish --only conformance            # 미리보기
python -m scripts.okf.publish --only conformance --write     # dist/okf/lint-report.md
```

결과 베이스라인은 `_ops/okf/lint-baseline-*.md`로 추적(트렌드). 실행 이력은 `_ops/lint-log.md`.
