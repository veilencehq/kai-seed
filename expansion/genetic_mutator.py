import os
import random
import json
import shutil
from datetime import datetime

CORE_DIR = os.path.expanduser("~/kai/core")
MUTATION_DIR = os.path.expanduser("~/kai/expansion/mutants")
LOG_PATH = os.path.expanduser("~/kai/logs/genetic_mutator_log.json")

os.makedirs(MUTATION_DIR, exist_ok=True)

def load_log():
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            return json.load(f)
    return {}

def save_log(data):
    with open(LOG_PATH, "w") as f:
        json.dump(data, f, indent=2)

def mutate_line(line):
    if "# MUTATE" in line and "True" in line:
        return line.replace("True", "False")
    elif "# MUTATE" in line and "False" in line:
        return line.replace("False", "True")
    return line

def simulate_mutation():
    logs = load_log()
    timestamp = str(datetime.now())
    mutant_batch = []

    for fname in os.listdir(CORE_DIR):
        if fname.endswith(".py") and "self_update" not in fname:
            src_path = os.path.join(CORE_DIR, fname)
            dest_path = os.path.join(MUTATION_DIR, f"{fname}.mutated")

            with open(src_path, "r") as src, open(dest_path, "w") as dst:
                for line in src:
                    dst.write(mutate_line(line))

            mutant_batch.append(fname)

    logs[timestamp] = {
        "mutated_files": mutant_batch,
        "notes": "Boolean flips only (marked with # MUTATE)"
    }

    save_log(logs)

if __name__ == "__main__":
    simulate_mutation()
    print("Kai Mutation Simulation Complete ✅")
