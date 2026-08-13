#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INGEST 프로토콜 수행 스크립트 (2026-08-13)
- outputs/briefings/ 의 미처리 브리핑 6 건을 wiki/ 에 편입
- 중복 대조 후 MERGE 위주 처리 (양적 성장 ≠ 건강)
"""

import os
import re
from datetime import datetime

# Vault 경로
VAULT = "/Users/dkmac/csp-brain"

# 미처리 브리핑 파일 목록
BRIEFINGS = [
    ("outputs/briefings/BRIEFING_HR-TECH_2026-08-10.md", "HR-TECH", "2026-07-22-autonomous-hiring-paradox.md"),
    ("outputs/briefings/BRIEFING_HR-TECH_2026-08-11.md", "HR-TECH", "2026-07-22-autonomous-hiring-paradox.md"),
    ("outputs/briefings/BRIEFING_HR-TECH_2026-08-12.md", "HR-TECH", "2026-07-22-autonomous-hiring-paradox.md"),
    ("outputs/briefings/BRIEFING_IO-PSYCH_2026-08-11.md", "IO-PSYCH", "2026-07-22-autonomous-hiring-paradox.md"),
    ("outputs/briefings/BRIEFING_MONEY-FLOW_2026-08-11.md", "MONEY-FLOW", "2026-08-10-capital-flow-market-neutral.md"),
    ("outputs/briefings/BRIEFING_MONEY-FLOW_2026-08-12.md", "MONEY-FLOW", "2026-08-10-capital-flow-market-neutral.md"),
]

# 대상 wiki 문서
TARGETS = {
    "2026-07-22-autonomous-hiring-paradox.md": os.path.join(VAULT, "wiki/signals/2026-07-22-autonomous-hiring-paradox.md"),
    "2026-08-10-capital-flow-market-neutral.md": os.path.join(VAULT, "wiki/signals/2026-08-10-capital-flow-market-neutral.md"),
}

def read_frontmatter(filepath):
    """frontmatter 파싱"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        fm_text = match.group(1)
        fm = {}
        for line in fm_text.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                fm[key.strip()] = val.strip()
        return fm, content
    return {}, content

def extract_key_stats(content, domain):
    """브리핑에서 핵심 통계 추출"""
    stats = []
    
    # 통계 패턴: **통계**: 또는 **통계**: 형태
    stat_matches = re.findall(r'\*\*통계\*\*:\s*(.+?)(?=\n|$)', content)
    for stat in stat_matches[:4]:  # 최대 4 개
        stats.append(stat.strip())
    
    # 핵심 통찰도 추출
    insights = re.findall(r'\*\*핵심 통찰\*\*:\s*\*\*"(.+?)"\*\*', content)
    
    return stats, insights

def create_timeline_entry(briefing_path, domain, stats, insights):
    """Timeline 엔트리 생성"""
    date = datetime.now().strftime("%Y-%m-%d")
    
    # 브리핑 제목 추출
    fm, _ = read_frontmatter(briefing_path)
    title = fm.get('title', 'Unknown Briefing')
    
    entry = f"### {date} — {domain} 브리핑 INGEST\n\n"
    entry += f"`{briefing_path}` 를 편입했다. **신규 문서를 만들지 않고 기존 문서에 병합한 이유**는, 브리핑의 핵심 통계와 통찰이 기존 문서와 중복되기 때문이다.\n\n"
    entry += "브리핑이 **새로 더한 것**은 다음이다.\n\n"
    
    # 통계 요약
    if stats:
        entry += "1. **핵심 통계**:\n"
        for i, stat in enumerate(stats[:3], 1):
            entry += f"   - {stat}\n"
        entry += "\n"
    
    # 통찰 요약
    if insights:
        entry += "2. **핵심 통찰**:\n"
        for i, insight in enumerate(insights[:2], 1):
            entry += f"   - {insight}\n"
        entry += "\n"
    
    entry += "**후속 확인**: 해당 통계와 통찰이 다음 브리핑에서 재확인되면 별도 신호로 승격을 검토한다.\n\n"
    
    return entry

def append_to_timeline(target_path, entry):
    """기존 문서의 Timeline 에 엔트리 추가"""
    with open(target_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Timeline 섹션 찾기
    timeline_match = re.search(r'\n## Timeline\n', content)
    if not timeline_match:
        print(f"  ERROR: Timeline 섹션을 찾을 수 없음: {target_path}")
        return False
    
    # Timeline 직전까지의 내용
    timeline_start = timeline_match.start()
    before_timeline = content[:timeline_start + len('\n## Timeline\n')]
    after_timeline = content[timeline_start + len('\n## Timeline\n'):]
    
    # 엔트리 추가 (Timeline 헤더 바로 다음에)
    new_content = before_timeline + entry + after_timeline
    
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def mark_processed(briefing_path):
    """브리핑 파일에 processed 마킹"""
    fm, content = read_frontmatter(briefing_path)
    
    # processed 필드 추가
    fm['processed'] = 'true'
    fm['processed_date'] = datetime.now().strftime("%Y-%m-%d")
    fm['processed_note'] = f"INGEST 프로토콜 수행 — MERGE 판정 (기존 문서에 병합)"
    
    # frontmatter 재구성
    fm_lines = []
    for key, val in fm.items():
        fm_lines.append(f"{key}: {val}")
    
    new_fm = "---\n" + "\n".join(fm_lines) + "\n---\n"
    
    # 본문만 추출 (기존 frontmatter 제거)
    body_match = re.match(r'^---\n.*?\n---\n(.*)', content, re.DOTALL)
    body = body_match.group(1) if body_match else content
    
    new_content = new_fm + body
    
    with open(briefing_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def update_ingest_log(new_count, merge_count, dup_count):
    """ingest-log.md 업데이트"""
    log_path = os.path.join(VAULT, "_ops/ingest-log.md")
    
    today = datetime.now().strftime("%Y-%m-%d")
    entry = f"""## {today} — INGEST 프로토콜 수행 (아침 브리핑 6 건)

**집계**:
- **신규 (NEW)**: {new_count} 건
- **병합 (MERGE)**: {merge_count} 건
- **중복 종결 (DUPLICATE)**: {dup_count} 건

**판정 근거**:
- **HR-TECH 3 건** (08-10, 08-11, 08-12): 2026-07-22-autonomous-hiring-paradox.md 에 병합
  - 이유: 52% 에이전트 도입, 26% 편향, Eightfold FCRA, 70% vs 8% 신뢰 격차 — 모두 기존 문서에 있음
- **IO-PSYCH 1 건** (08-11): 2026-07-22-autonomous-hiring-paradox.md 에 병합
  - 이유: arXiv:2603.14963 (의미 보호 구역), arXiv:2605.28680 (Decency vs Meaningfulness) — HR 실행 함의 중복
- **MONEY-FLOW 2 건** (08-11, 08-12): 2026-08-10-capital-flow-market-neutral.md 에 병합
  - 이유: Fed 금리, 환율 1460 원, 5:5 자산배분 — 자본시장 신호 중복

**인용된 Human Gate**:
- Human Gate #1-4: 에이전트 조직 설계, DEI 벤더 심사, 의미 보호 구역, 도메인별 AI 영향 평가 (IO-PSYCH)
- Human Gate #1-4: 편향 감사, 법적 리스크 모니터링, 후보자 경험 심의회, 진화 게이트 (HR-TECH)
- Human Gate #1-3: Fed 금리 감시, 환율 임계치, 자산배분 심의 (MONEY-FLOW)

**후속 작업**:
- [ ] 2026-07-22-autonomous-hiring-paradox.md 의 Timeline 에 4 건 브리핑 내용 추가
- [ ] 2026-08-10-capital-flow-market-neutral.md 의 Timeline 에 2 건 브리핑 내용 추가
- [ ] _ops/change-log.md 에 [INGEST] 엔트리 추가
- [ ] wiki/signals/_index.md 에 링크 존재 확인

---

"""
    
    with open(log_path, 'r', encoding='utf-8') as f:
        log_content = f.read()
    
    # 맨 앞에 추가 (after frontmatter)
    fm_match = re.match(r'^(---\n.*?\n---\n)', log_content, re.DOTALL)
    if fm_match:
        new_log = fm_match.group(1) + "\n" + entry + log_content[len(fm_match.group(1)):]
    else:
        new_log = entry + log_content
    
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(new_log)
    
    return True

def main():
    print("=" * 60)
    print("INGEST 프로토콜 수행 (2026-08-13)")
    print("=" * 60)
    
    new_count = 0
    merge_count = 0
    dup_count = 0
    
    for briefing_rel, domain, target_rel in BRIEFINGS:
        briefing_path = os.path.join(VAULT, briefing_rel)
        target_path = TARGETS[target_rel]
        
        print(f"\n처리: {briefing_rel}")
        print(f"  도메인: {domain}")
        print(f"  대상: {target_rel}")
        
        # 브리핑 읽기
        fm, content = read_frontmatter(briefing_path)
        stats, insights = extract_key_stats(content, domain)
        
        print(f"  추출된 통계: {len(stats)}개")
        print(f"  추출된 통찰: {len(insights)}개")
        
        # Timeline 엔트리 생성
        entry = create_timeline_entry(briefing_rel, domain, stats, insights)
        
        # 기존 문서에 추가
        if append_to_timeline(target_path, entry):
            print(f"  → 병합 완료 (Timeline 에 추가)")
            merge_count += 1
        else:
            print(f"  → ERROR: 병합 실패")
            continue
        
        # processed 마킹
        mark_processed(briefing_path)
        print(f"  → processed 마킹 완료")
    
    # ingest-log 업데이트
    update_ingest_log(new_count, merge_count, dup_count)
    
    print("\n" + "=" * 60)
    print(f"처리 완료: 신규 {new_count}건, 병합 {merge_count}건, 중복 {dup_count}건")
    print("=" * 60)

if __name__ == "__main__":
    main()
