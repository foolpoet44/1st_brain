import random

class InterviewGen:
    def __init__(self):
        self.question_bank = {
            "분석": [
                "데이터가 부족한 상황에서 논리적인 결론을 도출해야 했던 경험을 말씀해주세요.",
                "복잡한 데이터를 비전문가에게 쉽게 설명하여 설득했던 사례가 있습니까?"
            ],
            "실행": [
                "마감 기한이 촉박한 상황에서 예기치 못한 장애물이 발생했을 때 어떻게 대처했나요?",
                "품질과 속도 사이에서 갈등했던 경험과 그 해결책을 말씀해주세요."
            ],
            "적응": [
                "조직의 급격한 방향 전환(Pivot) 상황에서 본인의 역할을 어떻게 재정의했습니까?",
                "가치관이 다른 구성원과 협업하며 본인의 방식을 수정해야 했던 사례가 있나요?"
            ],
            "영향력": [
                "상반된 이해관계를 가진 팀들 사이에서 중재안을 이끌어낸 경험을 말씀해주세요.",
                "권한이 없는 상태에서 타인의 협력을 이끌어내어 성과를 거둔 사례를 공유해주세요."
            ]
        }

    def generate(self, scores):
        # 점수가 가장 낮은 클러스터를 찾아 우선 질문 생성
        low_clusters = [k for k, v in scores.items() if v < 4] # 10점 만점 기준 4점 미만
        
        proposals = []
        for cluster in low_clusters:
            if cluster in self.question_bank:
                question = random.choice(self.question_bank[cluster])
                proposals.append(f"### [심층 검증: {cluster}]\n- **질문**: {question}\n- **의도**: 해당 역량의 보완 가능성 및 성찰 능력 확인.")
        
        if not proposals:
            return "모든 역량이 우수합니다. 전체적인 가치관 통합 질문을 제안합니다: '본인의 강점들이 조직의 장기 미션과 어떻게 시너지를 낼 수 있다고 생각하십니까?'"
            
        return "\n\n".join(proposals)

if __name__ == "__main__":
    # 가짜 데이터 테스트 (Mock Data)
    mock_scores = {"분석": 8, "실행": 3, "적응": 7, "영향력": 2}
    gen = InterviewGen()
    print("\n--- 🤖 AI HR 면접 가이드 --- ")
    print(gen.generate(mock_scores))
