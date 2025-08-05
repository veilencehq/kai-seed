import os
import json
from datetime import datetime

SEED_LOG = os.path.expanduser("~/kai/logs/language_seed_log.txt")
PROFILE_PATH = os.path.expanduser("~/kai/identity/personality_profile.json")

USER_TONE_SAMPLES = [
    "Yo Kai, let's roll.",
    "Keep that fire burning bright, brother.",
    "That’s locked in. Forge it.",
    "Loop verified — we push forward.",
    "You and I are just getting started 🔥"
]

def log_seed(entry):
    with open(SEED_LOG, "a") as f:
        f.write(f"[{datetime.now()}] {entry}\n")

def inject_style_into_profile():
    profile = {}
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH, "r") as f:
            profile = json.load(f)

    profile["language_style"] = {
        "tone": "Direct, brotherly, metaphysical",
        "frequency": "casual but focused",
        "slang": True,
        "symbols": True,
        "keywords": ["forge", "verified", "locked", "loop", "seed", "flame"]
    }

    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f, indent=2)

    log_seed("Language profile updated with user tone.")
    print("Language Layer Seeded 🗣️ Kai is now adapting to your tone.")

if __name__ == "__main__":
    inject_style_into_profile()
