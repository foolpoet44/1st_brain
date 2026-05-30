---
type: Signal
source: LinkedIn/X (@gonnector)
date: 2026-05-30
tags: ["anthropic", "claude-4.8", "prompt-engineering", "infra"]
url: https://www.linkedin.com/posts/gonnector_ai-agent-claude-share-7465905827950895105-ZUvt/
---
# [SIGNAL] Claude Opus 4.8: 바닐라 모델의 승리와 제어 파라미터의 시대

## 💡 핵심 철학의 전환
Anthropic은 4.8 모델에서 모델을 다그치는 'Anti-laziness' 스캐폴딩(예: "중간에 멈추지 마", "끝까지 답해")을 제거하고, **Effort 레버**와 **명시적 범위 지정**으로 조절할 것을 권고합니다.

## 🚀 10개 핵심 포인트 (Full Detail)
1. **응답 길이 자동 보정 (Verbosity Calibration)**: 작업 복잡도에 따라 길이를 스스로 판단. 단순 조회는 짧게, 분석은 길게.
2. **Effort 파라미터의 준거성**: xhigh/high 레벨이 지능 민감 작업에 필수. low 레벨에서는 지시한 범위 '딱 거기까지만' 수행함.
3. **Thinking 기본 OFF**: `thinking: {type: "adaptive"}`를 명시적으로 설정해야 활성화됨.
4. **추론 선호와 툴 호출**: 모델이 추론(Reasoning)을 선호하여 툴 호출이 줄어들 수 있음. 툴 사용이 필요하면 Effort를 올려야 함.
5. **규칙적 진행 상황 업데이트**: 모델 자체의 업데이트 품질이 향상되어 "3번마다 요약하라"는 식의 강제 스캐폴딩 제거 권장.
6. **극도로 명시적인 해석 (Literal Interpretation)**: 프롬프트를 문자 그대로 해석함. 일반화가 필요하면 모든 섹션에 적용하라고 명시해야 함.
7. **직설적 톤 (Direct Opinionated Style)**: 이모지나 맞장구성 표현이 줄어들고 건조하고 명확한 스타일로 변경됨.
8. **디자인 하우스 스타일 보유**: 크림색 배경, 세리프 폰트 등의 고유 미학을 가짐. 부정 지시보다는 구체적 대안 스펙 제시가 효과적.
9. **코드 리뷰 하니스의 recall 이슈**: 하이 세버리티만 보고하라는 지시를 너무 잘 따라 recall이 낮아 보일 수 있으니 발견 단계에서는 제약을 풀 것.
10. **인터랙티브 코딩 최적화**: 다중 턴 작업에서 토큰을 더 많이 쓰는 경향. 첫 턴에 의도와 제약을 명확히 명시하는 것이 효율 극대화.

## 🛠️ CSP-Brain 적용 전략
- **Resolver 고도화**: 질문의 복잡도를 에이전트가 사전 판별하여 API 호출 시 `effort: "xhigh"` 등을 동적으로 할당하는 로직 추가.
- **Harness Scaffolding 제거**: `CLAUDE.md` 내의 중복된 강조와 모델 다그치기 문구들을 삭제하여 '바닐라 성능' 극대화.
- **Literal Prompting**: "이 문서 전체에 적용해" 보다는 "전체 문서를 훑고 각 섹션마다 적용해"와 같이 범위를 명시적으로 지정하도록 가이드 수정.
