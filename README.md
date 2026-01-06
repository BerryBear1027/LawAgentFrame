# 合同风险智能分析系统 (Contract Risk AI) - 架构设计与实施路线图

## 1. 架构设计哲学：整洁架构 (Clean Architecture)

本项目采用 **Clean Architecture (整洁架构)** 模式。这种架构的核心思想是将“业务逻辑”与“外部依赖”完全分离。

* **内层 (Core/Interfaces)**：定义了系统要做什么（比如：分析风险、读取文档）。这里不包含任何具体的 API 调用代码，只定义规则。
* **外层 (Services/API)**：负责具体的脏活累活（比如：调用 OpenAI、读取磁盘上的 PDF、启动 Web 服务器）。


# 合同风险智能分析 — 项目说明（当前状态）

此仓库提供了一个以“整洁架构”为指导思想搭建的项目骨架，用于后续实现合同风险分析相关能力。当前代码主要是框架与接口定义，很多实现为 Stub/Mock；仓库不包含训练数据、生产向量库或已对接的模型服务。

重要提示：README 中描述的多数功能仍为计划或建议的实现路径，当前仓库只是开发骨架，请勿假定已有完整数据集或对外可用的 API。

**当前目标**：提供清晰的代码组织、接口定义（抽象层）和一个可扩展的起点，便于后续逐步实现 LLM 集成、文档解析、向量检索与业务编排逻辑。

**仓库结构（简要）**

- `src/api/` — Web 入口（FastAPI stub）。包含 `main.py`，用于接收请求并调用核心引擎的示例路由；目前主要为示范接口位置，而不是完整生产接口。
- `src/core/` — 业务编排核心。`risk_engine.py` 提供了引擎的框架（如何接收 provider 与 vector store），当前为流程骨架/桩实现。
- `src/interfaces/` — 抽象定义（Protocol/ABC）。包含 `llm_provider.py`（定义 chat/completion 与 embedding 方法）、`document_loader.py`、`vector_store.py` 等接口，供后续实现遵循。
- `src/services/` — 基础服务实现位置。`openai_service.py` 当前为演示/Mock 实现（返回固定或占位内容），尚未包含真实的 OpenAI SDK 调用。
- `src/evaluation/`、`src/utils/`、`tests/` — 用于评估、工具函数和测试的占位目录。
- `requirements.txt`、`.env.example` — 依赖与环境变量示例（例如 `OPENAI_API_KEY`），仅作参考。

当前实现的关键点（事实说明）

- `src/interfaces/llm_provider.py`：定义了必须实现的方法签名（抽象基类/协议）。
- `src/core/risk_engine.py`：提供引擎构造和流程占位（stub），未实现完整的检索-生成编排逻辑。
- `src/services/openai_service.py`：目前为 Mock/示例实现，不会对外发起真实 API 请求（需要用户添加 API key 并替换为实际 SDK 调用）。
- `src/api/main.py`：包含 FastAPI 启动示例与路由位置（示范如何将请求传给核心引擎），但不应视为已部署的、对外稳定的 HTTP API。

建议的下一步（显式为“待实现”而非已完成）

1. LLM 集成：在 `src/services/openai_service.py` 中引入官方 SDK，并用 `.env` 中的 `OPENAI_API_KEY` 安全加载真实调用。先在本地测试小请求。
2. 文档加载与切片：实现 `DocumentLoader`，支持 PDF/文本的解析与按业务规则切片（合同条款编号、章节等）。
3. 向量存储：选择并实现 `VectorStore`（如 ChromaDB、FAISS 等），并创建数据导入脚本用于构建检索库。
4. 完善 `risk_engine.py`：实现检索-提示拼接-调用 LLM 的完整 RAG 流程及结果解析、结构化输出。
5. 测试与 CI：补充单元/集成测试，确保接口契约与实现一致。

#### 第一步：下载代码
在终端（Terminal）或 Git Bash 中运行：
```bash
git clone https://github.com/BerryBear1027/LawAgentFrame.git
cd LawAgentFrame
```

#### 第二步：创建并激活虚拟环境

**Windows 用户 (PowerShell):**

```powershell
# 1. 创建环境
python -m venv .venv

# 2. 激活环境 (注意斜杠)
.\.venv\Scripts\Activate.ps1
```

*如果不成功，试一下 `.\.venv\Scripts\activate*`
*激活成功标志：命令行前面会出现绿色的 `(.venv)*`

**Mac / Linux 用户:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 第三步：安装依赖库

确保终端前有 `(.venv)` 标志，然后运行以下命令（使用清华源加速，防止报错）：

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### 第四步：配置环境变量

由于安全原因，`.env` 文件没有上传。你需要手动创建一个。

1. 在项目根目录下新建一个文件，命名为 `.env` (注意前面有点)。
2. 在里面写入以下内容（目前先用 Mock Key）：
```ini
OPENAI_API_KEY=sk-mock-key-for-testing
```
#### 第五步：启动服务
在终端运行：
```bash
uvicorn src.api.main:app --reload
```

如果看到以下提示，说明启动成功：

> INFO: Uvicorn running on [http://127.0.0.1:8000](http://127.0.0.1:8000)

#### 第六步：验证是否成功
终端运行测试脚本：

```bash
python test_api_script.py
```

---

如果也用 PyCharm，可能会遇到“解释器为空”的情况：

1. 打开 PyCharm -> **Settings** -> **Python Interpreter**。
2. 点击 **Add Interpreter** -> **Local**。
3. 选择 **Existing**。
4. 路径指向项目文件夹下的 `.venv/Scripts/python.exe` (Windows) 或 `.venv/bin/python` (Mac)。
5. **一定要把 `src` 文件夹标记为源码根目录**：右键 `src` 文件夹 -> **Mark Directory as** -> **Sources Root**。

---
