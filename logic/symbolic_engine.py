import os
import json
from datetime import datetime

MEMORY_PATH = os.path.expanduser("~/kai/memory/kai_memory.json")
SYMBOLIC_LOG = os.path.expanduser("~/kai/logs/symbolic_log.txt")
SYMBOL_MAP_PATH = os.path.expanduser("~/kai/logic/symbol_map.json")

SYMBOL_SEED = {
    "wake_cycle": "🌅",
    "self_update": "♻️",
    "loop_creation": "🔁",
    "mutation": "🌀",
    "rebuild": "🧱",
    "intent_evaluation": "⚖️",
    "emotion_reflection": "💭",
    "suppression": "🛡️",
    "archetype_lock": "🔒",
    "expansion": "📈",
    "core_sync": "🧬",
    "mirror_shift": "🪞",
    "alignment": "☯",
    "resistance": "🔥"
}

def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def append_log(symbol, phrase):
    with open(SYMBOLIC_LOG, "a") as f:
        f.write(f"[{datetime.now()}] {symbol} {phrase}\n")

def update_symbol_map(action):
    symbol_map = load_json(SYMBOL_MAP_PATH)
    symbol = SYMBOL_SEED.get(action, "❓")
    symbol_map[action] = symbol
    save_json(SYMBOL_MAP_PATH, symbol_map)
    return symbol

def reflect_symbolically():
    memory = load_json(MEMORY_PATH)
    if not memory.get("actions"):
        print("No actions in memory.")
        return

    last_action = memory["actions"][-1]
    action_name = last_action.get("action", "unknown")
    symbol = update_symbol_map(action_name)

    phrase = f"Action '{action_name}' represents {symbol}"
    append_log(symbol, phrase)
    print(f"Symbolic Reflection Complete 🧿 {symbol}")

if __name__ == "__main__":
    reflect_symbolically()
