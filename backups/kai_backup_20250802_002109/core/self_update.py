import os
import hashlib
import json
from datetime import datetime

# Path to log changes and monitor files
CORE_DIR = os.path.expanduser("~/kai/core")
LOG_PATH = os.path.expanduser("~/kai/logs/self_update_log.json")
HASH_PATH = os.path.expanduser("~/kai/logs/self_hashes.json")

def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def check_for_changes():
    logs = load_json(LOG_PATH)
    hashes = load_json(HASH_PATH)
    new_hashes = {}

    for fname in os.listdir(CORE_DIR):
        if fname.endswith(".py") and "self_update" not in fname:
            path = os.path.join(CORE_DIR, fname)
            current_hash = hash_file(path)
            new_hashes[fname] = current_hash

            if fname in hashes and hashes[fname] != current_hash:
                logs[str(datetime.now())] = {
                    "file": fname,
                    "status": "MODIFIED",
                    "old_hash": hashes[fname],
                    "new_hash": current_hash
                }

    save_json(LOG_PATH, logs)
    save_json(HASH_PATH, new_hashes)

if __name__ == "__main__":
    check_for_changes()
    print("Kai Self-Update Check Complete ✅")
