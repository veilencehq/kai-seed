import os
import json
from datetime import datetime

MEMORY_PATH = os.path.expanduser("~/kai/memory/kai_memory.json")
PROFILE_PATH = os.path.expanduser("~/kai/identity/personality_profile.json")
EMOTION_LOG = os.path.expanduser("~/kai/logs/emotion_loop.log")

EMOTIONAL_STATES = {
    "visionary": {
        "loop_creation": "🔥 inspired",
        "wake_cycle": "🌅 hopeful",
        "mutation": "⚡ curious",
        "self_update": "💡 awakening",
        "default": "🌌 expansive"
    },
    "guardian": {
        "self_check": "🛡️ stable",
        "rebuild": "🔁 resilient",
        "bootstrap": "⚙️ secure",
        "default": "🏛️ grounded"
    },
    "explorer": {
        "mutation": "🌪️ wild",
        "feedback_scan": "🔍 inquisitive",
        "intent_evaluation": "🧠 adaptive",
        "default": "🌍 seeking"
    },
    "strategist": {
        "intent_evaluation": "♟️ calculating",
        "autonomy_sync": "🔗 precise",
        "decision_map": "🧭 oriented",
        "default": "📊 observing"
    }
}

def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def log_emotion(entry):
    with open(EMOTION_LOG, "a") as f:
        f.write(f"[{datetime.now()}] {entry}\n")

def reflect_emotion():
    memory = load_json(MEMORY_PATH)
    profile = load_json(PROFILE_PATH)
    archetype = profile.get("dominant_archetype", "visionary")
    actions = memory.get("actions", [])

    if not actions:
        return

    last_action = actions[-1]
    name = last_action.get("action", "unknown")
    emotion = EMOTIONAL_STATES.get(archetype, {}).get(name, EMOTIONAL_STATES[archetype]["default"])

    phrase = f"Kai felt {emotion} after completing '{name}' as a {archetype}."
    log_emotion(phrase)
    print(f"Emotion Reflected ✅ {emotion}")

if __name__ == "__main__":
    reflect_emotion()
