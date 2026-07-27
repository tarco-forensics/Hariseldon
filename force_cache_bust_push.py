# =============================================================================
# T2SAIM PREDATOR V4 — FORCE CACHE-BUST & RE-PUSH MOTOR
# Injects cache-busting timestamp into index.html & tarkan_index.html,
# then force pushes to both main and gh-pages branches.
# =============================================================================
import os
import subprocess
import time

HARISELDON_DIR = r"B:\Hariseldon"
INDEX_PATH = os.path.join(HARISELDON_DIR, "index.html")
TARKAN_PATH = os.path.join(HARISELDON_DIR, "tarkan_index.html")
TIMESTAMP = str(int(time.time()))

def cache_bust():
    for path in [INDEX_PATH, TARKAN_PATH]:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            # Insert or replace timestamp comment at top
            if "<!-- CACHE_BUST:" in content:
                import re
                content = re.sub(r"<!-- CACHE_BUST: \d+ -->", f"<!-- CACHE_BUST: {TIMESTAMP} -->", content)
            else:
                content = f"<!-- CACHE_BUST: {TIMESTAMP} -->\n" + content
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Injected cache-bust timestamp ({TIMESTAMP}) into {os.path.basename(path)}")

    # Git add, commit, push to main and gh-pages
    subprocess.run(["git", "add", "index.html", "tarkan_index.html"], cwd=HARISELDON_DIR)
    subprocess.run(["git", "commit", "-m", f"build: force refresh cache bust {TIMESTAMP}"], cwd=HARISELDON_DIR)
    subprocess.run(["git", "push", "origin", "main"], cwd=HARISELDON_DIR)
    res = subprocess.run(["git", "push", "origin", "main:gh-pages", "--force"], cwd=HARISELDON_DIR, capture_output=True, text=True)
    print("GH-Pages Force Push Result:", res.stderr.strip() or res.stdout.strip())

if __name__ == "__main__":
    cache_bust()
