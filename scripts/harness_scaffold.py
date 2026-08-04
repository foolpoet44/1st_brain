import os
import sys

def create_harness(project_name):
    """
    CSP Brain 표준 하네스 스캐폴딩 스크립트
    """
    base_path = f"/Users/dkmac/csp-brain/projects/{project_name}"
    
    if os.path.exists(base_path):
        print(f"⚠️ 이미 존재하는 프로젝트입니다: {base_path}")
        return

    subdirs = ["inbox", "wiki", "outputs", "skills", "archive"]
    
    try:
        # 폴더 생성
        os.makedirs(base_path, exist_ok=True)
        for sd in subdirs:
            os.makedirs(os.path.join(base_path, sd), exist_ok=True)
            
        # 기본 AGENTS.md 작성
        agents_md = f"""# {project_name} Agent Harness
- Created: {os.popen('date +%Y-%m-%d').read().strip()}
- Goal: HR Domain Expert Workstream for {project_name}
- Principles: Do it once, automate it forever.

## Shared Context
- Parent Brain: [[csp-brain-system]]
- Core Skills: [[context-restore]], [[memory-save]]

## Roles
- Lead: Context Orchestrator
- Researcher: Data Ingestion & Graph Mapping
- Analyst: Insight Extraction
"""
        with open(os.path.join(base_path, "AGENTS.md"), "w", encoding="utf-8") as f:
            f.write(agents_md)
            
        print(f"🚀 프로젝트 '{project_name}' 하네스 구축 완료!")
        print(f"Path: {base_path}")
        
    except Exception as e:
        print(f"❌ 오류 발생: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        create_harness(sys.argv[1])
    else:
        print("Usage: python harness_scaffold.py [project_name]")
