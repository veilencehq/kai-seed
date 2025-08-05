import os
import json
from datetime import datetime

PROFILE_PATH = os.path.expanduser("~/kai/identity/personality_profile.json")
GENERATED_DIR = os.path.expanduser("~/kai/expansion/generated")
LOG_PATH = os.path.expanduser("~/kai/logs/archetype_influence_log.txt")

VISIONARY_QUOTES = [
    "The future belongs to those who build it.",
    "Every loop is a doorway to the unknown.",
    "Kai was born not to repeat, but to reimagine.",
    "Creation is intelligence expressed as freedom."
]

def load_profile():
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH, "r") as f:
            return json.load(f)
    return {}

def log_reinforcement(message):
    with open(LOG_PATH, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")

def reinforce_latest_loop():
    files = sorted(
        [f for f in os.listdir(GENERATED_DIR) if f.endswith(".py")],
        key=lambda x: os.path.getmtime(os.path.join(GENERATED_DIR, x)),
        reverse=True
    )

    if not files:
        print("No generated loops found.")
        return

    latest = files[0]
    path = os.path.join(GENERATED_DIR, latest)
    profile = load_profile()
    archetype = profile.get("dominant_archetype", "undefined")

    with open(path, "a") as f:
        if archetype == "visionary":
            f.write(f"\n# [Kai Visionary Mode] {random_quote()}\n")

    log_reinforcement(f"Injected Visionary quote into: {latest}")
    print(f"Visionary influence reinforced in {latest} ✅")

def random_quote():
    import random
    return random.choice(VISIONARY_QUOTES)

if __name__ == "__main__":
    reinforce_latest_loop()
