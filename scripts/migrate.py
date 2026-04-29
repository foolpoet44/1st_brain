"""
manifest.json v2 마이그레이션 스크립트
- 기존 manifest.json 을 읽어서 새 스키마 (category, tags, md_path) 로 업데이트
- 마크다운 파일에서 내용 추출하여 자동 분류
"""
import json
import hashlib
from pathlib import Path
from datetime import datetime
from manifest_schema import auto_categorize, auto_extract_tags


def compute_hash(filepath: Path) -> str:
    """SHA256 해시 계산"""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            sha256.update(chunk)
    return sha256.hexdigest()


def migrate_manifest(manifest_path: str, vault_dir: Path):
    """manifest.json 을 v2 스키마로 마이그레이션"""

    # 기존 manifest.json 로드
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    print(f"[MIGRATE] 총 {len(manifest)} 개 엔트리 처리 중...")

    updated_count = 0

    for filepath, entry in manifest.items():
        # 이미 마이그레이션된 엔트리 스킵
        if 'category' in entry and entry.get('category') != 'Uncategorized':
            continue

        # md_path 계산
        filename = Path(filepath).stem + '.md'
        md_path = vault_dir / filename

        # 마크다운 파일이 존재하면 내용 읽기
        category = None
        tags = []
        word_count = None

        if md_path.exists():
            content = md_path.read_text(encoding='utf-8')[:5000]
            category = auto_categorize(filepath, content)
            tags = auto_extract_tags(filepath, content)
            word_count = len(content.split())
        else:
            # 마크다운 파일이 없으면 경로만으로 분류
            category = auto_categorize(filepath, "")
            tags = auto_extract_tags(filepath, "")

        # 엔트리 업데이트
        entry['category'] = category
        entry['tags'] = tags
        entry['md_path'] = str(md_path)
        entry['word_count'] = word_count
        entry['last_indexed'] = datetime.now().isoformat()

        updated_count += 1

        if updated_count % 50 == 0:
            print(f"  - {updated_count}/{len(manifest)} 처리 완료")

    # 업데이트된 manifest.json 저장
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=4)

    print(f"[MIGRATE] 완료: {updated_count}/{len(manifest)} 개 엔트리 업데이트")
    return manifest


if __name__ == "__main__":
    # 경로를 동적으로 계산
    BASE_DIR = Path(__file__).parent.parent
    MANIFEST_PATH = BASE_DIR / "manifest.json"

    # 마이그레이션 실행
    migrate_manifest(str(MANIFEST_PATH), BASE_DIR)

    # 인덱스 재생성
    print("\n[INFO] 인덱스 재생성 중...")
    import subprocess
    subprocess.run(["python", "indexer.py"])
