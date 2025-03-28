# LLM + RAG Based Dynamic Automation System

A Python-based API service that uses **LLM-powered Retrieval-Augmented Generation (RAG)** to dynamically map user prompts to predefined or user-defined automation functions, generate executable code, and return it through a REST API.

---

## Key Features

-  **Semantic prompt interpretation** using vector embeddings
-  **Predefined + custom automation functions** (e.g., open apps, monitor system)
-  **RAG-powered function retrieval** using FAISS + Sentence Transformers
-  **Dynamic code generation** for invoking matched functions
-  **FastAPI-based API** to expose `/execute` and `/register` endpoints
-  **Execution logging** using JSONL files
-  **Extensible architecture** (e.g., add new utilities, commands, etc.)

---

## Project Structure & File Responsibilities

| File Name                  | Purpose                                                                 |
|----------------------------|-------------------------------------------------------------------------|
| `automation_functions.py` | Built-in automation functions (e.g., open Chrome, check CPU)            |
| `custom_functions.py`     | Stores dynamically registered user-defined functions                    |
| `function_metadata.py`    | Initial metadata for predefined functions (name, description, category) |
| `build_vector_store.py`   | Builds FAISS vector index + stores metadata using Sentence Transformers |
| `retriever.py`            | Retrieves best-matching function from prompt using vector search        |
| `code_generator.py`       | Generates Python code to invoke matched function                        |
| `register.py`             | Handles registering new functions, saving logic, and updating index     |
| `main_api.py`             | FastAPI app exposing `/execute` and `/register` endpoints               |
| `logger.py`               | Logs prompt → function match details into `execution_log.jsonl`         |
| `inspect_metadata.py`     | (Debug) Inspect current `function_metadata.pkl` entries                 |
| `inspect_faiss.py`        | (Debug) Inspect current FAISS index entries                             |

---

##  Sequence of Implementation

### 1. **Define Automation Functions**
Create `automation_functions.py` with built-in functions like:
- `open_chrome()`
- `get_cpu_usage()`
- `run_shell_command()`

### 2. **Create Initial Metadata**
In `function_metadata.py`, define metadata describing each function for semantic search.

### 3. **Build Vector Store**
Run:
```bash
python build_vector_store.py
```
This:
- Generates embeddings from descriptions
- Saves them into `functions.index`
- Saves metadata into `function_metadata.pkl`

### 4. **Implement Retrieval Logic**
Use `retriever.py` to:
- Convert user prompt to embedding
- Query FAISS
- Retrieve top-matching function

### 5. **Generate Python Code**
Use `code_generator.py` to generate a Python script from the matched function name.

### 6. **Run FastAPI Server**
Launch the service via:

```bash
uvicorn main_api:app --reload
```

Endpoints:
- `POST /execute` — provide a prompt to get the matching function and code
- `POST /register` — add new functions on the fly

### 7. **Register New Functions Dynamically**
Use `register.py` logic via the `/register` endpoint:
- Appends function to `custom_functions.py`
- Adds metadata and rebuilds FAISS index

### 8. **Log Everything**
All executions are logged into `logs/execution_log.jsonl` with:
- Timestamp
- Prompt
- Matched function
- Status
- Error (if any)

### 9. **(Optional Debug) Inspect Internals**
- Run `inspect_metadata.py` to list all function metadata
- Run `inspect_faiss.py` to inspect FAISS index count and embeddings

---

## Required Packages

Install all dependencies via:

```bash
pip install fastapi uvicorn sentence-transformers faiss-cpu pydantic numpy psutil
```

---

##  Example Usage

### Register a Function
```json
POST /register
{
  "name": "get_current_datetime",
  "description": "Returns the current date and time.",
  "category": "Date and Time Utilities",
  "logic": "import datetime\nnow = datetime.datetime.now()\nreturn now.strftime('%Y-%m-%d %H:%M:%S')"
}
```

### Execute a Prompt
```json
POST /execute
{
  "prompt": "What is the current time?"
}
```

Response:
```json
{
  "function": "get_current_datetime",
  "code": "from custom_functions import get_current_datetime\n..."
}
```
### Register `open_notepad`

```json
{
  "name": "open_notepad",
  "description": "Opens the Notepad text editor. Also matches: launch notepad, start notepad app, open text editor.",
  "category": "Application Control",
  "logic": "import os\nos.system('notepad')"
}
```

**Prompt to Execute:**
```json
{
  "prompt": "Launch Notepad"
}
```

---

##  Screenshots 

Below are sample screenshots for reference:
### Initial Loaded Page
![WhatsApp Image 2025-03-28 at 11 17 43_3004c560](https://github.com/user-attachments/assets/4d7e1208-d3a3-45cb-a91d-54da772ba92f)

### Docs Page
![WhatsApp Image 2025-03-28 at 11 19 02_d1711589](https://github.com/user-attachments/assets/89bf30aa-a5a5-4600-88db-9e55020070c2)

## Examples

### 1. get_current_datetime
#### /register part
![WhatsApp Image 2025-03-28 at 17 36 15_20eb3ba0](https://github.com/user-attachments/assets/7f7fa541-6439-43b4-af3f-1e1dbbe4327a)
![WhatsApp Image 2025-03-28 at 17 36 46_8c8692e9](https://github.com/user-attachments/assets/f66ce0de-ba19-481e-b50f-ef06219e6e3a)

#### /execute part
![WhatsApp Image 2025-03-28 at 17 39 32_8b72735c](https://github.com/user-attachments/assets/d7e589c1-6ac4-4c2f-aada-649f95ca509a)
![WhatsApp Image 2025-03-28 at 17 39 57_e28c88e3](https://github.com/user-attachments/assets/3a5ef1e5-b65c-4af6-a920-a4701da37437)

#### The code generated in the /execute part is run, and it generates the desired output:
![WhatsApp Image 2025-03-28 at 17 40 43_35fd09c7](https://github.com/user-attachments/assets/feb98659-bfce-4a92-9e73-e8940377e87b)

### 2. Launch Notepad
#### /register part
![WhatsApp Image 2025-03-28 at 19 39 03_495e601d](https://github.com/user-attachments/assets/a3fc9733-0c91-498f-966f-a230b38e8f72)
![WhatsApp Image 2025-03-28 at 19 39 23_c629cec3](https://github.com/user-attachments/assets/bba605f2-46fe-41a1-a6fc-3e6c8d2d38e6)

#### /execute part
![WhatsApp Image 2025-03-28 at 19 39 53_741d42ef](https://github.com/user-attachments/assets/6d892f52-f91a-4afd-ab4c-e5122a79f5fb)
![WhatsApp Image 2025-03-28 at 19 40 13_43541b2d](https://github.com/user-attachments/assets/d1f9b850-1a01-499b-9eed-966e0c47e6de)

#### Generated code is run, and it opens the Notepad:
![WhatsApp Image 2025-03-28 at 19 42 21_7f568d4b](https://github.com/user-attachments/assets/11364be6-f27c-4bf6-abbe-cb730bba983c)

---

