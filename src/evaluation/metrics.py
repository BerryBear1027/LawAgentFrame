from typing import Dict, Any


class LoopholeEvaluator:
    @staticmethod
    def evaluate(prediction: Dict, ground_truth: Dict) -> Dict[str, Any]:
        """
        对比 AI 的预测 (prediction) 和 标准答案 (ground_truth)
        """
        score = 0
        feedback = []

        # 1. 它是把有漏洞的说成没漏洞了吗？(Recall)
        if prediction.get("risk_found") == ground_truth.get("risk_exists"):
            score += 40
        else:
            return {"score": 0, "reason": "漏洞检出状态错误"}

        # 2. 漏洞类型对不对？
        # ... (这里写逻辑判断类型是否匹配)

        return {"score": score, "feedback": feedback}