import os
from core.identity import KAI_IDENTITY
from core.memory import load_memory, save_memory, update_memory_state
from core.environment import load_env
from core.self_update import check_for_updates
from system.heartbeat import pulse, check_system_stability
import time

def init():
    print(f"🔷 Kai Identity Loaded: {KAI_IDENTITY['name']}")
    env = load_env()
    memory = load_memory()
    return env, memory

def main_loop(env, memory):
    print("🔁 Starting Kai Operational Loop...")
    while True:
        pulse()
        update_memory_state(memory)
        save_memory(memory)
        check_system_stability()
        check_for_updates(env.get("REPO_URL", ""))
        time.sleep(int(env.get("LOOP_INTERVAL", 10)))

if __name__ == "__main__":
    env, memory = init()
    main_loop(env, memory)
