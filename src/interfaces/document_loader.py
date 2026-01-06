from abc import ABC, abstractmethod
from typing import List

class DocumentLoader(ABC):
    """
    文档加载抽象基类。
    后续可扩展 PDFLoader, DocxLoader, TXTLoader。
    """

    @abstractmethod
    def load(self, file_path: str) -> str:
        """读取文件并返回完整文本"""
        pass

    @abstractmethod
    def chunk(self, text: str, chunk_size: int = 1000) -> List[str]:
        """将长文本切分为片段"""
        pass