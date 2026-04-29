# Extracted Knowledge from Conv: 56a4f7f1-0b14-41f2-803c-6fa0fd54ba46

**Date**: 2026-01-23T23:19:23.488569Z

### Extracted Code (bash)

```bash
# Claude Code 설치 (NPM 방식)
npm install -g @anthropic-ai/claude-code

# 또는 다운로드 방식
# https://claude.ai/code 에서 직접 다운로드
```

### Extracted Code (bash)

```bash
# Gemini API 키 발급
# https://makersuite.google.com/app/apikey

# 환경 변수 설정 (.bashrc 또는 .zshrc)
export GEMINI_API_KEY="your-api-key-here"

# Python에서 사용
pip install google-generativeai
```

### Extracted Code (python)

```python
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# 간단한 테스트
response = model.generate_content("안녕하세요!")
print(response.text)
```

### Extracted Code (text)

```text
my-agent/
├── agents/
│   ├── researcher.py      # 리서치 에이전트
│   ├── writer.py          # 작성 에이전트
│   └── analyzer.py        # 분석 에이전트
├── config/
│   └── prompts.yaml       # 프롬프트 관리
├── data/
│   ├── input/            # 입력 데이터
│   └── output/           # 결과물 (md 파일들)
├── utils/
│   └── gemini_client.py  # Gemini API 래퍼
└── main.py               # 오케스트레이터
```

### Extracted Code (yaml)

```yaml
researcher:
  system: |
    당신은 정보를 체계적으로 수집하고 정리하는 리서처입니다.
    항상 출처를 명확히 하고, 객관적 사실과 의견을 구분합니다.
  
writer:
  system: |
    수집된 정보를 바탕으로 읽기 쉬운 보고서를 작성합니다.
    항상 구조화되고 논리적인 흐름을 유지합니다.
```

### Extracted Code (python)

```python
import yaml
from agents.researcher import research
from agents.writer import write_report

def run_agent_workflow(topic):
    """에이전트 워크플로우 실행"""
    
    # 1. 리서치 단계
    print(f"📚 리서치 시작: {topic}")
    research_data = research(topic)
    
    # 2. 작성 단계
    print("✍️ 보고서 작성 중...")
    report = write_report(research_data)
    
    # 3. 결과 저장 (md 파일)
    with open(f"data/output/{topic}.md", "w") as f:
        f.write(report)
    
    print(f"✅ 완료: data/output/{topic}.md")

if __name__ == "__main__":
    run_agent_workflow("AI 에이전트 트렌드")
```

### Extracted Code (python)

```python
# qa/test_agent.py
import google.generativeai as genai

def test_output_quality(md_file_path):
    """생성된 md 파일의 품질 검증"""
    
    with open(md_file_path, 'r') as f:
        content = f.read()
    
    # Gemini로 품질 검증
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    qa_prompt = f"""
    다음 보고서를 검토하고 평가해주세요:
    
    {content}
    
    다음 기준으로 평가:
    1. 구조의 명확성 (1-10점)
    2. 정보의 정확성 (1-10점)
    3. 가독성 (1-10점)
    4. 개선 제안사항
    """
    
    response = model.generate_content(qa_prompt)
    return response.text
```

### Extracted Code (bash)

```bash
# 프로젝트 초기화
git init
git add .
git commit -m "Initial agent setup"

# 브랜치 전략 (간단하게)
git checkout -b feature/new-agent
# 작업...
git commit -m "Add researcher agent"
git checkout main
git merge feature/new-agent
```

### Extracted Code (markdown)

```markdown
# Agent Development Tasks

## 🚀 In Progress
- [ ] Researcher 에이전트 개발

## ✅ Completed
- [x] 기본 환경 설정
- [x] Gemini API 연결

## 💡 Backlog
- [ ] 이미지 분석 에이전트 추가
- [ ] 슬랙 알림 기능
```

### Extracted Code (bash)

```bash
# Claude Code 실행
claude-code

# 대화 예시
> "Python으로 뉴스 요약 에이전트를 만들고 싶어. 
   웹에서 특정 키워드 뉴스를 가져와서 Gemini로 요약하고, 
   결과를 md 파일로 저장해줘"

# Claude Code가 자동으로:
# 1. 필요한 패키지 제안 (requests, beautifulsoup4)
# 2. 코드 구조 생성
# 3. 실행 가능한 코드 작성
```

### Extracted Code (text)

```text
news-summarizer/
├── main.py              # Claude Code가 생성
├── requirements.txt     # Claude Code가 생성
├── config.yaml         # 설정 파일
└── outputs/            # 요약 결과들
    ├── tech-news.md
    └── business-news.md
```

### Extracted Code (markdown)

```markdown
### Day 1: 환경 구축
- [ ] VSCode 설치
- [ ] Claude Code 설치
- [ ] Gemini API 키 발급
- [ ] Python 환경 설정

### Day 2: 첫 에이전트
- [ ] "Hello Agent" 만들기
- [ ] Gemini 연결 테스트
- [ ] md 파일 출력 확인

### Day 3: 실전 적용
- [ ] 업무에 필요한 에이전트 아이디어 도출
- [ ] Claude Code와 대화하며 PRD 작성
- [ ] 30분 안에 프로토타입 완성

### Week 2: 확장
- [ ] Git으로 버전 관리
- [ ] QA 자동화 추가
- [ ] 두 번째 에이전트 추가
```
