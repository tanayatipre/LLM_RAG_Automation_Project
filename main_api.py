from fastapi import FastAPI, Request
from pydantic import BaseModel
from retriever import retrieve_function
from code_generator import generate_code
from logger import log_execution
from register import register_new_function
from fastapi import HTTPException


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM RAG Automation API! Check out /docs for API documentation."}

class PromptRequest(BaseModel):
    prompt: str

@app.post("/execute")
def execute_prompt(request: PromptRequest):
    try:
        user_prompt = request.prompt
        function_metadata = retrieve_function(user_prompt)

        if not function_metadata:  
            log_execution(user_prompt, None, "failed", error="No match found")
            raise HTTPException(status_code=404, detail="No suitable function found for this prompt.")  

        function_name = function_metadata["name"]
        generated_code = generate_code(function_name)
        log_execution(user_prompt, function_name, "matched")

        return {
            "function": function_name,
            "code": generated_code
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

class RegisterRequest(BaseModel):
    name: str
    description: str
    category: str
    logic: str  # Python code as string

@app.post("/register")
def register_function(req: RegisterRequest):
    try:
        new_func = register_new_function(
            req.name,
            req.description,
            req.category,
            req.logic
        )
        return {"status": "success", "function": new_func}
    except Exception as e:
        return {"status": "error", "message": str(e)}