#!/bin/bash
# Evolution Gate - csp-brain Type 자동 분류의 안전장치
# 
# 이 스크립트는 다음 워크플로우를 실행한다:
# 1. evolution_gate.py 실행하여 자동 분류 및 patch 생성
# 2. validation_sample.json 을 Hermes 가 읽을 수 있도록 출력
# 3. 인간 승인 대기 (clarify 도구 사용은 Hermes 가 수행)
# 4. 승인 시, patch 파일들을 실제 문서에 적용
#
# 사용법:
#   ./scripts/evolution_gate.sh --batch-size 100
#   ./scripts/evolution_gate.sh --apply --batch-id batch_2026-07-27_001

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_ROOT="$(dirname "$SCRIPT_DIR")"
PENDING_DIR="$VAULT_ROOT/.pending_changes"

# 색상 정의
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${GREEN}════════════════════════════════════════${NC}"
    echo -e "${GREEN}  Evolution Gate: $1${NC}"
    echo -e "${GREEN}════════════════════════════════════════${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# 분류 실행 (Human approval 대기)
run_classification() {
    local batch_size=${1:-100}
    local offset=${2:-0}
    local dry_run=${3:-false}
    
    print_header "자동 분류 시작 (Batch: $batch_size 개)"
    
    if [ "$dry_run" = true ]; then
        echo -e "${YELLOW}🔍 DRY-RUN 모드: 실제 변경사항이 적용되지 않습니다${NC}"
        python3 "$SCRIPT_DIR/evolution_gate.py" --batch-size "$batch_size" --offset "$offset" --dry-run
    else
        python3 "$SCRIPT_DIR/evolution_gate.py" --batch-size "$batch_size" --offset "$offset"
    fi
    
    echo ""
    print_warning "📋 다음 단계:"
    echo "   1. Hermes 가 .pending_changes/validation_sample.json 을 읽습니다"
    echo "   2. clarify 도구로 10 개 샘플에 대한 인간 검증을 요청합니다"
    echo "   3. 80% 이상 승인되면, 아래 명령어로 실제 적용:"
    echo "      ./scripts/evolution_gate.sh --apply --batch-id <BATCH_ID>"
}

# 승인된 배치 실제 적용
apply_batch() {
    local batch_id=$1
    
    if [ -z "$batch_id" ]; then
        print_error "batch-id 가 필요합니다: --batch-id batch_2026-07-27_001"
        exit 1
    fi
    
    print_header "배치 적용: $batch_id"
    
    # audit_log 에서 해당 배치의 문서 목록 추출
    AUDIT_LOG="$VAULT_ROOT/audit_logs/classification_$(date +%Y-%m-%d).json"
    
    if [ ! -f "$AUDIT_LOG" ]; then
        print_error "audit_log 를 찾을 수 없습니다: $AUDIT_LOG"
        exit 1
    fi
    
    # Python 으로 audit_log 파싱하여 patch 적용
    python3 - "$batch_id" "$AUDIT_LOG" "$PENDING_DIR" << 'PYTHON_SCRIPT'
import sys
import json
from pathlib import Path
import shutil

batch_id = sys.argv[1]
audit_log_path = sys.argv[2]
pending_dir = Path(sys.argv[3])
vault_root = pending_dir.parent

# audit_log 로드
with open(audit_log_path, 'r', encoding='utf-8') as f:
    audit_data = json.load(f)

# 해당 배치의 레코드 찾기
batch_records = [r for r in audit_data if r.get('batch_id') == batch_id]

if not batch_records:
    print(f"❌ Batch ID 를 찾을 수 없습니다: {batch_id}")
    sys.exit(1)

print(f"✅ {len(batch_records)}개 문서의 patch 를 적용합니다...")

# patch 파일 적용
applied_count = 0
for record in batch_records:
    doc_path = record['document']
    patch_file_name = f"{Path(doc_path).parent.name}_{Path(doc_path).name}"
    patch_file = pending_dir / patch_file_name
    
    if patch_file.exists():
        # patch 파일을 실제 문서로 복사 (덮어쓰기)
        dest_path = vault_root / doc_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(patch_file, dest_path)
        print(f"  ✅ Applied: {doc_path}")
        applied_count += 1
    else:
        print(f"  ⚠️  Patch file not found: {patch_file}")

print(f"\n📊 요약: {applied_count}/{len(batch_records)}개 문서 적용 완료")

# patch 파일 정리 (백업은 .pending_changes 에 남김)
print(f"🗑️  Patch files are kept in .pending_changes/ for rollback safety")

# audit_log 업데이트 (human_approved: true 로 표시)
for record in batch_records:
    record['human_approved'] = True

with open(audit_log_path, 'w', encoding='utf-8') as f:
    json.dump(audit_data, f, indent=2, ensure_ascii=False)

print(f"📝 Audit log updated: human_approved=true for batch {batch_id}")
PYTHON_SCRIPT
    
    print_success "배치 적용 완료!"
    echo ""
    echo "📋 다음 단계:"
    echo "   git add -A"
    echo "   git commit -m \"feat: Applied type classification batch $batch_id via Evolution Gate\""
}

# 사용법 출력
show_usage() {
    echo "Usage:"
    echo "  $0 --classify [--batch-size N] [--offset N] [--dry-run]"
    echo "  $0 --apply --batch-id <BATCH_ID>"
    echo ""
    echo "Options:"
    echo "  --classify      자동 분류 실행 (human approval 대기)"
    echo "  --apply         승인된 배치 실제 적용"
    echo "  --batch-size N  배치 크기 (기본값: 100)"
    echo "  --offset N      오프셋 (기본값: 0)"
    echo "  --dry-run       실제 변경 없이 미리보기"
    echo "  --batch-id ID   적용할 배치 ID"
    echo "  --help          사용법 표시"
}

# 메인 로직
if [ $# -eq 0 ]; then
    show_usage
    exit 1
fi

case "$1" in
    --classify)
        shift
        BATCH_SIZE=100
        OFFSET=0
        DRY_RUN=false
        
        while [ $# -gt 0 ]; do
            case "$1" in
                --batch-size)
                    BATCH_SIZE="$2"
                    shift 2
                    ;;
                --offset)
                    OFFSET="$2"
                    shift 2
                    ;;
                --dry-run)
                    DRY_RUN=true
                    shift
                    ;;
                *)
                    print_error "Unknown option: $1"
                    show_usage
                    exit 1
                    ;;
            esac
        done
        
        run_classification "$BATCH_SIZE" "$OFFSET" "$DRY_RUN"
        ;;
    
    --apply)
        shift
        BATCH_ID=""
        
        while [ $# -gt 0 ]; do
            case "$1" in
                --batch-id)
                    BATCH_ID="$2"
                    shift 2
                    ;;
                *)
                    print_error "Unknown option: $1"
                    show_usage
                    exit 1
                    ;;
            esac
        done
        
        apply_batch "$BATCH_ID"
        ;;
    
    --help)
        show_usage
        ;;
    
    *)
        print_error "Unknown command: $1"
        show_usage
        exit 1
        ;;
esac
