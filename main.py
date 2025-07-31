from core.memory import load_memory, save_memory, update_memory_state
from system.heartbeat import pulse, check_system_stability
import time

def main_loop():
    print("🧠 Kai loop initiated...")
    memory = load_memory()

    while True:
        pulse()
        update_memory_state(memory)
        save_memory(memory)
        check_system_stability()
        time.sleep(10)
