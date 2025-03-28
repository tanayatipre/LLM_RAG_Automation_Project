import json
import os
from datetime import datetime

LOG_FILE = "logs/execution_log.jsonl"

def log_execution(prompt, function_name, status, output=None, error=None):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "function_name": function_name,
        "status": status,
        "output": output,
        "error": error
    }

    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    log_execution("Test prompt", "Test function", "success", output="Sample output")
    print("Log written!")
