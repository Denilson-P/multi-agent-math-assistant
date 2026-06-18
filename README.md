# 🧮 Multi-Agent Math Assistant

A multi-agent mathematical chatbot built with Python, Streamlit, OpenAI, and specialized AI agents.

The goal of this project is to demonstrate practical concepts such as:

* Agent orchestration
* Tool calling
* Prompt engineering
* Guardrails
* Conversation memory
* Context management
* Multi-language support
* Separation of responsibilities between agents

---

# 🚀 Features

## Specialized Agents

### 🧠 Expression Interpreter Agent

Responsible for:

* Understanding natural language requests
* Extracting mathematical expressions from text
* Supporting follow-up calculations
* Using conversation context
* Preparing expressions for execution

This agent does **not** perform calculations.

---

### 🔢 Mathematical Agent

Responsible for:

* Executing mathematical operations
* Using tools as the source of truth
* Handling mathematical expressions
* Returning structured results

Supported operations:

* Addition
* Subtraction
* Multiplication
* Division

All calculations are executed through dedicated tools.

---

### ✍️ Writer Agent

Responsible for:

* Generating user-friendly responses
* Adapting answers to the user's language
* Formatting calculation results
* Explaining errors naturally

This agent never performs calculations.

---

## 🧠 Conversation Memory

The chatbot maintains context during the conversation and supports follow-up requests.

Example:

User:

```text
What is 5 + 4?
```

Assistant:

```text
The result is 9.
```

User:

```text
Now multiply it by 3.
```

Assistant:

```text
After the multiplication, we get 27.
```

---

## 🌎 Multi-Language Support

The chatbot automatically detects the user's language and responds accordingly.

Examples:

Portuguese:

```text
Quanto é 5 + 4?
```

English:

```text
What is 5 plus 4?
```

Spanish:

```text
¿Cuánto es 5 más 4?
```

The response language automatically adapts to the user input.

---

## 🛡️ Error Handling

The application gracefully handles:

* Division by zero
* Invalid expressions
* Unsupported calculations
* Interpretation failures
* Unexpected calculation errors

Errors are converted into friendly responses in the user's language.

---

# 🏗️ Architecture

```text
User
 │
 ▼
Streamlit Interface
 │
 ▼
Language Detector
 │
 ▼
Expression Interpreter Agent
 │
 ▼
Mathematical Agent
 │
 ▼
Math Tools
 │
 ▼
Writer Agent
 │
 ▼
Conversation Memory
 │
 ▼
Response
```

---

# 📂 Project Structure

```text
app/
│
├── agents/
│   ├── expression_interpreter_agent.py
│   ├── mathematical_agent.py
│   └── writer_agent.py
│
├── clients/
│   └── openai_client.py
│
├── language/
│   └── language_detector.py
│
├── memory/
│   └── conversation_memory.py
│
├── orchestrator/
│   └── chat_orchestrator.py
│
├── prompts/
│   ├── expression_interpreter_prompt.py
│   └── writer_prompt.py
│
├── tools/
│   ├── math_tools.py
│   └── tool_registry.py
│
└── main.py
```

---

# ⚙️ Technologies

* Python 3.12+
* Streamlit
* OpenAI SDK
* GPT-4o-mini
* Poetry

---

# 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/Raniel-Git/multi-agent-math-assistant.git
cd multi-agent-math-assistant
```

Install dependencies:

```bash
poetry install
```

Activate the environment:

```bash
source $(poetry env info --path)/bin/activate
```

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

# ▶️ Running the Application

Start Streamlit:

```bash
poetry run streamlit run app/main.py
```

Or:

```bash
streamlit run app/main.py
```

---

# 💡 Example Requests

```text
Calculate: (18 + 6) / 3
```

```text
Multiply the result by 4
```

```text
I have 6 boxes with 12 items each and lost 9 items.
How many are left?
```

```text
What is five plus four?
```

```text
Ahora divide el resultado por 2
```

---

# 🎯 Learning Objectives

This project was developed to explore:

* AI Agent Design
* Agent Collaboration
* Tool Calling
* Memory and Context
* Prompt Engineering
* Guardrails
* LLM Integration
* Streamlit Applications
* Multi-Agent Architectures

---

# 📄 License

This project is intended for educational and learning purposes.
