# AI Agent Project

A modular AI Agent built using **FastAPI**, **LangGraph**, **LangChain**, and **Ollama**. This project is designed to serve as a scalable foundation for building intelligent AI workflows, agents, and APIs.

---

## 🚀 Features

- FastAPI backend
- LangGraph workflow engine
- Ollama integration for local LLMs
- Environment-based configuration
- Centralized logging
- Modular project structure
- Git version control

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- LangGraph
- LangChain
- LangChain-Ollama
- Ollama
- Uvicorn
- Python-dotenv

---

## 📁 Project Structure

```text
ai-agent-project/
│
├── app/
│   ├── api/
│   ├── core/
│   │   ├── config.py
│   │   └── logger.py
│   ├── graph/
│   │   └── workflow.py
│   ├── llm/
│   │   └── ollama_client.py
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── logs/
├── tests/
├── .env
├── .gitignore
├── requirements.txt
├── test_ollama.py
├── test_graph.py
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ABDULSAMAD201/ai-agent-project.git
cd ai-agent-project
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download Ollama from:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

Download the Llama model:

```bash
ollama pull llama3.2
```

Verify installed models:

```bash
ollama list
```

---

## 🔧 Environment Variables

Create a `.env` file in the project root.

```env
APP_NAME=AI Agent Project
HOST=127.0.0.1
PORT=8000
OLLAMA_MODEL=llama3.2
```

---

## ▶️ Running the Application

Start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Testing

### Test Ollama

```bash
python test_ollama.py
```

### Test LangGraph

```bash
python test_graph.py
```

---

## 📌 Current Progress

### Phase 1

- Project setup
- FastAPI application
- LangGraph integration
- Ollama integration
- Configuration management
- Logging
- GitHub repository setup

---

## 📅 Roadmap

### Phase 2

- Chat API endpoint
- LangGraph execution through FastAPI
- Request and response models

### Phase 3

Implemented features:

- SQL Query Explanation
- SQL Bug Detection
- SQL Query Optimization
- Natural Language to SQL Generation
- Intent-based routing using LangGraph
- Modular graph architecture
- Reusable LLM helper for cleaner node implementation

Current Capabilities:

- Explain SQL queries
- Detect SQL syntax and logic issues
- Suggest query optimizations
- Generate SQL from natural language
- Automatically route requests to the appropriate AI node

### Phase 4

- Tool integration
- Multi-agent workflows
- Retrieval-Augmented Generation (RAG)

---

## 📄 License

This project is for educational and learning purposes.

---

## 👨‍💻 Author

**Abdul Samad**

GitHub: https://github.com/ABDULSAMAD201
