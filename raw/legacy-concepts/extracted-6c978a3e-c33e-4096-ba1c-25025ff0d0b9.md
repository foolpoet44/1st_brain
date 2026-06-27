# Extracted Knowledge from Conv: 6c978a3e-c33e-4096-ba1c-25025ff0d0b9

**Date**: 2026-03-30T02:09:37.097654Z

### Extracted Code (text)

```text
pulse-check-webform/
├── package.json                          (Next.js 14 + Supabase SSR)
├── tsconfig.json / next.config.js
├── tailwind.config.ts / postcss.config.js
├── .env.local.example
├── supabase/
│   └── migrations/
│       └── 001_initial_schema.sql        ← DoD C-1, C-2, D-1, D-2, D-3 전부 커버
├── src/
│   ├── types/index.ts                    ← 전체 타입 정의
│   ├── lib/
│   │   ├── supabase/client.ts            (브라우저 클라이언트)
│   │   ├── supabase/server.ts            (서버 클라이언트)
│   │   ├── crypto.ts                     ← DoD D-1: SHA-256 해싱
│   │   └── questions.ts                  ← DoD B-1: 주관식 문항 4개 + 동의 텍스트
│   └── app/
│       ├── layout.tsx
│       └── actions.ts                    ← DoD A-1, C-1, C-2, D-1, D-2, D-3 서버 액션
```

### Extracted Code (text)

```text
pulse-check-webform/
├── package.json                          Next.js 14 + Supabase SSR 의존성
├── tsconfig.json / next.config.js
├── tailwind.config.ts / postcss.config.js
├── .env.local.example                    → 이걸 .env.local로 복사 후 키 입력
│
├── supabase/migrations/
│   └── 001_initial_schema.sql            DoD C-1,C-2,D-1,D-2,D-3 테이블+RLS
│
└── src/
    ├── types/index.ts                    전체 타입 정의
    ├── lib/
    │   ├── supabase/client.ts            브라우저 클라이언트
    │   ├── supabase/server.ts            서버 클라이언트
    │   ├── crypto.ts                     DoD D-1: SHA-256 해싱
    │   └── questions.ts                  DoD B-1: 주관식 문항 4개
    └── app/
        ├── layout.tsx
        └── actions.ts                    DoD A-1,C-1,C-2,D-1~D-3 서버 액션
```
