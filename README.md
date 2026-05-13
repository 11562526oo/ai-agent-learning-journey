为什么学 AI Agent

当前学习进度

学习路线

已完成项目

如何运行代码


# AI Agent Learning Journey

一个用于记录 **AI Agent 学习、实验、项目实践与工程化落地** 的个人仓库。

这个仓库的目标不是只存放零散 demo，而是持续沉淀：

- **基础知识**
- **实验代码**
- **Prompt 模板**
- **正式项目**
- **复盘笔记**
- **架构设计**

希望通过长期积累，把这个仓库逐步建设成我的 **AI Agent 第二大脑**。

---

## 仓库目标

本仓库主要用于完成以下目标：

1. 学习 LLM 基础能力与 API 调用方式
2. 理解 Prompt Engineering、Tool Calling、RAG、ReAct 等核心概念
3. 用 Python 快速验证 AI Agent 原理
4. 用 Java 做企业级工程化落地
5. 沉淀可复用的 Prompt、脚本、组件与项目模板
6. 最终完成多个可展示的 AI Agent 项目

---

## 当前学习路线

### 阶段 1：基础能力
- LLM API 调用
- Message 结构
- System Prompt
- Temperature
- 基础文本任务：总结、分类、抽取、改写

### 阶段 2：Tool Calling 与 Agent 原理
- Function Calling / Tool Use
- ReAct 模式
- 手写 Agent 循环
- 文件、命令、搜索等工具接入

### 阶段 3：RAG 与完整应用
- Embedding
- 向量数据库
- 文档切分
- 检索增强生成
- 带前端界面的 AI 应用

### 阶段 4：Java 工程化
- Spring AI
- LangChain4j
- Java Agent 服务化
- 企业级落地与可观测性

---

## 目录结构

````text
ai-agent-learning-journey/
├── README.md
├── .gitignore
├── docs/   用于存放学习过程中的文档沉淀，包括计划、笔记、周复盘和架构设计
│   ├── learning-plan.md    总体学习计划和阶段目标
│   ├── weekly-review/  每周学习复盘
│   │   ├── week1.md
│   │   ├── week2.md
│   │   └── week3.md
│   ├── notes/  主题化技术笔记
│   │   ├── llm-basics.md
│   │   ├── prompt-engineering.md
│   │   ├── tool-calling.md
│   │   ├── rag.md
│   │   └── react-agent.md
│   └── architecture/   存放项目架构设计、模块说明、流程图说明等内容
│       ├── mini-agent-architecture.md
│       └── knowledge-base-architecture.md
├── playground/     用于存放学习阶段的实验代码和小 demo
│   ├── python/     用于用 Python 快速验证 AI Agent 原理
│   │   ├── week1/
│   │   │   ├── day1_hello_llm.py
│   │   │   ├── day2_prompt_compare.py
│   │   │   ├── day3_text_tasks.py
│   │   │   ├── day4_chain_of_thought.py
│   │   │   ├── day5_weekly_report_generator.py
│   │   │   ├── utils.py
│   │   │   └── requirements.txt
│   │   ├── week2/
│   │   ├── week3/
│   │   └── common/
│   └── java/       用于用 Java 做后续工程化验证
│       ├── spring-ai-demo/
│       ├── langchain4j-demo/
│       └── common/
├── projects/   用于存放正式项目，区别于 playground 的实验性质
│   ├── 01-mini-react-agent/
│   │   ├── README.md
│   │   ├── backend/
│   │   ├── frontend/
│   │   ├── docs/
│   │   └── examples/
│   ├── 02-personal-knowledge-base/
│   │   ├── README.md
│   │   ├── backend/
│   │   ├── frontend/
│   │   ├── ingestion/
│   │   ├── docs/
│   │   └── examples/
│   └── 03-java-enterprise-agent/
│       ├── README.md
│       ├── backend/
│       ├── frontend/
│       ├── docs/
│       └── examples/
├── prompts/    用于存放 Prompt 资产
│   ├── system-prompts/
│   │   ├── code-assistant.md
│   │   ├── weekly-report-assistant.md
│   │   └── rag-assistant.md
│   ├── task-prompts/
│   │   ├── summarize.md
│   │   ├── classify.md
│   │   └── extract.md
│   └── experiments/
│       ├── prompt-test-001.md
│       └── prompt-test-002.md
├── scripts/    用于存放辅助脚本，提高学习和实验效率
│   ├── init_env.sh
│   ├── run_python_demo.sh
│   └── format_notes.sh
└── assets/ 用于存放静态资源
    ├── images/
    └── diagrams/

````
---
### 代码提交规范  
feat: add week1 day1 hello llm demo 新增功能

feat: add system prompt comparison example

feat: implement weekly report generator

docs: add week1 review notes    文档修改

refactor: extract common llm utils  重构代码

fix: ~~~~
