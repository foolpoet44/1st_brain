"""
시맨틱 검색 API (Semantic Search API)
- BM25 기반 키워드 검색
- 임베딩 기반 시맨틱 검색 (선택)
- 하이브리드 검색 지원
"""
import json
import re
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from collections import Counter
import math


class BM25Search:
    """BM25 기반 키워드 검색"""

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        """
        Args:
            k1: 단어 빈도 가중치 (1.2~2.0)
            b: 문서 길이 정규화 (0.5~1.0)
        """
        self.k1 = k1
        self.b = b
        self.documents = []
        self.doc_lengths = []
        self.avg_doc_length = 0
        self.term_freq = {}  # term -> {doc_id: tf}
        self.doc_count = 0

    def tokenize(self, text: str) -> List[str]:
        """텍스트 토큰화 (한글/영문)"""
        # 한글 (2 글자 이상), 영문 (3 글자 이상)
        pattern = r'[가-힣]{2,}|[a-zA-Z]{3,}'
        return re.findall(pattern, text.lower())

    def index(self, documents: List[Dict]):
        """문서 인덱싱"""
        self.documents = documents
        self.doc_count = len(documents)

        # 토큰화 및 통계
        self.doc_lengths = []
        self.term_freq = {}

        for i, doc in enumerate(documents):
            text = f"{doc.get('category', '')} {' '.join(doc.get('tags', []))} {doc.get('content', '')}"
            tokens = self.tokenize(text)

            # 문서 길이
            self.doc_lengths.append(len(tokens))

            # 단어 빈도
            for token in set(tokens):
                if token not in self.term_freq:
                    self.term_freq[token] = {}
                self.term_freq[token][i] = self.term_freq[token].get(i, 0) + 1

        # 평균 문서 길이
        self.avg_doc_length = sum(self.doc_lengths) / len(self.doc_lengths) if self.doc_lengths else 0

        print(f"[BM25] 인덱싱 완료: {self.doc_count}개 문서, {len(self.term_freq)}개 용어")

    def search(self, query: str, top_k: int = 10) -> List[Dict]:
        """BM25 검색"""
        query_tokens = self.tokenize(query)

        scores = Counter()

        for token in query_tokens:
            if token not in self.term_freq:
                continue

            # IDF 계산
            df = len(self.term_freq[token])
            idf = math.log((self.doc_count - df + 0.5) / (df + 0.5) + 1)

            for doc_id, tf in self.term_freq[token].items():
                # BM25 스코어
                doc_len = self.doc_lengths[doc_id]
                numerator = tf * (self.k1 + 1)
                denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avg_doc_length)

                scores[doc_id] += idf * (numerator / denominator)

        # 상위 결과 반환
        results = []
        for doc_id, score in scores.most_common(top_k):
            doc = self.documents[doc_id]
            results.append({
                "path": doc.get("path"),
                "md_path": doc.get("md_path"),
                "category": doc.get("category"),
                "tags": doc.get("tags"),
                "score": round(score, 4),
                "snippet": doc.get("content", "")[:200]
            })

        return results


class HybridSearch:
    """하이브리드 검색 (BM25 + Vector)"""

    def __init__(self, index_dir: Optional[Path] = None):
        self.bm25 = BM25Search()
        self.index_dir = index_dir
        self.embeddings = None
        self.documents = []

        # 임베딩 로드 시도
        if index_dir and (index_dir / "embeddings.npy").exists():
            try:
                self.embeddings = np.load(index_dir / "embeddings.npy")
                with open(index_dir / "documents.json", 'r', encoding='utf-8') as f:
                    self.documents = json.load(f)
                print(f"[HYBRID] 임베딩 로드: {len(self.embeddings)}개")
            except Exception as e:
                print(f"[HYBRID] 임베딩 로드 실패: {e}")

    def index_from_manifest(self, manifest_path: Path, vault_dir: Path):
        """manifest.json 에서 인덱스 구축"""
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)

        # 모든 .md 파일 스캔 (서브디렉토리 포함)
        all_md_files = {}
        for md_file in vault_dir.rglob("*.md"):
            all_md_files[md_file.name.lower()] = md_file

        documents = []
        not_found = []

        for filepath, entry in manifest.items():
            # 원본 파일명으로 마크다운 파일 찾기
            source_filename = Path(filepath).name  # e.g., "보고자료.pptx"
            md_filename = source_filename + '.md'  # e.g., "보고자료.pptx.md"

            md_path = all_md_files.get(md_filename.lower())

            if not md_path:
                not_found.append(source_filename)
                continue

            try:
                content = md_path.read_text(encoding='utf-8')
            except Exception as e:
                print(f"[WARN] 파일 읽기 실패: {md_path} - {e}")
                continue

            documents.append({
                "path": filepath,
                "md_path": str(md_path),
                "category": entry.get('category', 'Uncategorized'),
                "tags": entry.get('tags', []),
                "content": content
            })

        # BM25 인덱스
        self.bm25.index(documents)
        self.documents = documents

        print(f"[HYBRID] 인덱스 완료: {len(documents)}개 문서 ({len(not_found)}개 파일 없음)")
        if len(not_found) < 10:
            for f in not_found:
                print(f"  - 없음: {f}")

    def search(
        self,
        query: str,
        top_k: int = 10,
        category_filter: Optional[str] = None,
        use_vector: bool = False
    ) -> List[Dict]:
        """
        검색 실행

        Args:
            query: 검색어
            top_k: 반환 결과 수
            category_filter: 카테고리 필터
            use_vector: 벡터 검색 사용 여부
        """
        # BM25 검색
        bm25_results = self.bm25.search(query, top_k * 2)

        # 카테고리 필터
        if category_filter:
            bm25_results = [r for r in bm25_results if r.get('category') == category_filter]

        # 벡터 검색 (선택)
        if use_vector and self.embeddings is not None:
            print("[HYBRID] 벡터 검색은 현재 지원되지 않습니다 (모델 로드 필요)")

        # 상위 k 개 결과
        return bm25_results[:top_k]


def create_search_api(manifest_path: Path, vault_dir: Path, index_dir: Path):
    """검색 API 생성"""
    searcher = HybridSearch(index_dir)
    searcher.index_from_manifest(manifest_path, vault_dir)
    return searcher


if __name__ == "__main__":
    # 경로를 동적으로 계산
    BASE_DIR = Path(__file__).parent.parent
    MANIFEST_PATH = BASE_DIR / "manifest.json"
    INDEX_DIR = BASE_DIR / "harness" / "embeddings"

    # 검색기 초기화
    searcher = create_search_api(MANIFEST_PATH, BASE_DIR, INDEX_DIR)

    # 데모 검색
    print("\n=== 검색 데모 ===")
    test_queries = [
        "임원 모니터링",
        "AX 교육",
        "주간보고",
        "인원현황"
    ]

    for query in test_queries:
        print(f"\n[SEARCH] 검색어: {query}")
        results = searcher.search(query, top_k=3)
        for i, r in enumerate(results, 1):
            print(f"  {i}. [{r['category']}] {Path(r['path']).name} (score: {r['score']})")
        if not results:
            print("  - 결과 없음")
