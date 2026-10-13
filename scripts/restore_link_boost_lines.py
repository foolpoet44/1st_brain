"""링크 부스팅 손상 복원 (줄 단위).
손상 커밋이 '바꾼' 줄 중 새 줄에 [[ 가 더 많아진 줄을 (손상 줄 → 원래 줄)로 짝지어 사전을 만들고,
현재 파일에서 손상 줄과 정확히 같은 줄만 원래 줄로 되돌린다. 이후의 정상 편집은 건드리지 않는다."""
import subprocess, sys, re, difflib, json, collections
ROOT = sys.argv[1]; WRITE = sys.argv[2] == 'write'; SKIP = set(sys.argv[3:])
COMMITS = ['fecec41', '82164c3', '7a51a3e', '694e697']
LINK = re.compile(r'\[\[([^\[\]|]+)\|([^\[\]]*)\]\]|\[\[([^\[\]|]+)\]\]')
def git(*a): return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True).stdout
def show(rev, f):
    r = subprocess.run(['git', '-C', ROOT, 'show', f'{rev}:{f}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None
def norm(s):
    prev = None
    while prev != s: prev, s = s, LINK.sub(lambda m: m.group(2) if m.group(2) is not None else m.group(3), s)
    return s.lower()
mapping = {}
for c in COMMITS:
    for f in git('diff-tree', '--no-commit-id', '--name-only', '-r', '-z', c).split('\0'):
        if not f or f.startswith(('Understand-Anything/', 'open-design/')): continue
        old, new = show(c + '^', f), show(c, f)
        if old is None or new is None: continue
        a, b = old.split('\n'), new.split('\n')
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if tag != 'replace': continue
            olds = a[i1:i2]
            if i2 - i1 == j2 - j1:
                for ol, nl in zip(olds, b[j1:j2]):
                    if nl.count('[[') > ol.count('[['):
                        mapping.setdefault(nl, ol)
            for nl in b[j1:j2]:
                hm = re.match(r'^(#+) \[\[[^\[\]]+\]\]\s*$', nl)
                if hm:
                    hs = [ol for ol in olds if ol.startswith(hm.group(1) + ' ') and '[[' not in ol]
                    if hs: mapping.setdefault(nl, hs[0]); continue
                if nl.count('[[') <= 0: continue
                best = max(olds, key=lambda ol: difflib.SequenceMatcher(None, norm(nl), ol.lower()).ratio())
                if best.count('[[') < nl.count('[[') and difflib.SequenceMatcher(None, norm(nl), best.lower()).ratio() > 0.6:
                    mapping.setdefault(nl, best)
def resolve(l):
    seen = set()
    while l in mapping and l not in seen: seen.add(l); l = mapping[l]
    return l
report = collections.Counter()
for f in git('ls-files', '-z').split('\0'):
    if not f or f in SKIP or f.startswith(('Understand-Anything/', 'open-design/')): continue
    try: s = open(f'{ROOT}/{f}', encoding='utf-8').read()
    except Exception: continue
    lines = s.split('\n'); n = 0
    for i, l in enumerate(lines):
        if l in mapping:
            r = resolve(l)
            if r != l: lines[i] = r; n += 1
    if n:
        report[f] = n
        if WRITE: open(f'{ROOT}/{f}', 'w', encoding='utf-8').write('\n'.join(lines))
print(json.dumps({'mapping': len(mapping), 'files': len(report), 'lines': sum(report.values())}))
