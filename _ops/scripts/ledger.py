#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ledger.py — 이중구조 결손 명단(점수 D)과 미해소 원장(침묵)을 재산출하는 저장된 측정 도구.

왜 이 파일이 있는가 (2026-11-19 신설)
--------------------------------------
2026-11-16 부터 매 저녁 성찰이 "기계로 재산출했다"고 적어 왔다. 그런데 그 기계는
저장되지 않았다. 결과(표)만 `_ops/*.md` 에 남고, 그 표를 만든 정의 — 모집단 범위,
인용을 세는 자리, 항목별 검색어 — 는 매일 밤 세션 안에서 새로 태어나 사라졌다.
그래서 같은 줄("머리말 인용")이 7 · 8 · 10 세 값으로 산출됐다. 숫자가 흔들린 것이
아니라 정의가 흔들렸다.

`wiki/concepts/agent-friendly-redesign.md` 가 2026-04-29 에 적어 둔 원칙이 이것이다.
에이전트에게 필요한 것은 보기 좋은 표가 아니라 **상태 명세**이고, 정합성이 중요한
구간은 추론이 아니라 **코드 수준에서 결정론적으로** 검증해야 한다. 이 파일은 그
원칙의 첫 집행물이다.

사용법:  python3 _ops/scripts/ledger.py [--date YYYY-MM-DD]
출력:    표준출력에 마크다운 표 2종 (큐 · 침묵). 파일을 직접 고치지 않는다.
"""
import os, re, sys, glob, json, datetime, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ── 정의 1: 모집단 ─────────────────────────────────────────────────────────
# 위키 모집단 = wiki/ 아래 .md 전부에서 자동 생성 목차(_index.md)를 뺀 것.
WIKI_GLOB = 'wiki/**/*.md'
EXCLUDE_BASENAMES = {'_index.md'}
# 성찰 모집단 = outputs/daily-reflect/REFLECT_*.md 의 본문·부록 전체.
# 원장 자신(_ops/open-items.md)과 변경 기록(_ops/change-log.md)은 제외한다.
# 자기가 쓴 점호를 생존 증거로 쓰지 않기 위함 (2026-11-18 결정).
REFLECT_GLOB = 'outputs/daily-reflect/REFLECT_*.md'

# ── 정의 2: 인용을 세는 자리 ───────────────────────────────────────────────
# 지식 인용으로 세는 것은 **wiki/ 안에서** 온 링크뿐이다.
#   body   = 위키 문서 산문 안의 링크 (머리말·집행 구간 밖)
#   fmlink = 위키 문서 머리말(frontmatter) 안의 링크
#   execd  = 본 성찰 계열이 신설한 '## Compiled Truth' · '## Timeline' 구간 안의 링크
# 점수 D 는 execd 를 세지 않는다. 측정의 결과가 다음 측정의 입력이 되는 것을 막기 위함.
EXEC_HEADINGS = {'## Compiled Truth', '## Timeline'}

# ── 정의 3: 미해소 항목과 검색어 ───────────────────────────────────────────
# 항목은 지우지 않는다. 해소되면 status 만 바꾼다. 나이는 최초 진단일에서 센다.
# 검색어를 고치면 그날 성찰 부록에 변경 사실을 적는다. 말없이 고치지 않는다.
ITEMS = [
 (1,  'ROI 지표 4종의 측정 주기·주체',              '2026-06-23', r'ROI 지표|ROI.{0,6}4종|agentic-roi'),
 (2,  'opq-framework 가중치 공개·엔진 구현 주체',    '2026-07-18', r'opq-framework|OPQ 가중치|가중치 공개'),
 (3,  '고립 문서 수(orphans 18)의 재현 불가',        '2026-08-07', r'고립 문서|orphans|고립 18'),
 (4,  '종결 선언 16편의 위키 모집단 제외 여부',      '2026-08-08', r'종결 선언|종결선언'),
 (5,  '계기판이 과거 기록을 하루치만 받는 설정',     '2026-08-22', r'하루치만|얕은 복제|깊이 1'),
 (6,  '주간 다이제스트의 자기 기여 분리 여부',       '2026-08-29', r'주간 다이제스트'),
 (7,  '별칭·목차·경로형 링크를 인용으로 셀 것인가',  '2026-08-31', r'별칭|경로형 링크|자동 생성 목차'),
 (8,  '계기판 구조 점수에 이중구조 항 추가 여부',    '2026-10-11', r'구조 점수|산식에 반영|산식 반영'),
 (9,  '결근 칸을 건강 점수 산식에 넣을 것인가',      '2026-10-14', r'결근|출근부'),
 (10, '드라이브 일일 수집(Protocol 1-b) 재가동 여부','2026-10-14', r'드라이브 수집|드라이브 일일|gdrive|입구 수집'),
 (11, '추세 기록장의 표시 창(60줄) 확대 여부',       '2026-10-22', r'60줄|표시 창|추세 기록장'),
 (12, 'ai-offloading-risk 태그 반영 여부',           '2026-11-08', r'ai-offloading-risk|오프로딩'),
 (13, '⚠️ 메모 2건의 원문 확인 역할 배정',           '2026-11-10', r'메모 2건|원문 확인 역할'),
 (14, '저녁 성찰이 멈춘 날의 통보 경로',             '2026-11-14', r'멈춘 날|통보 경로|결근 통보'),
 (15, '요약 문서의 임계값 수치·측정 절차 부재',      '2026-11-14', r'임계값 수치|측정 절차 부재|임계값과 측정'),
 (16, '요약·기록 둘 다 결손 문서의 집행',            '2026-11-15', r'결손|이중구조'),
 (17, '큐 순위 기준에 자기 인용이 섞여 있다',        '2026-11-16', r'자기 인용|점수 B'),
 (18, '입구 보류 2편의 편입 + 입구 지표의 뜻',       '2026-11-17', r'관찰 전용|입구 보류|observed_only'),
 (19, '집행자가 그린 지식 인용을 순위에서 분리',     '2026-11-17', r'집행분|집행자가 그린'),
 (20, '침묵 알림 임계값(몇 편 공백에서 통보)',       '2026-11-18', r'침묵 알림|알림 임계값|몇 편 공백'),
 (21, '예측 등록 시 측정 시점 명기(자율 규칙)',      '2026-11-18', r'측정 시점|집필 전 펄스|집필 후 펄스'),
 (22, '측정 도구를 저장소에 둘 것인가(이 파일)',     '2026-11-19', r'측정 도구|ledger\.py|저장된 도구'),
]
SILENT_THRESHOLD = 2  # 공백 N편 이상이면 '침묵'. 사람 통보 기준은 미정(항목 ⑳).


def read(p):
    return open(p, encoding='utf-8', errors='replace').read()


def split_frontmatter(s):
    if s.startswith('---'):
        e = s.find('\n---', 3)
        if e > 0:
            return s[:e], s[e:]
    return '', s


def wiki_files():
    out = []
    for p in glob.glob(os.path.join(ROOT, WIKI_GLOB), recursive=True):
        if os.path.basename(p) in EXCLUDE_BASENAMES:
            continue
        out.append(p)
    return sorted(out)


def exec_zones(body):
    """'## Compiled Truth' · '## Timeline' 구간의 (시작, 끝) 바이트 오프셋."""
    zones, start, pos = [], None, 0
    for ln in body.splitlines(True):
        if ln.startswith('## '):
            if start is not None:
                zones.append((start, pos)); start = None
            if ln.strip() in EXEC_HEADINGS:
                start = pos
        pos += len(ln)
    if start is not None:
        zones.append((start, pos))
    return zones


def queue(today):
    files = wiki_files()
    deficient = []
    for p in files:
        s = read(p)
        fmt, body = split_frontmatter(s)
        if re.search(r'^processed:\s*true', fmt, re.M):
            continue
        if '## Compiled Truth' in s and '## Timeline' in s:
            continue
        upd = re.search(r'^updated:\s*(\S+)', fmt, re.M)
        deficient.append((p, upd.group(1).strip('"\'') if upd else ''))
    stems = {os.path.splitext(os.path.basename(p))[0] for p, _ in deficient}
    cnt = {t: {'body': 0, 'fmlink': 0, 'execd': 0} for t in stems}
    for p in files:
        fmt, body = split_frontmatter(read(p))
        zones = exec_zones(body)
        for m in re.finditer(r'\[\[([^\]\|#]+)', body):
            t = os.path.splitext(os.path.basename(m.group(1).strip()))[0]
            if t not in cnt:
                continue
            off = m.start()
            cnt[t]['execd' if any(a <= off < b for a, b in zones) else 'body'] += 1
        for m in re.finditer(r'\[\[([^\]\|#]+)', fmt):
            t = os.path.splitext(os.path.basename(m.group(1).strip()))[0]
            if t in cnt:
                cnt[t]['fmlink'] += 1
    rows = []
    for p, u in deficient:
        stem = os.path.splitext(os.path.basename(p))[0]
        c = cnt[stem]
        try:
            age = (today - datetime.date.fromisoformat(u[:10])).days
        except Exception:
            age = None
        d = age * (1 + c['body'] + c['fmlink']) if age is not None else -1
        b = age * (1 + c['body'] + c['fmlink'] + c['execd']) if age is not None else -1
        rows.append(dict(path=os.path.relpath(p, ROOT), updated=u or '—', age=age,
                         body=c['body'], fmlink=c['fmlink'], execd=c['execd'], D=d, B=b))
    rows.sort(key=lambda r: (-r['D'], r['path']))
    return rows


def silence(today):
    # 같은 날짜의 본편·보충편(_EVENING 등 접미사 9편)은 한 편으로 묶는다.
    # 계기판의 reflect_presence() 와 같은 정의를 쓴다. 편수 세는 법이 둘이면
    # '공백 2편'이 서로 다른 날짜 폭을 가리킨다.
    #
    # 2026-11-22 수정 — 기준일이 공백 칸을 지배하지 않았다.
    #   이전 동작: --date 는 '나이' 칸만 바꾸고, '공백'은 디스크의 현재 파일 전부로 셌다.
    #   그래서 --date 로 과거를 지정해도 산출값은 언제나 '지금'이었고, 과거에 기록된
    #   '기준일 D 침묵 N 건'은 어떤 인자로도 재현되지 않았다(실측: 2026-11-21 기록값 5건,
    #   같은 인자 재실행 7건). 기준일 이후 성찰을 모집단에서 제외해 D 시점을 재현한다.
    #   모집단의 마지막 날짜를 함께 반환해, 라벨이 측정 기간과 어긋나면 드러나게 한다.
    files = sorted(glob.glob(os.path.join(ROOT, REFLECT_GLOB)))
    byday = {}
    for f in files:
        m = re.match(r'REFLECT_(\d{4}-\d{2}-\d{2})(?:_.+)?\.md$', os.path.basename(f))
        if not m:
            continue
        if m.group(1) > today.isoformat():   # 기준일 이후는 보지 않는다
            continue
        byday.setdefault(m.group(1), []).append(read(f))
    texts = [(d, '\n'.join(v)) for d, v in sorted(byday.items())]
    out = []
    for n, name, born, pat in ITEMS:
        rx = re.compile(pat)
        last = None
        for d, t in texts:
            if rx.search(t):
                last = d
        # 검색어가 한 번도 맞지 않으면 공백을 0 으로 적지 않는다.
        # 0 은 '최근에 말했다'는 뜻이고, 미적중은 '잴 수 없다'는 뜻이다. 둘은 다르다.
        if last is None:
            out.append(dict(n=n, name=name, born=born,
                            age=(today - datetime.date.fromisoformat(born)).days,
                            last='—', gap=None, silent=False, unmeasured=True))
            continue
        gap = sum(1 for d, _ in texts if d > last)
        out.append(dict(n=n, name=name, born=born,
                        age=(today - datetime.date.fromisoformat(born)).days,
                        last=last, gap=gap, silent=gap >= SILENT_THRESHOLD, unmeasured=False))
    return out, len(texts), (texts[-1][0] if texts else '—')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--date', default=None)
    a = ap.parse_args()
    today = datetime.date.fromisoformat(a.date) if a.date else datetime.date.today()
    rows = queue(today)
    print(f'# 큐 — 결손 {len(rows)}편 (기준일 {today})\n')
    print('| # | 문서 | 마지막 갱신 | 미갱신일 | 본문 | 머리말 | 집행분 | 점수 D | 점수 B |')
    print('| --: | :-- | :-- | --: | --: | --: | --: | --: | --: |')
    for i, r in enumerate(rows, 1):
        age = r['age'] if r['age'] is not None else '—'
        D = r['D'] if r['D'] >= 0 else 0
        B = r['B'] if r['B'] >= 0 else 0
        print(f"| {i} | `{r['path']}` | {r['updated']} | {age} | {r['body']} | {r['fmlink']} | {r['execd']} | {D} | {B} |")
    tot = {k: sum(r[k] for r in rows) for k in ('body', 'fmlink', 'execd')}
    zero = sum(1 for r in rows if r['body'] + r['fmlink'] == 0)
    print(f"\n합계: 본문 {tot['body']} · 머리말 {tot['fmlink']} · 집행분 {tot['execd']} · 지식 인용 0편 {zero}/{len(rows)}")
    items, nref, lastday = silence(today)
    print(f'\n# 침묵 — 성찰 {nref}편 기준 (기준일 {today} · 모집단 마지막 날짜 {lastday})\n')
    print('| # | 항목 | 최초 진단 | 나이 | 최종 언급 | 공백 |')
    print('| --: | :-- | :-- | --: | :-- | --: |')
    for it in items:
        g = '— 검색어 미적중' if it['unmeasured'] else (f"**{it['gap']}**" if it['silent'] else str(it['gap']))
        print(f"| {it['n']} | {it['name']} | {it['born']} | {it['age']}일 | {it['last']} | {g} |")
    print(f"\n침묵({SILENT_THRESHOLD}편 이상): {sum(1 for i in items if i['silent'])}건 · "
          f"측정 불가(검색어 미적중): {sum(1 for i in items if i['unmeasured'])}건")


if __name__ == '__main__':
    main()
