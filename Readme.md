# 🤖 AI SQL Agent

An AI-powered SQL assistant built with **FastAPI**, **LangGraph**, **LangChain**, **Ollama**, and **SQLite**. The agent can generate SQL, explain queries, optimize SQL, detect bugs, inspect database schemas, and safely execute read-only SQL using tool-calling and conversation memory.

---

## ✨ Features

- 💬 Natural language SQL assistant
- 🧠 LangGraph agent with conversation memory
- 🛠️ LangChain tool calling
- 📝 Generate SQL from natural language
- 📖 Explain SQL queries
- ⚡ Optimize SQL queries
- 🐞 Detect SQL bugs and suggest fixes
- 🗂️ List database tables
- 📋 Describe database schemas
- 🔍 Execute read-only SQL queries
- 🔒 SQL safety validation (blocks destructive queries)
- 📊 Structured logging
- 🚀 FastAPI REST API
- 🗃️ SQLite database integration

---

# 🏗️ Project Architecture

```
                +------------------+
                |     FastAPI      |
                +--------+---------+
                         |
                         v
                +------------------+
                |   LangGraph AI   |
                |      Agent       |
                +--------+---------+
                         |
            +------------+-------------+
            |                          |
            v                          v
    SQL Tools                  Database Tools
    ---------                  --------------
    • Generate SQL             • List Tables
    • Explain SQL              • Describe Table
    • Optimize SQL             • Execute SQL
    • Detect Bugs

                         |
                         v
                  SQLite Database
```

---

# 📁 Project Structure

```
AI-SQL-Agent/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── graph/
│   ├── llm/
│   ├── models/
│   ├── prompts/
│   ├── tools/
│   ├── utils/
│   └── main.py
│
├── tests/
├── logs/
├── database.db
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# 🛠️ Tech Stack

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Programming Language          |
| FastAPI    | REST API                      |
| LangGraph  | Agent Workflow                |
| LangChain  | Tool Calling                  |
| Ollama     | Local LLM                     |
| Llama 3.x  | Language Model                |
| SQLite     | Database                      |
| SQLAlchemy | ORM / Database Access         |
| Pydantic   | Request & Response Validation |
| Uvicorn    | ASGI Server                   |

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/AI-SQL-Agent.git
cd AI-SQL-Agent
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download and install Ollama:

https://ollama.com/download

Pull the required model:

```bash
ollama pull llama3.2
```

_(Replace with the model configured in your `.env` if different.)_

---

## 5. Configure Environment Variables

Create a `.env` file:

```env
OLLAMA_MODEL=llama3.2
```

---

## 6. Run the application

```bash
uvicorn app.main:app --reload
```

---

## 7. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 💬 Example API Requests

## Generate SQL

```json
{
  "message": "Generate SQL to list all employees",
  "session_id": "default"
}
```

---

## Explain SQL

```json
{
  "message": "Explain SELECT * FROM employees",
  "session_id": "default"
}
```

---

## Optimize SQL

```json
{
  "message": "Optimize SELECT * FROM employees",
  "session_id": "default"
}
```

---

## Detect SQL Bugs

```json
{
  "message": "Find the bug in: SELEC * FROM employees",
  "session_id": "default"
}
```

---

## List Database Tables

```json
{
  "message": "List all database tables",
  "session_id": "default"
}
```

---

## Describe a Table

```json
{
  "message": "Describe the employees table",
  "session_id": "default"
}
```

---

## Execute SQL

```json
{
  "message": "Execute this SQL query: SELECT * FROM employees;",
  "session_id": "default"
}
```

---

# 🔒 SQL Safety

To protect the database, the application only executes **read-only** queries.

Allowed:

```sql
SELECT * FROM employees;
```

Blocked:

```sql
DROP TABLE employees;

DELETE FROM employees;

UPDATE employees SET salary = 100000;

INSERT INTO employees VALUES (...);

ALTER TABLE employees ...

TRUNCATE TABLE employees;
```

Unsafe queries are rejected before execution.

---

# 🧠 Agent Capabilities

The AI agent can:

- Generate SQL from natural language
- Explain SQL queries
- Optimize SQL performance
- Detect SQL syntax issues
- Inspect database schema
- Execute safe SQL queries
- Maintain conversational context using LangGraph memory
- Use tools dynamically through LangChain

---

# 📊 Logging

The application logs:

- Incoming user requests
- Tool selection
- SQL execution
- Query results
- Errors and exceptions

This improves observability and debugging.

---

# 🧪 Testing

Run the application:

```bash
uvicorn app.main:app --reload
```

Then test endpoints through:

```
http://127.0.0.1:8000/docs
```

---

# 🚀 Future Improvements

- Docker & Docker Compose
- PostgreSQL/MySQL support
- Authentication
- User-specific chat history
- Streaming responses
- Query execution statistics
- Multi-database support
- Vector database integration
- RAG for SQL documentation
- Web frontend (React/Next.js)
- CI/CD with GitHub Actions

---

# 🤝 Contributing

Contributions, bug reports, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request
