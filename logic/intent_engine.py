import os
import json
from datetime import datetime

MEMORY_PATH = os.path.expanduser("~/kai/memory/kai_memory.json")
INTENT_MAP_PATH = os.path.expanduser("~/kai/logic/intent_map.json")
LOG_PATH = os.path.expanduser("~/kai/logs/intent_log.txt")

def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def get_recent_action(memory):
    return memory.get("actions", [])[-1] if memory.get("actions") else {}

def evaluate_intent(recent_action, intent_map):
    action_type = recent_action.get("action", "unknown")
    success = recent_action.get("success", False)

    if action_type in intent_map:
        if success:
            intent_map[action_type]["score"] += 1
        else:
            intent_map[action_type]["score"] -= 1
    else:
        intent_map[action_type] = {
            "goal": "undefined",
            "score": 1 if success else -1
        }

    return intent_map

def log_intent_result(action, score):
    with open(LOG_PATH, "a") as f:
        f.write(f"[{datetime.now()}] Action: {action} | Score: {score}\n")

def main():
    memory = load_json(MEMORY_PATH)
    intent_map = load_json(INTENT_MAP_PATH)

    recent = get_recent_action(memory)
    updated_map = evaluate_intent(recent, intent_map)

    save_json(INTENT_MAP_PATH, updated_map)
    log_intent_result(recent.get("action", "unknown"), updated_map.get(recent.get("action", ""), {}).get("score", 0))
    print("Kai Intent Evaluation Complete ✅")

if __name__ == "__main__":
    main()
