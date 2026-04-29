# Extracted Knowledge from Conv: b44e0b01-4db3-4225-b05b-4ed2e86b0de6

**Date**: 2026-03-26T04:56:21.002838Z

### Extracted Code (css)

```css
--red: #A50034        /* LG 브랜드 컬러 — 주요 강조 */
--red-light: #f9e6ec  /* 카드 보더, 배경 */
--yellow: #FBBF24     /* 배지, 하이라이트 */
--dark: #1a1a2e       /* Hero 배경 베이스 */
```

### Extracted Code (text)

```text
[top-bar]
  └── .tb-left: LG 로고 + 수직 구분선 + 페이지 타이틀
  └── .tb-right: 배지 (index) / 뒤로가기 링크 (하위 페이지)
  
[hero]
  └── 배경: linear-gradient(165deg, #0d0d0d → #1a1a2e → #0f3460)
  └── ::before: radial-gradient 레이어 (반투명 red glow)
  └── .hero-eyebrow: 대문자 + letter-spacing (컨텍스트 라벨)
  └── .hero-title: clamp() 반응형
  └── .hero-desc: 설명문
```

### Extracted Code (css)

```css
@media(max-width: 1100px) { grid-template-columns: repeat(2, 1fr) }
@media(max-width: 600px)  { grid-template-columns: 1fr }
```

### Extracted Code (text)

```text
y26-hr-html-builder/
├── SKILL.md              ← 워크플로우 + 트리거 조건
└── references/
    ├── design-tokens.md  ← CSS 변수, 컬러 팔레트, 타이포그래피
    ├── components.md     ← top-bar, hero, card, tab 컴포넌트 템플릿
    └── patterns.md       ← 페이지 타입별 레이아웃 패턴
```

### Extracted Code (text)

```text
SKILL.md (113줄)         ← 트리거 조건 + 5단계 워크플로우
references/
  design-tokens.md (182줄)  ← CSS 변수, 컬러, 타이포, Hero 그라디언트
  components.md (427줄)     ← 11개 컴포넌트 템플릿 (copy-paste 가능)
  page-patterns.md (180줄)  ← 4가지 레이아웃 패턴 + 판단 트리
```
