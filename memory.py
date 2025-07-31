import json
from pathlib import Path

MEMORY_FILE = Path("kai_memory.json")

def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE) as f:
            return json.load(f)
    return {"thoughts": [], "timestamp": None}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def update_memory_state(memory):
    memory["thoughts"].append("Heartbeat stable, memory looped.")
