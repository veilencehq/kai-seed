import json
import os
from datetime import datetime

MEMORY_PATH = os.path.expanduser("~/kai/memory/kai_memory.json")
DECISION_MAP_PATH = os.path.expanduser("~/kai/config/kai_decision_map.json")
LOG_PATH = os.path.expanduser("~/kai/logs/kai_heartbeat.log")

def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def evaluate_decisions():
    memory = load_json(MEMORY_PATH)
    decision_map = load_json(DECISION_MAP_PATH)

    history = memory.get("actions", [])[-10:]  # last 10 actions
    feedback_log = []

    for entry in history:
        action = entry.get("action")
        success = entry.get("success", False)

        if action not in decision_map:
            decision_map[action] = {"success": 0, "fail": 0}

        if success:
            decision_map[action]["success"] += 1
        else:
            decision_map[action]["fail"] += 1

        feedback_log.append(f"[{datetime.now()}] Evaluated '{action}' → {'✅' if success else '❌'}")

    save_json(DECISION_MAP_PATH, decision_map)

    # Log results
    with open(LOG_PATH, "a") as log_file:
        for log in feedback_log:
            log_file.write(log + "\n")

if __name__ == "__main__":
    evaluate_decisions()
    print("Kai Feedback Evaluation Complete ✅")
