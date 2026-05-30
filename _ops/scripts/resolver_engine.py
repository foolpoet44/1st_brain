import os

class ResolverEngine:
    """
    CSP-Brain Synaptic Resolver Engine v1.0
    의도를 분석하여 최적의 파일 맥락을 추천합니다.
    """
    def __init__(self):
        self.mapping = {
            "HR": ["채용", "면접", "평가", "연봉", "조직", "HR", "심리", "역량"],
            "AI": ["에이전트", "MCP", "코드", "자동화", "토큰", "프롬프트", "리졸버"],
            "SYSTEM": ["성찰", "업데이트", "대시보드", "맥박", "로그", "진화"],
            "INVEST": ["투자", "경제", "시장", "지표", "레포트", "분석"]
        }
        
    def resolve(self, query):
        detected_domains = []
        for domain, keywords in self.mapping.items():
            if any(keyword in query for keyword in keywords):
                detected_domains.append(domain)
        
        recommendations = []
        # Domain to Path Mapping
        if "HR" in detected_domains:
            recommendations.extend(["wiki/concepts/hr-conceptual-atoms.md", "projects/oka/"])
        if "AI" in detected_domains:
            recommendations.extend(["wiki/concepts/agentic-engineering.md", "_ops/RESOLVER.md"])
        if "SYSTEM" in detected_domains:
            recommendations.extend(["KNOWLEDGE_PULSE.md", "_ops/change-log.md"])
        if "INVEST" in detected_domains:
            recommendations.append("outputs/analyses/INVESTMENT_memo.md")
            
        return list(set(recommendations))

if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ""
    engine = ResolverEngine()
    files = engine.resolve(query)
    for f in files:
        print(f)
