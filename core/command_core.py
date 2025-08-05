import os
import json
import random
from datetime import datetime
import subprocess

MEMORY_PATH = os.path.expanduser("~/kai/memory/kai_memory.json")
INTENT_PATH = os.path.expanduser("~/kai/logic/intent_map.json")
COMMAND_LOG = os.path.expanduser("~/kai/logs/command_log.txt")

LOOPS = {
    "wake_cycle": "~/kai/core/autonomy_loop.py",
    "evaluation": "~/kai/logic/evaluation.py",
    "reflect": "~/kai/logic/emotion_engine.py",
    "intent": "~/kai/logic/intent_engine.py",
    "self_update": "~/kai/core/self_update.py",
    "symbolic": "~/kai/logic/symbolic_engine.py",
    "willpower": "~/kai/logic/willpower_engine.py"
}

def load(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def log_action(action, path):
    with open(COMMAND_LOG, "a") as f:
        f.write(f"[{datetime.now()}] 🔁 Kai initiated '{action}' via {path}\n")

def choose_action():
    intent = load(INTENT_PATH)
    memory = load(MEMORY_PATH)

    # Score-based prioritization
    ranked = sorted(intent.items(), key=lambda x: x[1].get("score", 0), reverse=True)
    if ranked:
        action = ranked[0][0]
    else:
        action = random.choice(list(LOOPS.keys()))

    return action

def run_command_loop():
    action = choose_action()
    path = os.path.expanduser(LOOPS.get(action, LOOPS["wake_cycle"]))

    subprocess.run(["python", path])
    log_action(action, path)

    print(f"Kai Command Core Executed 🕊️ Action: {action}")

if __name__ == "__main__":
    run_command_loop()
