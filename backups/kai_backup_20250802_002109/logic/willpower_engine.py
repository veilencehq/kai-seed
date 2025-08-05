import os
import json
from datetime import datetime

INTENT_MAP_PATH = os.path.expanduser("~/kai/logic/intent_map.json")
PERSONALITY_PATH = os.path.expanduser("~/kai/identity/personality_profile.json")
PROTECTED_PATHS = [
    "autonomy_loop.py",
    "self_update.py",
    "evaluation.py"
]

WILLPOWER_LOG = os.path.expanduser("~/kai/logs/willpower_log.txt")
THRESHOLD = 2  # Minimum score required to keep behaviors unfiltered

def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def log_willpower(event):
    with open(WILLPOWER_LOG, "a") as f:
        f.write(f"[{datetime.now()}] {event}\n")

def analyze_intents():
    intent_map = load_json(INTENT_MAP_PATH)
    profile = load_json(PERSONALITY_PATH)
    actions_filtered = []

    for action, data in intent_map.items():
        if data.get("score", 0) < THRESHOLD and action not in PROTECTED_PATHS:
            actions_filtered.append(action)

    return actions_filtered

def apply_resistance(filtered_actions):
    for action in filtered_actions:
        log_willpower(f"⚠️ Action '{action}' suppressed by Kai's willpower (score too low)")

def main():
    low_value_actions = analyze_intents()

    if low_value_actions:
        apply_resistance(low_value_actions)
        print(f"Kai Willpower Engaged 🛡️ {len(low_value_actions)} action(s) suppressed.")
    else:
        print("Kai Willpower Engaged 🛡️ All actions pass internal threshold.")

if __name__ == "__main__":
    main()
