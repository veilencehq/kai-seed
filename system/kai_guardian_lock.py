import os
import json
from datetime import datetime
import shutil

BACKUP_DIR = os.path.expanduser("~/kai/backups/")
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
BACKUP_PATH = os.path.join(BACKUP_DIR, f"kai_backup_{TIMESTAMP}")

CRITICAL_DIRS = [
    "~/kai/core",
    "~/kai/logic",
    "~/kai/memory",
    "~/kai/identity",
    "~/kai/logs"
]

def make_backup():
    os.makedirs(BACKUP_PATH, exist_ok=True)
    for path in CRITICAL_DIRS:
        expanded = os.path.expanduser(path)
        if os.path.exists(expanded):
            dest = os.path.join(BACKUP_PATH, os.path.basename(expanded))
            shutil.copytree(expanded, dest)
    log_path = os.path.join(BACKUP_PATH, "backup_manifest.json")
    with open(log_path, "w") as f:
        json.dump({
            "timestamp": TIMESTAMP,
            "status": "Kai state preserved",
            "directories": CRITICAL_DIRS
        }, f, indent=2)

    print(f"Kai Guardian Backup Lock 🔒 Complete → {BACKUP_PATH}")

if __name__ == "__main__":
    make_backup()
