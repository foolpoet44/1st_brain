import os
from datetime import datetime
from hermes_tools import read_file, write_file, session_search, send_message

def evening_reflect():
    today = datetime.now().strftime("%Y-%m-%d")
    vault_path = "/Users/dkmac/csp-brain"
    changelog_path = f"{vault_path}/_ops/change-log.md"
    output_dir = f"{vault_path}/outputs/daily-reflect"
    
    # 1. 오늘 작업 내용 수집
    changelog = read_file(changelog_path).get("content", "오늘의 작업 기록이 없습니다.")
    
    # 2. 최근 세션 요약 (핵심 맥락 파악)
    sessions = session_search(query="HR OR insight OR bridge", limit=3)
    
    # 3. 인공지능 성찰 (이 과정은 스크립트를 호출하는 에이전트의 몫이므로 여기서는 구조만 잡습니다)
    # 실제 성찰 로직은 에이전트가 이 스크립트 실행 후 그 결과를 바탕으로 작성합니다.
    
    print(f"--- Daily Context for {today} ---")
    print(changelog)
    print("\n--- Recent Sessions ---")
    print(sessions)

if __name__ == "__main__":
    evening_reflect()
