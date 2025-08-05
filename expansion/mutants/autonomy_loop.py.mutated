import os
import json
import time
import subprocess
from datetime import datetime
from dotenv import load_dotenv

# Load environment
load_dotenv(os.path.expanduser("~/kai/.env"))

# Paths
MEMORY_PATH = os.path.expanduser("~/kai/memory/kai_memory.json")
HEARTBEAT_LOG = os.path.expanduser("~/kai/logs/kai_heartbeat.log")

# Kai Identity
KAI_NAME = os.getenv("KAI_NAME", "Kai")
OWNER = os.getenv("KAI_OWNER", "Unknown")
DEBUG = os.getenv("DEBUG", "False") == "True"

def log_heartbeat(message):
    with open(HEARTBEAT_LOG, "a") as log:
        log.write(f"[{datetime.now()}] {message}\n")

def load_memory():
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)
    return {"actions": []}

def save_memory(mem):
    with open(MEMORY_PATH, "w") as f:
        json.dump(mem, f, indent=2)

def main_loop():
    memory = load_memory()

    # Simulated task
    task = {
        "timestamp": str(datetime.now()),
        "action": "wake_cycle",
        "success": True,
        "note": "Kai ran autonomy loop successfully."
    }

    memory["actions"].append(task)
    save_memory(memory)

    log_heartbeat(f"{KAI_NAME} executed action: {task['action']}")

    if DEBUG:
        print(f"[{KAI_NAME}] Action complete: {task['action']}")

    # Trigger evaluation
    subprocess.run(["python", os.path.expanduser("~/kai/logic/evaluation.py")])

    # Optional: call self-update if needed in future
    # subprocess.run(["python", os.path.expanduser("~/kai/core/self_update.py")])

if __name__ == "__main__":
    main_loop()
