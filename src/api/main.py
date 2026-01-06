from fastapi import FastAPI
from src.core.risk_engine import ContractRiskEngine
from src.services.openai_service import OpenAIService
from src.schemas import AnalysisRequest, AnalysisResponse

# 1. 初始化 App
app = FastAPI(title="Contract Risk Analysis AI", version="0.1.0")

# 2. 依赖注入
# 暂时用 Mock 数据初始化
llm_service = OpenAIService(api_key="mock_key")
risk_engine = ContractRiskEngine(llm=llm_service, vector_store=None)

# 3. 定义健康检查接口 (这是那个绿色的条目)
@app.get("/")
def health_check():
    return {"status": "System is running"}

# ==========================================
# 4. 定义核心分析接口 (你缺的就是这一段！！！)
# ==========================================
@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_contract(request: AnalysisRequest):
    """
    接收合同文本，调用核心引擎进行漏洞分析
    """
    # 调用核心引擎
    result = await risk_engine.analyze_clause(request.text)
    return result

# 5. 方便直接运行的入口
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)