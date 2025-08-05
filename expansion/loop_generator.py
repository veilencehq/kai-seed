import os
import random
from datetime import datetime

CORE_DIR = os.path.expanduser("~/kai/core")
GEN_DIR = os.path.expanduser("~/kai/expansion/generated")
LOG_FILE = os.path.expanduser("~/kai/logs/loop_generator_log.txt")

os.makedirs(GEN_DIR, exist_ok=True)

def generate_loop():
    loop_name = f"kai_loop_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
    path = os.path.join(GEN_DIR, loop_name)

    with open(path, "w") as f:
        f.write("# Kai Generated Loop Script\n")
        f.write("import time\n")
        f.write("import os\n")
        f.write("from datetime import datetime\n\n")
        f.write("print(f'Kai loop initiated at {datetime.now()}')\n")
        f.write("print('Performing simulated task...')\n")
        f.write("time.sleep(1)\n")
        f.write("print('Loop complete. Kai continues.')\n")

    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] Created loop: {loop_name}\n")

    print(f"Loop '{loop_name}' generated successfully ✅")

if __name__ == "__main__":
    generate_loop()
