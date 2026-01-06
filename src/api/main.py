from fastapi import FastAPI
from src.core.risk_engine import ContractRiskEngine
from src.services.openai_service import OpenAIService
from src.schemas import AnalysisRequest, AnalysisResponse

app = FastAPI(title="Contract Risk AI")

# 这里填你的 OpenAI Key，或者先写 "sk-mock-key" 跑通流程
llm_service = OpenAIService(api_key="sk-mock-key")
risk_engine = ContractRiskEngine(llm=llm_service, vector_store=None)

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_contract(request: AnalysisRequest):
    result = await risk_engine.analyze_clause(request.text)
    return result