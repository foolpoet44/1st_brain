---
type: Project
status: Active
tags: [hr-tech, psy-assess, automation]
related_to: "[[opq-framework]]"
---

# OKA Project

## 1. 미션

심리 진단 데이터를 구조화하고 이를 기반으로 HR 운영(채용, 배치, 육성)의 자동화 및 인텔리전스를 실현하는 "Vibe Coding" 프로젝트.

## 2. 주요 아키텍처

- **Data Sources**: OPQ32, 8-Cluster 심리 진단 결과.
- **Knowledge Layer**: `csp-brain` 7-Layer Architecture 기반의 시맨틱 데이터 저장소.
- **Automation**: 진단 결과 PDF의 자동 인제스천 및 인사이트 리포트 생성 스크립트.

## 3. 타임라인

### 2026-05-16

- **심리 진단 모델 통합**: OPQ32 프레임워크를 지식 체계에 이식.
- **분석 리포트 생성**: `Psy_assess-OPQ.pdf` 기반의 핵심 역량 클러스터 분석 완료.
- **시스템 인제스천**: `wiki/concepts`와 `outputs/analyses`에 관련 지식 업데이트.

### 2026-05-31 (Planned)

- **[[AgentSchool Simulation]]**: 에이전트를 활용한 조직 사회적 역동 시뮬레이션 마일스톤 착수.

### 2026-06-11
- **심리 진단 요약 인제스천 완료**: `hermes/` 디렉토리에 대기 중이던 `Psy_assess_summary.md`를 Vault의 `outputs/analyses/`로 정식 편입.
- **지식 대사(Metabolism) 활성화**: 심리 진단 지표(Resilience, Engagement 등)를 시스템의 추론 근거로 활성화.

### 2026-07-11 (Current)
- **OKA 분석 결과 최종 적용**: 분석된 심리 진단 요약(`psy-assess-summary.md`)을 기반으로 지식 구조를 확정하고, `csp-brain` Vault 내의 지식 맥락을 갱신함.
- **지휘자(Orchestrator) 모드 가동**: 분석 결과가 시스템의 핵심 IP(Eval)로 전이될 수 있도록 검증 및 동기화 절차 수행.

## 4. 핵심 지표 (Atoms)

- Resilience (회복탄력성)
- Job Engagement (직무 몰입)
- Stress Tolerance (스트레스 내성)
- 8-Cluster Competency Model

### 관련 지식 연결 (Backlinks)

- [[vibe-coding]]
- [[7-layer-architecture]]
