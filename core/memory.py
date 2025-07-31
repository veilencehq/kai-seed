import json
from pathlib import Path

MEMORY_FILE = Path("memory.json")

def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    else:
        default_memory = {"thoughts": [], "goals": []}
        save_memory(default_memory)
        return default_memory

def save_memory(data):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=4)
