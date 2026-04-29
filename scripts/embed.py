"""
임베딩 생성기 (Embedding Generator)
- 마크다운 문서 내용을 임베딩
- Qdrant 벡터 DB 에 저장
- 하이브리드 검색 (BM25 + Vector) 지원

Note: 기업 방화벽 환경에서는 로컬 모델 사용 필요
"""
import json
import hashlib
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
import numpy as np

# SSL 인증서 문제 해결 (기업 환경)
os.environ.setdefault('CURL_CA_BUNDLE', '')
os.environ.setdefault('REQUESTS_CA_BUNDLE', '')

# sentence-transformers 임포트
try:
    from sentence_transformers import SentenceTransformer
    import ssl
    # SSL 검증 비활성화 (기업 프록시 환경)
    ssl._create_default_https_context = ssl._create_unverified_context
except ImportError:
    print("[WARNING] sentence-transformers 가 설치되지 않았습니다.")
    print("  실행: pip install sentence-transformers")
    raise


class EmbeddingGenerator:
    """문서 임베딩 생성 및 관리"""

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        cache_folder: Optional[str] = None,
        local_model_path: Optional[str] = None
    ):
        """
        Args:
            model_name: 임베딩 모델 이름
            cache_folder: HuggingFace 캐시 폴더
            local_model_path: 로컬 모델 경로 (오프라인용)
        """
        self.model_name = model_name
        self.cache_folder = cache_folder

        if local_model_path and Path(local_model_path).exists():
            print(f"[INIT] 로컬 모델 로드: {local_model_path}")
            self.model = SentenceTransformer(local_model_path)
        else:
            print(f"[INIT] 모델 로드 중: {model_name} (캐시: {cache_folder})")
            self.model = SentenceTransformer(model_name, cache_folder=cache_folder)

        self.dimension = self.model.get_sentence_embedding_dimension()
        print(f"[INIT] 임베딩 모델 준비 완료: {self.dimension}차원")

    def embed_text(self, text: str) -> np.ndarray:
        """단일 텍스트 임베딩"""
        return self.model.encode(text, normalize_embeddings=True)

    def embed_batch(self, texts: List[str], batch_size: int = 32) -> np.ndarray:
        """배치 임베딩"""
        return self.model.encode(
            texts,
            batch_size=batch_size,
            normalize_embeddings=True,
            show_progress_bar=True
        )

    def compute_hash(self, text: str) -> str:
        """텍스트 해시 (변경 감지용)"""
        return hashlib.md5(text.encode()).hexdigest()


class DocumentIndex:
    """문서 인덱스 (Qdrant 기반)"""

    def __init__(self, collection_name: str = "zavis_brain", in_memory: bool = False):
        """
        Args:
            collection_name: Qdrant 컬렉션 이름
            in_memory: 인메모리 모드 (테스트용)
        """
        try:
            from qdrant_client import QdrantClient
            from qdrant_client.models import (
                Distance, VectorParams, PointStruct,
                Filter, FieldCondition, MatchValue
            )
        except ImportError:
            print("[WARNING] qdrant-client 가 설치되지 않았습니다.")
            print("  실행: pip install qdrant-client")
            raise

        self.collection_name = collection_name

        if in_memory:
            self.client = QdrantClient(":memory:")
        else:
            self.client = QdrantClient(path="./vector_store")

        self.qdrant = QdrantClient
        self.VectorParams = VectorParams
        self.PointStruct = PointStruct
        self.Filter = Filter
        self.FieldCondition = FieldCondition
        self.MatchValue = MatchValue

    def create_collection(self, dimension: int, force: bool = False):
        """컬렉션 생성"""
        if force and self.client.collection_exists(self.collection_name):
            self.client.delete_collection(self.collection_name)

        if not self.client.collection_exists(self.collection_name):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=dimension,
                    distance=Distance.COSINE
                )
            )
            print(f"[INIT] 컬렉션 생성: {self.collection_name}")

    def upsert_documents(self, documents: List[Dict], embeddings: np.ndarray):
        """문서 업서트 (삽입/업데이트)"""
        points = []
        for i, doc in enumerate(documents):
            point = PointStruct(
                id=i,
                vector=embeddings[i].tolist(),
                payload=doc
            )
            points.append(point)

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        print(f"[UPSERT] {len(documents)} 개 문서 인덱싱 완료")

    def search(
        self,
        query_vector: np.ndarray,
        limit: int = 10,
        category_filter: Optional[str] = None
    ) -> List[Dict]:
        """벡터 검색"""
        query_filter = None
        if category_filter:
            query_filter = self.Filter(
                must=[
                    self.FieldCondition(
                        key="category",
                        match=self.MatchValue(value=category_filter)
                    )
                ]
            )

        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector.tolist(),
            limit=limit,
            query_filter=query_filter
        )

        return [
            {
                "path": hit.payload.get("path"),
                "md_path": hit.payload.get("md_path"),
                "category": hit.payload.get("category"),
                "tags": hit.payload.get("tags"),
                "score": hit.score,
                "snippet": hit.payload.get("content", "")[:200]
            }
            for hit in results
        ]


def build_embeddings(
    vault_dir: Path,
    manifest_path: Path,
    output_dir: Path,
    use_qdrant: bool = True
):
    """임베딩 빌드 파이프라인"""

    # manifest.json 로드
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 임베딩 생성기 초기화
    embedder = EmbeddingGenerator()

    # 문서 콘텐츠 수집
    documents = []
    doc_ids = []

    print("[EMBED] 문서 콘텐츠 수집 중...")

    for filepath, entry in manifest.items():
        md_path = Path(entry.get('md_path', ''))

        if not md_path.exists():
            continue

        content = md_path.read_text(encoding='utf-8')

        # 메타데이터와 콘텐츠 결합
        doc_text = f"""
        카테고리: {entry.get('category', 'Uncategorized')}
        태그: {', '.join(entry.get('tags', []))}
        파일: {filepath}
        ---
        {content[:3000]}  # 첫 3000 자만
        """.strip()

        documents.append({
            "path": filepath,
            "md_path": str(md_path),
            "category": entry.get('category', 'Uncategorized'),
            "tags": entry.get('tags', []),
            "content": content[:2000],  # 스니펫용
            "hash": entry.get('hash', '')
        })
        doc_ids.append(filepath)

    print(f"[EMBED] {len(documents)} 개 문서 임베딩 중...")

    # 배치 임베딩
    texts = [
        f"{doc['category']} {' '.join(doc['tags'])} {doc['content'][:1000]}"
        for doc in documents
    ]
    embeddings = embedder.embed_batch(texts)

    # 로컬 저장 (NumPy)
    output_dir.mkdir(parents=True, exist_ok=True)
    np.save(output_dir / "embeddings.npy", embeddings)
    with open(output_dir / "documents.json", 'w', encoding='utf-8') as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)

    print(f"[SAVE] 임베딩 저장: {output_dir / 'embeddings.npy'}")

    # Qdrant 에 저장
    if use_qdrant:
        print("[QDRANT] 벡터 DB 구축 중...")
        index = DocumentIndex(in_memory=False)
        index.create_collection(embedder.dimension, force=True)
        index.upsert_documents(documents, embeddings)
        print("[QDRANT] 완료")

    return {
        "total_documents": len(documents),
        "dimension": embedder.dimension,
        "output_dir": str(output_dir)
    }


if __name__ == "__main__":
    # 경로를 동적으로 계산
    BASE_DIR = Path(__file__).parent.parent
    MANIFEST_PATH = BASE_DIR / "manifest.json"
    OUTPUT_DIR = BASE_DIR / "harness" / "embeddings"

    # 임베딩 빌드
    result = build_embeddings(
        vault_dir=BASE_DIR,
        manifest_path=MANIFEST_PATH,
        output_dir=OUTPUT_DIR,
        use_qdrant=True
    )

    print(f"\n[RESULT] 임베딩 빌드 완료:")
    print(f"  - 문서: {result['total_documents']}개")
    print(f"  - 차원: {result['dimension']}")
    print(f"  - 저장소: {result['output_dir']}")
