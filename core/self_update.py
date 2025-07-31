import os
import subprocess

def check_for_updates(repo_url):
    if not repo_url:
        print("🚫 No REPO_URL provided. Skipping update.")
        return
    print("🔄 Checking for updates...")
    try:
        subprocess.run(["git", "pull", repo_url], check=True)
    except subprocess.CalledProcessError:
        print("⚠️ Failed to pull latest updates.")
