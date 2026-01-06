LOOPHOLE_SYSTEM_PROMPT = """
你是一位资深法务专家，专门负责审查合同中的逻辑漏洞(Loophole)。
任务：进行防御性审查，寻找定义模糊、权利不对等、条款缺失等问题。
输出：必须是严格的 JSON 格式。
"""

def get_loophole_prompt(clause_text: str) -> str:
    return f"""
请分析以下条款：
"{clause_text}"

请严格按照以下 JSON 键值返回（不要Markdown）：
{{
    "risk_found": true/false,
    "risk_type": "Ambiguity/Unfair_Term/Missing_Clause/None",
    "severity": "High/Medium/Low",
    "analysis": "说明...",
    "suggestion": "建议..."
}}
"""