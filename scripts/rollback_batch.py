#!/usr/bin/env python3
"""
Evolution Gate Rollback Script

csp-brain Vault 에서 특정 배치 (batch) 의 분류 결과를 일괄 롤백한다.
audit_log 를 파싱하여 해당 batch_id 를 가진 모든 문서의 type 필드를 제거한다.

사용법:
    python scripts/rollback_batch.py --batch-id batch_2026-07-27_001

출력:
    - 롤백된 문서 목록
    - rollback_audit.json 에 이력 기록
"""

import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime

# Vault 루트 경로 (스크립트 위치 기준 2 단계 상위)
VAULT_ROOT = Path(__file__).parent.parent
AUDIT_LOG_DIR = VAULT_ROOT / "audit_logs"


def load_audit_log():
    """가장 최근의 audit_log 파일을 로드한다."""
    if not AUDIT_LOG_DIR.exists():
        print(f"❌ Audit log directory not found: {AUDIT_LOG_DIR}")
        sys.exit(1)
    
    # 가장 최근 audit_log 파일 찾기
    audit_files = sorted(AUDIT_LOG_DIR.glob("classification_*.json"))
    if not audit_files:
        print("❌ No audit log files found.")
        sys.exit(1)
    
    latest_log = audit_files[-1]
    with open(latest_log, "r", encoding="utf-8") as f:
        return json.load(f), latest_log


def find_batch_records(audit_data, batch_id):
    """audit_log 에서 특정 batch_id 를 가진 모든 레코드를 찾는다."""
    records = []
    for entry in audit_data:
        if entry.get("batch_id") == batch_id:
            records.append(entry)
    return records


def rollback_document(doc_path, original_type):
    """문서의 type 필드를 제거한다. (frontmatter 에서)"""
    full_path = VAULT_ROOT / doc_path
    if not full_path.exists():
        return False, f"File not found: {doc_path}"
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # frontmatter 파싱 (간단한 YAML 파싱)
    if not content.startswith("---"):
        return False, f"No frontmatter: {doc_path}"
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return False, f"Invalid frontmatter: {doc_path}"
    
    frontmatter_str = parts[1]
    body = parts[2]
    
    # type: 라인 제거
    lines = frontmatter_str.split("\n")
    new_lines = []
    type_removed = False
    for line in lines:
        if line.strip().startswith("type:") and not type_removed:
            type_removed = True
            continue
        new_lines.append(line)
    
    if not type_removed:
        return False, f"No type field found: {doc_path}"
    
    # 새 content 조립
    new_frontmatter = "\n".join(new_lines)
    new_content = f"---{new_frontmatter}---{body}"
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    return True, f"Rolled back: {doc_path} (was {original_type})"


def main():
    parser = argparse.ArgumentParser(description="Rollback a batch of type classifications")
    parser.add_argument("--batch-id", required=True, help="Batch ID to rollback (e.g., batch_2026-07-27_001)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be rolled back without making changes")
    args = parser.parse_args()
    
    print(f"🔍 Searching for batch: {args.batch_id}")
    
    # audit_log 로드
    audit_data, log_file = load_audit_log()
    print(f"📄 Loaded audit log: {log_file.name}")
    
    # 배치 레코드 찾기
    batch_records = find_batch_records(audit_data, args.batch_id)
    if not batch_records:
        print(f"❌ No records found for batch_id: {args.batch_id}")
        sys.exit(1)
    
    print(f"✅ Found {len(batch_records)} records in this batch")
    
    # 롤백 실행
    results = []
    for record in batch_records:
        doc_path = record.get("document")
        proposed_type = record.get("proposed_type")
        
        if args.dry_run:
            print(f"  [DRY-RUN] Would rollback: {doc_path} (type: {proposed_type})")
            results.append({"document": doc_path, "status": "dry_run", "type": proposed_type})
        else:
            success, message = rollback_document(doc_path, proposed_type)
            status = "success" if success else "failed"
            print(f"  {'✅' if success else '❌'} {message}")
            results.append({"document": doc_path, "status": status, "type": proposed_type})
    
    # 롤백 이력 기록
    if not args.dry_run:
        rollback_audit = {
            "timestamp": datetime.now().isoformat(),
            "batch_id": args.batch_id,
            "total_records": len(batch_records),
            "results": results
        }
        
        rollback_file = AUDIT_LOG_DIR / f"rollback_{args.batch_id}.json"
        with open(rollback_file, "w", encoding="utf-8") as f:
            json.dump(rollback_audit, f, indent=2, ensure_ascii=False)
        
        print(f"\n📝 Rollback audit saved to: {rollback_file}")
    
    # 요약 보고
    success_count = sum(1 for r in results if r["status"] == "success")
    print(f"\n📊 Summary: {success_count}/{len(results)} documents rolled back successfully")


if __name__ == "__main__":
    main()
