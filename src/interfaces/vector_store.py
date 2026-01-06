from abc import ABC, abstractmethod
from typing import List, Dict

class VectorStore(ABC):
    """
    向量数据库抽象基类。
    后续可对接 ChromaDB, Milvus, Pinecone。
    """

    @abstractmethod
    def add_documents(self, documents: List[str], metadatas: List[Dict] = None):
        """存入文档片段"""
        pass

    @abstractmethod
    def search(self, query_vector: List[float], top_k: int = 5) -> List[str]:
        """根据向量检索相关文档"""
        pass