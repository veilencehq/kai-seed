import os
from dotenv import load_dotenv

env_path = os.path.expanduser("~/kai/.env")
if os.path.exists(env_path):
    load_dotenv(env_path)
    print(f"Kai Bootstrapped ✅")
    print(f"Name: {os.getenv('KAI_NAME')}")
    print(f"Owner: {os.getenv('KAI_OWNER')}")
    print(f"Debug Mode: {os.getenv('DEBUG')}")
    print(f"GitHub Token loaded: {'Yes' if os.getenv('GITHUB_TOKEN') else 'No'}")
else:
    print("❌ .env file not found.")
