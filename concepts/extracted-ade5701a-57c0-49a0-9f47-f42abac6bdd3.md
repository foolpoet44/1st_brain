# Extracted Knowledge from Conv: ade5701a-57c0-49a0-9f47-f42abac6bdd3

**Date**: 2026-03-11T05:08:57.871314Z

### Extracted Code (text)

```text
Create a modern, visually stunning single-page website that introduces Lovable.dev 
to Korean HR professionals and non-developers.

## Design Requirements
- Hero section with animated gradient background (purple → blue → indigo tones)
- Glassmorphism card design throughout
- Smooth scroll animations (fade-in on scroll)
- Fully responsive (mobile-first)
- Korean language content
- Dark mode default

## Page Structure

### 1. Hero Section
- Large headline: "아이디어가 있다면, 앱을 만들 수 있습니다"
- Subheadline: "코드 없이, 대화만으로 풀스택 웹앱을 완성하는 AI 빌더"
- Two CTA buttons: "지금 시작하기" (primary) / "데모 보기" (secondary)
- Animated floating UI mockup or abstract tech visual

### 2. What is Lovable Section
- Three-column feature cards with icons:
  Card 1: "자연어로 개발" — 영어든 한국어든 말하듯 입력하면 React 앱이 생성됩니다
  Card 2: "풀스택 자동화" — Frontend(React), Backend(Supabase), 배포까지 원클릭
  Card 3: "코드 소유권" — GitHub 연동으로 생성된 코드를 직접 소유하고 수정 가능

### 3. Tech Stack Visualization
- Show the stack: React + Tailwind + Supabase + Vercel
- Visual flow diagram: "아이디어 → 프롬프트 → 앱 완성"
- Add small badge: "Powered by Claude Sonnet (Anthropic)"

### 4. Who Is It For Section
- Target persona cards (3 types):
  Persona 1: HR 담당자 — "평가 시스템, 설문, 온보딩 앱을 직접 만들고 싶은 분"
  Persona 2: 기획자/PM — "개발자 없이 MVP를 검증하고 싶은 분"
  Persona 3: 창업 준비자 — "SaaS 아이디어를 빠르게 시장에 던져보고 싶은 분"

### 5. Use Case Examples
- Horizontal scroll card gallery with 5 example apps:
  "1on1 아젠다 자동 생성기" / "조직 건강도 Pulse Check 앱" / 
  "역량 평가 퀴즈 플랫폼" / "리더십 피드백 대시보드" / "팀 무드 트래커"
- Each card has: app name, short description, "Lovable로 만든 앱" badge

### 6. How It Works (Step-by-step)
- Numbered steps with connecting line visual:
  Step 1: "아이디어를 문장으로 입력"
  Step 2: "AI가 코드를 실시간 생성"
  Step 3: "미리보기에서 즉시 확인"
  Step 4: "수정 요청을 대화로 반복"
  Step 5: "완성 후 즉시 배포"

### 7. Pricing Teaser
- Simple 2-tier card: Free / Pro
- Highlight: "무료로 시작, 확장할 때 업그레이드"
- CTA: "lovable.dev 바로가기" button

### 8. Footer
- Tagline: "당신의 아이디어가 코드가 되는 순간"
- Links: Lovable.dev / GitHub / Discord

## Technical Specs
- Use shadcn/ui components
- Framer Motion for scroll animations
- lucide-react for icons
- No external API calls needed
- All content hardcoded in Korean
```

### Extracted Code (text)

```text
Add a live typing animation in the hero section that cycles through these 
Korean phrases: "HR 평가 시스템 만들어줘" → "팀 무드 트래커 앱 만들어줘" 
→ "온보딩 체크리스트 앱 만들어줘"
This should look like someone typing into a Lovable prompt input box.
```

### Extracted Code (text)

```text
Add a interactive demo section where users can click one of 3 preset prompts 
and see a simulated "AI is generating your app..." loading animation, 
then reveal a mock app screenshot. All in Korean UI.
```
