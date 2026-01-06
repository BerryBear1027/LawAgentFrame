import requests
import json

# 1. 定义接口地址
url = "http://127.0.0.1:8000/analyze"

# 2. 准备测试数据 (模拟一个有霸王条款的合同)
payload = {
    "text": "甲方有权在任何时候单方面解除本合同，且无需承担任何违约责任。乙方若需解除合同，需提前90天申请。"
}

print(f"正在发送请求到 {url} ...")

try:
    # 3. 发送 POST 请求
    response = requests.post(url, json=payload)

    # 4. 打印结果
    if response.status_code == 200:
        print("\n✅ 测试成功！API 返回结果如下：")
        print("-" * 50)
        # 漂亮地打印 JSON
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        print("-" * 50)
    else:
        print(f"\n❌ 测试失败，状态码: {response.status_code}")
        print("错误信息:", response.text)

except Exception as e:
    print(f"\n❌ 连接错误: {e}")
    print("请检查：\n1. uvicorn 服务是否开启？\n2. 端口是否是 8000？")