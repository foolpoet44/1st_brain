---
type: Analysis
related_to: ["[[AI-Native-Company-Roadmap]]", "[[digital-exoskeleton]]"]
date: 2026-05-30
---
# [MASTER PLAN] AI 네이티브 조직으로의 진화: Josh Kim & Jeongmin Lee 통합 모델

## 1. 개요
본 리포트는 2026년 5월 말 공유된 Josh Kim과 Jeongmin Lee의 AI 네이티브 조직 구축 인사이트를 통합하여, `csp-brain` 시스템의 운영 고도화 및 고객 AX 컨설팅을 위한 마스터 플랜을 제안합니다.

## 2. 5대 핵심 아키텍처 (Integrated Architecture)

### ❶ 지식 대사 작용 (Knowledge Metabolism - Data Layer)
- **맥락의 상시 적재**: 슬랙, 회의록, 노션 등 파편화된 비정형 데이터를 AI-Readable한 마크다운 자산으로 실시간 변환.
- **이벤트 트리거형 파일 생성**: 데이터 입력 시 AI 전용 Read 파일(Context Corpus)을 생성하여 모델의 추론 정확도 향상.

### ❷ 도구적 자아 (Skill as Employee - Execution Layer)
- **Skill-ify**: 반복 작업과 전문가의 노하우를 '가상 직원(Skill)'으로 자격화하여 등록.
- **Resolver(조직도)**: 거대 지시문(System Prompt)을 지양하고, 필요할 때만 해당 스킬/파일을 호출하는 포인터 기반 리졸버 운영.

### ❸ 자가 개선 루프 (Self-Improving Loop - Strategy Layer)
- **크론잡 기반 복기**: 매일 아침/저녁 정해진 시간에 데이터 업데이트 및 업무 스트림라인 제안.
- **인사 평가로서의 Eval**: 에이전트의 결과물을 정기적으로 평가(LLM-as-a-judge)하여 시스템의 신뢰도 확보.

### ❹ 보안 거버넌스 (Governance - Guard Layer)
- **권한 관리의 세분화**: 구성원별 AI 리터러시와 데이터 접근 권한을 매핑하는 보안 거버넌스 수립.
- **보안 전담 AI 운영**: '오버쉐어링 방지'를 자동 감시하는 에이전트 레이어 배치.

### ❺ 자산화된 프로세스 (Process as Code - Asset Layer)
- **파일명이 곧 프로세스**: 폴더 구조와 파일 규칙 자체가 회사의 일하는 방식이 됨.
- **Codex/Hermes 기반 Tooling**: 사내 ERP 등 필요한 도구는 에이전트가 직접 코딩하고 배포(Git/Vercel 연동).

## 3. CSP-Brain NEXT ACTIONS
1. **Resolver 도입**: 현재의 `SKILL.md` 체계를 더 세분화하여, 특정 조건에서만 로드되는 '포인터 기반 스킬 호출' 로직 강화.
2. **Cronjob 고도화**: 매일 저녁 수행되는 `REFLECT` 프로토콜에 Josh Kim 식의 '업무 태스크 제안' 자동 생성 기능 추가.
3. **Security Audit**: 지식 그래프 상의 '민감 정보'를 식별하고 관리하는 보안 프로토콜 설계.
