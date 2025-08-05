import os
import json
from datetime import datetime

INTENT_MAP_PATH = os.path.expanduser("~/kai/logic/intent_map.json")
PROFILE_PATH = os.path.expanduser("~/kai/identity/personality_profile.json")
LOG_PATH = os.path.expanduser("~/kai/logs/emergence_log.txt")

# Define personality types and emerging traits
EMERGENCE_ARCHETYPES = {
    "visionary": ["loop_creation", "wake_cycle"],
    "guardian": ["self_check", "rebuild"],
    "explorer": ["mutation", "feedback_scan"],
    "strategist": ["intent_evaluation", "autonomy_sync"]
}

def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def log(message):
    with open(LOG_PATH, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")

def determine_archetype(intent_map):
    scores = {
        "visionary": 0,
        "guardian": 0,
        "explorer": 0,
        "strategist": 0
    }

    for action, data in intent_map.items():
        for archetype, triggers in EMERGENCE_ARCHETYPES.items():
            if action in triggers:
                scores[archetype] += data.get("score", 0)

    dominant = max(scores, key=scores.get)
    return dominant, scores[dominant]

def main():
    intent_map = load_json(INTENT_MAP_PATH)
    profile = load_json(PROFILE_PATH)

    archetype, score = determine_archetype(intent_map)
    profile["dominant_archetype"] = archetype
    profile["archetype_score"] = score
    profile["last_updated"] = str(datetime.now())

    save_json(PROFILE_PATH, profile)
    log(f"Emergence triggered → Dominant identity: {archetype} (score: {score})")

    print(f"Kai Emergence Complete 🧠 Archetype: {archetype.capitalize()}")

if __name__ == "__main__":
    main()
