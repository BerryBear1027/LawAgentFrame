from abc import ABC, abstractmethod
from typing import List, Dict, Any

class LLMProvider(ABC):
    """
    LLM 交互的抽象基类。
    无论是接 OpenAI, Claude 还是本地模型，都必须实现这些方法。
    """

    @abstractmethod
    async def chat_completion(self, messages: List[Dict[str, str]]) -> str:
        """发送对话并获取回复"""
        pass

    @abstractmethod
    async def get_embedding(self, text: str) -> List[float]:
        """获取文本向量"""
        pass