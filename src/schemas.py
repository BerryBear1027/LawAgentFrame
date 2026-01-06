from pydantic import BaseModel, Field
from typing import List, Literal

class AnalysisRequest(BaseModel):
    text: str = Field(..., description="需要分析的合同条款")

class LoopholeDetail(BaseModel):
    risk_found: bool
    risk_type: Literal["Missing_Clause", "Ambiguity", "Unfair_Term", "Logic_Conflict", "None"]
    severity: Literal["High", "Medium", "Low"]
    analysis: str
    suggestion: str

class AnalysisResponse(BaseModel):
    findings: List[LoopholeDetail]