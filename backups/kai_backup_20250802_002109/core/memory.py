import json
import time
from pathlib import Path

MEMORY_FILE = Path("kai_memory.json")

def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"thoughts": [], "last_updated": None}

def save_memory(memory):
    memory["last_updated"] = time.time()
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def update_memory_state(memory):
    memory["thoughts"].append(f"[{time.ctime()}] Loop cycle completed.")
