"""링크 부스팅(2026-07-27) 손상 복원.
부스터는 본문 속 문자열 X 를 [[<Understand-Anything|open-design 경로>/X.md|X]] 로 바꿨다.
그래서 '대상 경로가 두 디렉터리 안이고, 별칭이 파일 이름(확장자 제외)과 같은' 링크만
별칭 텍스트로 되돌린다. 안쪽(괄호 없는) 링크부터 반복해서 풀어 중첩을 해소한다."""
import re, sys, subprocess, json
PREFIX = ('Understand-Anything/', 'open-design/')
pat = re.compile(r'\[\[([^\[\]|]+)\|([^\[\]]*)\]\]')
def stem(t):
    b = t.strip().split('/')[-1].lstrip('…')
    return b[:-3] if b.endswith('.md') else b
def fix(s):
    n = 0
    while True:
        def rep(m):
            nonlocal n
            t, a = m.group(1), m.group(2)
            if t.strip().startswith(PREFIX) and a.strip() == stem(t):
                n += 1; return a.strip()
            return m.group(0)
        s2 = pat.sub(rep, s)
        if s2 == s: return s, n
        s = s2
def main(root, skip, write):
    files = subprocess.run(['git','-C',root,'ls-files','-z'],capture_output=True,text=True).stdout.split('\0')
    report = {}
    for f in files:
        if not f or f.startswith(PREFIX) or f in skip: continue
        p = f'{root}/{f}'
        try: s = open(p, encoding='utf-8').read()
        except Exception: continue
        if '[[' not in s: continue
        s2, n = fix(s)
        if n:
            report[f] = n
            if write: open(p, 'w', encoding='utf-8').write(s2)
    print(json.dumps({'files': len(report), 'links': sum(report.values())}, ensure_ascii=False))
    return report
if __name__ == '__main__':
    r = main(sys.argv[1], set(sys.argv[3:]), sys.argv[2] == 'write')
