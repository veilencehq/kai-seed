# ~/kai/core/environment.py

import os
from dotenv import load_dotenv

def load_environment(env_path=".env"):
    if os.path.exists(env_path):
        load_dotenv(env_path)
    else:
        print(f"[⚠️] .env file not found at {env_path}")

def get_env_var(key, default=None):
    return os.getenv(key, default)
