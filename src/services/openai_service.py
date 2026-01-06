from typing import List, Dict
from src.interfaces.llm_provider import LLMProvider

class OpenAIService(LLMProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def chat_completion(self, messages: List[Dict[str, str]]) -> str:
        # TODO: 这里后续接入真实的 openai 库
        return "Mock response: This is a test analysis."

    async def get_embedding(self, text: str) -> List[float]:
        # TODO: 后续接入 text-embedding-3-small
        return [0.1, 0.2, 0.3] # Mock vector