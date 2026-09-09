"""
수문 A — Google Drive 어댑터 (Drive Ingress)

목적: 볼트 밖에 고립된 '설계 명세서'(Drive의 Google Docs)를 볼트 inbox로 들여온다.
왜: Hermes는 볼트 *안*의 지식만 신진대사한다. 이 스크립트가 수원의 물을 길어 inbox에 부으면,
    그 다음은 기존 INGEST 파이프라인이 알아서 wiki로 편입한다. 즉 파이프라인의 '입구'만 뚫는다.

동작:
  1. rclone 으로 대상 Drive 폴더를 임시 폴더에 복사 (gdoc → md export).
  2. 파일별 콘텐츠 해시를 _ops/drive-manifest.json 과 대조 → 신규/변경분만 inbox/papers/ 에 저장.
  3. 저장 파일에 frontmatter 자동 부착 (source, original_path, pulled, processed:false).
  4. 결과를 _ops/drive-pull-log.md 에 append.

환경(헤드리스 Cloud Agent 전용 — GitHub Actions 에서 secret 으로 주입):
  RCLONE_CONFIG_GDRIVE_TYPE=drive
  RCLONE_CONFIG_GDRIVE_SCOPE=drive.readonly
  RCLONE_CONFIG_GDRIVE_SERVICE_ACCOUNT_FILE=<GDRIVE_SA_JSON 을 쓴 파일 경로>
  RCLONE_CONFIG_GDRIVE_ROOT_FOLDER_ID=<대상 Drive 폴더 ID>   # SA 이메일에 뷰어로 공유돼 있어야 함
  → rclone.conf 파일 없이 순수 env 로 동작 (CI 친화적).

사용:
  python drive_pull.py --self-check   # 순수 로직 검증(네트워크·rclone 불필요)
  python drive_pull.py --dry-run      # 무엇이 들어올지만 출력
  python drive_pull.py                # 실제 pull

표준 라이브러리 + subprocess(rclone) 만 사용. Windows/Linux 경로·한글 호환.
"""
import sys
import os
import re
import json
import hashlib
import subprocess
import tempfile
from datetime import date
from pathlib import Path

REMOTE = "gdrive:"                       # rclone env 로 정의되는 리모트 이름
EXPORT_FLAGS = ["--drive-export-formats", "md"]

VAULT = Path(__file__).resolve().parents[2]      # _ops/scripts/ → 볼트 루트
DEST = VAULT / "inbox" / "papers"
MANIFEST = VAULT / "_ops" / "drive-manifest.json"
LOG = VAULT / "_ops" / "drive-pull-log.md"


# ---- 순수 로직 (self-check 대상) -------------------------------------------

def content_hash(data: bytes) -> str:
    """콘텐츠 기반 해시. 같은 내용이면 같은 해시 → 재-pull 시 스킵 판정에 사용."""
    return hashlib.sha256(data).hexdigest()


def slugify(name: str) -> str:
    """상대경로 → 슬러그. 한글 보존. 경로구분자는 하이픈으로(폴더 간 충돌 방지),
    Windows 금지문자는 제거. rglob 이 넘기는 .md 확장자는 떼어낸다."""
    s = re.sub(r"\.md$", "", name)               # 확장자 제거
    s = re.sub(r"[\\/]", "-", s)                  # 경로구분자 → 하이픈(원경로 흔적 보존)
    s = re.sub(r'[:*?"<>|]', "", s)               # Windows 금지문자 제거
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s).strip("-")          # 하이픈 중복/양끝 정리
    return s or "untitled"


def make_frontmatter(original_path: str, pulled: str) -> str:
    """inbox 파일 머리에 붙일 YAML frontmatter. processed:false 로 INGEST 대기 표시."""
    # original_path 의 따옴표는 YAML 안전을 위해 제거
    safe = original_path.replace('"', "")
    return (
        "---\n"
        "source: gdrive\n"
        f'original_path: "{safe}"\n'
        f"pulled: {pulled}\n"
        "processed: false\n"
        "---\n\n"
    )


def diff_manifest(current: dict, previous: dict) -> tuple[list, list]:
    """(신규+변경 경로, 스킵 경로) 반환. current/previous 는 {original_path: hash}."""
    changed, skipped = [], []
    for path, h in current.items():
        if previous.get(path) == h:
            skipped.append(path)
        else:
            changed.append(path)
    return changed, skipped


# ---- I/O 계층 --------------------------------------------------------------

def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {}


def rclone_export(tmp: Path) -> None:
    """대상 Drive 폴더를 tmp 로 복사(gdoc→md). rclone 미설치/미인증 시 예외."""
    cmd = ["rclone", "copy", REMOTE, str(tmp), *EXPORT_FLAGS, "--transfers", "4"]
    subprocess.run(cmd, check=True)


def append_log(new_n: int, changed_n: int, skip_n: int, pulled: str) -> None:
    line = f"- {pulled}: 신규/변경 {changed_n}건 (그중 신규 파일 {new_n}), 스킵 {skip_n}건\n"
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line)


def run(dry_run: bool) -> int:
    pulled = date.today().isoformat()
    previous = load_manifest()

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        rclone_export(tmp)

        current, blobs = {}, {}
        for f in tmp.rglob("*.md"):
            rel = f.relative_to(tmp).as_posix()
            data = f.read_bytes()
            current[rel] = content_hash(data)
            blobs[rel] = data

        changed, skipped = diff_manifest(current, previous)

        if dry_run:
            print(f"[dry-run] 변경/신규 {len(changed)}건, 스킵 {len(skipped)}건")
            for p in changed:
                print(f"  + {p}  → inbox/papers/{slugify(p)}.md")
            return 0

        DEST.mkdir(parents=True, exist_ok=True)
        new_files = 0
        for rel in changed:
            out = DEST / f"{slugify(rel)}.md"
            if not out.exists():
                new_files += 1
            body = blobs[rel].decode("utf-8", errors="replace")
            out.write_text(make_frontmatter(rel, pulled) + body, encoding="utf-8")

    MANIFEST.write_text(json.dumps(current, ensure_ascii=False, indent=2), encoding="utf-8")
    append_log(new_files, len(changed), len(skipped), pulled)
    print(f"pull 완료: 변경/신규 {len(changed)}건, 스킵 {len(skipped)}건 → inbox/papers/")
    return 0


# ---- 자가 검증 (ponytail: 순수 로직만, rclone/네트워크 불필요) --------------

def self_check() -> int:
    # 해시: 같은 내용 → 같은 해시, 다른 내용 → 다른 해시
    assert content_hash(b"abc") == content_hash(b"abc")
    assert content_hash(b"abc") != content_hash(b"abd")

    # 슬러그: 한글 보존, 경로구분자→하이픈, 금지문자 제거, 공백→하이픈
    assert slugify("설계 명세서: OKA/v2.md") == "설계-명세서-OKA-v2"
    assert slugify("papers/논문.md") == "papers-논문"
    assert slugify("   ") == "untitled"

    # frontmatter: 필수 키 + 따옴표 안전
    fm = make_frontmatter('a/b "x".md', "2026-07-17")
    assert "source: gdrive" in fm and "processed: false" in fm
    assert '"x"' not in fm  # 따옴표 제거됨

    # diff: 동일 해시는 skip, 변경/신규는 changed
    prev = {"a.md": "h1", "b.md": "h2"}
    cur = {"a.md": "h1", "b.md": "hX", "c.md": "h3"}   # a 동일, b 변경, c 신규
    changed, skipped = diff_manifest(cur, prev)
    assert set(changed) == {"b.md", "c.md"} and skipped == ["a.md"]

    print("self-check OK")
    return 0


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    args = set(sys.argv[1:])
    if "--self-check" in args:
        return self_check()
    return run(dry_run="--dry-run" in args)


if __name__ == "__main__":
    raise SystemExit(main())
