#!/usr/bin/env python3
"""지식 인덱스 데이터 생성기 (_data/knowledge.json).

Jekyll 발행 전에 실행한다. github-pages Jekyll 에는 git 수정시각을 읽는
플러그인이 없고 발행 문서의 ~75% 가 날짜 프론트매터를 갖고 있지 않으므로,
진짜 '최신 수정순'은 git 의 마지막 커밋 시각으로만 신뢰성 있게 잡을 수 있다.

git log 한 번을 훑어 파일별 마지막 커밋 ISO 날짜를 구하고, 발행 대상 지식
문서를 최신순으로 정렬해 _data/knowledge.json 으로 떨군다. knowledge.html 은
이 데이터를 폴더별로 묶어 렌더링한다.

전제: 워크플로 checkout 이 fetch-depth: 0 (전체 히스토리) 이어야 파일별
마지막 커밋 시각이 정확하다.
"""
import subprocess
import json
import os
import re
import fnmatch

# 발행 대상 지식 폴더 (전체 Vault + 루트 파일)
# raw/, inbox/ 는 미처리 자료이므로 제외
DIRS = [
    "",              # 루트 파일 (SOUL.md, AGENTS.md, README.md 등)
    "wiki",          # HR Tech 신호, 브리핑
    "concepts",      # 개념 원자
    "projects",      # 프로젝트
    "outputs",       # 브리핑, 성찰, 분석
    "people",        # 인물
    "decisions",     # 결정
    "weekly",        # 주간 리포트
    "research",      # 연구
    "signals",       # Signal 노드
    "vault",         # csp-brain Vault
    "synapses",      # Synapse 문서
    "protocols",     # 프로토콜
    "curricula",     # 커리큘럼
    "scripts",       # 스크립트
    "reports",       # 보고서
    "analysis",      # 분석
    "Atoms",         # Atom 개념
    "moc",           # MOC (Map of Content)
    "templates",     # 템플릿
    "references",    # 레퍼런스
    "Type",          # Type 정의
    "Toss",          # Toss 프로젝트
    "sync",          # 동기화 로그
    "1st_brain",     # 1st_brain 대시보드
    "csp-brain",     # csp-brain Vault
    "_ops",          # 운영 로그
]

EXCLUDE_GLOBS = [
    "concepts/extracted-*.md",
    "outputs/temp-*.md",
    "vault/attachments/*",
    "raw/*",          # 미처리 raw 자료 제외
    "inbox/*",        # 미처리 inbox 자료 제외
]

EXCLUDE_FILES = {
    "outputs/weekly/2026-W18.md",
    ".gitmodules",
}


def last_commit_dates():
    """파일별 마지막 커밋 ISO 날짜를 git log 한 번으로 수집."""
    out = subprocess.run(
        ["git", "log", "--name-only", "--format=@%cI", "--", *DIRS],
        capture_output=True, text=True,
    ).stdout
    mtime = {}
    cur = ""
    for line in out.splitlines():
        if line.startswith("@"):
            cur = line[1:]
        elif line.strip():
            f = line.strip()
            if f not in mtime:  # git log 는 최신순 → 첫 등장이 마지막 커밋
                mtime[f] = cur
    return mtime


def excluded(path):
    if path in EXCLUDE_FILES:
        return True
    return any(fnmatch.fnmatch(path, g) for g in EXCLUDE_GLOBS)


def title_of(path):
    try:
        txt = open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        return os.path.basename(path)
    m = re.search(r"^---\s*$(.*?)^---\s*$", txt, re.M | re.S)
    if m:
        t = re.search(r"^title:\s*(.+?)\s*$", m.group(1), re.M)
        if t:
            return t.group(1).strip().strip("\"'")
    h = re.search(r"^#\s+(.+)$", txt, re.M)
    if h:
        return h.group(1).strip()
    # 루트 파일은 H1 이 없으면 파일명을 제목으로
    return os.path.basename(path)[:-3] if path.endswith(".md") else os.path.basename(path)


def main():
    mtime = last_commit_dates()
    tracked = subprocess.run(
        ["git", "ls-files"], capture_output=True, text=True
    ).stdout.split()

    items = []
    for path in tracked:
        if not path.endswith(".md"):
            continue
        
        # raw/, inbox/ 제외
        if path.startswith("raw/") or path.startswith("inbox/"):
            continue
        
        if excluded(path) or not os.path.exists(path):
            continue
        
        # 첫 폴더명 추출 (루트 파일은 "")
        first_dir = path.split("/")[0] if "/" in path else ""
        
        items.append({
            "path": path,
            "url": "/" + path[:-3] + ".html",
            "title": title_of(path),
            "dir": first_dir if first_dir else "root",
            "date": mtime.get(path, "")[:10],
        })

    # 최신 수정순 (날짜 내림차순; 날짜 없는 문서는 뒤로)
    items.sort(key=lambda x: x["date"], reverse=True)

    os.makedirs("_data", exist_ok=True)
    with open("_data/knowledge.json", "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=1)
    print(f"knowledge index: {len(items)} docs -> _data/knowledge.json")


if __name__ == "__main__":
    main()
