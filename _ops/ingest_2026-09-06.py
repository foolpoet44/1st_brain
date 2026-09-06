#!/usr/bin/env python3
"""
INGEST 프로토콜 실행 스크립트 — 2026-09-06
3 개 브리핑을 wiki 문서에 MERGE (중복 병합)
"""

import os
import re
from datetime import datetime

vault_path = "/Users/dkmac/csp-brain"

# ============================================================
# MERGE 2 & 3: IO-PSYCH 09-04 and 09-06 → 2026-07-22-autonomous-hiring-paradox.md
# ============================================================

hiring_paradox_path = os.path.join(vault_path, "wiki", "signals", "2026-07-22-autonomous-hiring-paradox.md")
io_psych_09_04_path = os.path.join(vault_path, "outputs", "briefings", "BRIEFING_IO-PSYCH_2026-09-04.md")
io_psych_09_06_path = os.path.join(vault_path, "outputs", "briefings", "BRIEFING_IO-PSYCH_2026-09-06.md")

with open(hiring_paradox_path, 'r', encoding='utf-8') as f:
    hiring_content = f.read()

with open(io_psych_09_04_path, 'r', encoding='utf-8') as f:
    io_09_04_content = f.read()

with open(io_psych_09_06_path, 'r', encoding='utf-8') as f:
    io_09_06_content = f.read()

# Find the --- separator at end of file
separator_idx = hiring_content.rfind('\n---\n')

# Prepare Timeline entry for IO-PSYCH 09-04
timeline_entry_09_04 = """
### 2026-09-04 — I/O 심리학 브리핑 INGEST

`outputs/briefings/BRIEFING_IO-PSYCH_2026-09-04.md` 를 편입했다. **MERGE 판정 이유**는 핵심 통계 (30%, 27 개월, 24 명) 가 기존 신뢰 사다리 통계와 일치하지만, **395% 효율성, 449 명 PsyCap 연구**는 새로운 신호이기 때문이다.

**브리핑이 새로 더한 것**:
1. **Human+AI 하이브리드 채용의 역설** (FAccT '26): 27 개월 Jobindex 데이터 (58,765 개 직무, 1,348,916 명 지원자). Human 0.813 vs AI 0.699 vs **Human+AI 0.854** (p<0.05). Post-AI Oversight 시 **CDP 0.876** (최고 공정성).
2. **AI 는 자원이다, 단 오류관리문화가 있을 때** (Frontiers '26): N=449 (제조 33.2%, IT 25.4%, 교육 18.0%). AI 도입 → 심리자본 (PsyCap) β=0.129 (p<0.001), 심리자본 → 혁신적 업무 행동 (IWB) β=1.104 (p<0.001). **오류관리문화 조절효과**: 고오류관리문화에서 AI→PsyCap 유의 (β=0.119), 저오류관리문화에서 무의미 (β=-0.011).
3. **알고리즘 투명성 → 절차적 공정성 → 조직 몰입** (American Impact Review '26): HR 전문가 523 명, 184 개 조직. 알고리즘 투명성 → 절차적 공정성 β=0.47 (p<0.001), 절차적 공정성 → 조직 몰입 β=0.38 (p<0.001).
4. **에이전트 네이티브 조직의 효율성** (arXiv '26): 8,000 개 합성 지식노동 태스크 시뮬레이션. 에이전트 네이티브 형태가 인간 모방 형태보다 **395.26% 더 효율적**. CTC(Contextual Transaction Cost) 인식이 핵심.

**Human Gate 추출 (4 개)**:
1. **Human Gate #1: 하이브리드 채용 심의회** — AI 추천 후보를 인간이 먼저 검토한 후 수동 검색 병행 의무화 (분기별 CDP 0.85 이상 감사).
2. **Human Gate #2: 심리자본 모니터링 위원회** — AI 도입 조직은 분기별 PsyCap 측정 및 PEMC 진단 결과 공시 (저오류관리문화 시 AI 도입 유예).
3. **Human Gate #3: 알고리즘 투명성 위원회** — AI 채용 도구의 판단 근거 3 항목 공개 의무화, 거부 시 24 시간 내 인간 설명 제공 (분기별 투명성 점수 공시).
4. **Human Gate #4: 에이전트 조직 설계 심의회** — AI 에이전트 조직도는 인간 모방 구조 금지, CTC(Contextual Transaction Cost) 측정 및 분기별 감사.

**핵심 통찰**: "편향은 기술의 실패가 아니라 인간과 AI 의 상호작용 설계 실패다." + "AI 는 도구가 아니라 자원 (Resource) 이다. 단, 오류를 허용하는 조직문화가 있을 때만." + "투명성은 기술적 기능이 아니라 심리적 계약이다." + "AI 는 인간 조직도를 모방하지 않는다. AI 는 컨텍스트 아키텍처를 가진다."

**후속 확인**:
- 분기별 CDP 측정 및 Human Gate #1 실행 여부
- AI 도입 조직의 PEMC 진단 결과 공시 여부
- 알고리즘 투명성 점수 분기별 공시 여부
- 에이전트 조직도의 인간 모방 구조 금지 준수 여부

"""

# Prepare Timeline entry for IO-PSYCH 09-06
timeline_entry_09_06 = """
### 2026-09-06 — I/O 심리학 브리핑 INGEST

`outputs/briefings/BRIEFING_IO-PSYCH_2026-09-06.md` 를 편입했다. **MERGE 판정 이유**는 핵심 통계 (67%, 26%, 30%) 가 기존 신뢰 사다리 통계와 일치하지만, **bullshitness 0.39 점 증가, 52.2% vs 51.1% 맥락적 풍자**는 새로운 신호이기 때문이다.

**브리핑이 새로 더한 것**:
1. **bullshitness 와 AI 위임 욕구 상관관계** (arXiv:2606.12430v2): 202 명 근로자, 171 개 작업 task 분석. "bullshitness" 척도 (Cronbach's α=0.877) 개발. bullshitness 1 SD 증가 → AI 위임 욕구 **0.39 점 증가** (5 점 척도, β=0.39, p<.001).
2. **알고리즘 불안의 방향성** (Frontiers in Psychology 2026.02.17): Reddit 1,454 개 내러티브 분석. VADER(52.2% 긍정) vs BERT(51.1% 부정) — 맥락적 풍자 포착 실패. Fear-Sadness **67% 동시 발생**. Anger(4%) 는 "탐욕스러운 경영진" 향함.
3. **알고리즘 관리: 자원이냐 요구냐** (Frontiers in Psychology 2026.05.21): 중국 50 개 하이테크 기업 353 명. AIM → Perceived Fit(β=0.512) > Perceived Control(β=0.269). **자원 경로 (Fit) 가 요구 경로 (Control) 보다 2 배 강함**.
4. **심리적 자본의 완전 매개 효과** (Frontiers in Psychology 2026.05.08): 449 명 2 차 시점 조사. AI → PsyCap(β=0.129) → IWB(β=1.104), **완전 매개**. 오류 관리 문화 높을 때 AI→PsyCap **0.119(p<.001)**, 낮을 때 **-0.011(p>0.05)**.

**Human Gate 추출 (4 개)**:
1. **Human Gate #1: 일의 의미 감사위원회** — 분기별 task 의미도 측정 (5 점 척도), AI 위임 대상은 bullshitness 상위 30% 로 제한.
2. **Human Gate #2: 신뢰 벡터 공개 의무** — 분기별 "누구를 신뢰하는가" (기술/벤더/인간 HR) 투명성 보고서.
3. **Human Gate #3: 알고리즘 맞춤 검증 의무** — 24 시간 내 CDP 0.85 이상 인간 검증, 이하는 재학습.
4. **Human Gate #4: 오후 2 시 이후 최종 거부 금지** — 14:00 이후 AI 거부는 16:00 까지 인간 bias 검증 의무.

**핵심 통찰**: "AI 는 인간 조직을 모방하지 않는다. AI 는 AI 네이티브 조직을 가진다." + "신뢰는 스칼라가 아니라 벡터다 — 26% 신뢰는 AI 기술이 아닌 인간 HR 향해야 함." + "통제는 자원이 아니라 요구다 — 알고리즘이 '맞춤'을 주면 자원, '감시'를 주면 요구." + "실수는 자원이 된다 — 오류를 처벌하지 않는 문화에서만 AI 가 심리적 자본으로 전환."

**후속 확인**:
- 분기별 task 의미도 측정 및 bullshitness 상위 30% AI 위임 준수 여부
- 신뢰 벡터 투명성 보고서 분기별 발간 여부
- CDP 0.85 미만 알고리즘 재학습 실행 여부
- 14:00 이후 AI 거부 시 16:00 까지 인간 bias 검증 수행 여부

"""

# Insert both entries before the final --- separator
if separator_idx != -1:
    new_content = hiring_content[:separator_idx] + timeline_entry_09_04 + timeline_entry_09_06 + hiring_content[separator_idx:]
else:
    new_content = hiring_content + "\n" + timeline_entry_09_04 + timeline_entry_09_06

# Update frontmatter updated date
new_content = re.sub(r'^(updated:).*$', r'\1 2026-09-06', new_content, flags=re.MULTILINE)

# Write back
with open(hiring_paradox_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("MERGE 완료: IO-PSYCH 09-04, 09-06 → 2026-07-22-autonomous-hiring-paradox.md")

# Mark both briefings as processed
for briefing_path, briefing_content in [(io_psych_09_04_path, io_09_04_content), (io_psych_09_06_path, io_09_06_content)]:
    fm = re.match(r'^---\n(.*?)\n---', briefing_content, re.DOTALL)
    if fm:
        fm_lines = fm.group(1).split('\n')
        new_fm_lines = []
        has_processed = False
        for line in fm_lines:
            new_fm_lines.append(line)
            if line.startswith('status:'):
                new_fm_lines.append('processed: true')
                new_fm_lines.append('processed_date: 2026-09-06')
                new_fm_lines.append('processed_note: MERGE → 2026-07-22-autonomous-hiring-paradox.md')
                has_processed = True
        
        if not has_processed:
            new_fm_lines.append('processed: true')
            new_fm_lines.append('processed_date: 2026-09-06')
            new_fm_lines.append('processed_note: MERGE → 2026-07-22-autonomous-hiring-paradox.md')
        
        new_fm = '\n'.join(new_fm_lines)
        new_briefing_content = re.sub(r'^---\n.*?\n---', '---\n' + new_fm + '\n---', briefing_content, flags=re.DOTALL)
        
        with open(briefing_path, 'w', encoding='utf-8') as f:
            f.write(new_briefing_content)
        
        print(f"마킹 완료: {briefing_path}")

print("\n✅ 모든 MERGE 작업 완료")
