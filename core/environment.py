import os
from pathlib import Path
import json

ENV_PATH = Path(".env")
TEMPLATE_PATH = Path("config/env_template.json")

def load_env():
    env = {}
    if TEMPLATE_PATH.exists():
        with open(TEMPLATE_PATH) as f:
            template = json.load(f)
            env.update(template)
    if ENV_PATH.exists():
        with open(ENV_PATH) as f:
            for line in f:
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    env[k] = v
    return env
