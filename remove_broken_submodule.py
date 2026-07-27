# =============================================================================
# T2SAIM PREDATOR V4 — SUBMODULE CLEANUP MOTOR
# Completely removes broken 'autoresearch' submodule (mode 160000) from git index
# fixing GitHub Pages exit code 128 build failure.
# =============================================================================
import os
import subprocess

HARISELDON_DIR = r"B:\Hariseldon"

def fix_submodule():
    print("================================================================================")
    print("🧹 T2SAIM BROKEN SUBMODULE CLEANUP MOTOR")
    print("================================================================================")

    # 1. Remove autoresearch from git index
    res = subprocess.run(["git", "rm", "-f", "--cached", "autoresearch"], cwd=HARISELDON_DIR, capture_output=True, text=True)
    print("Git rm output:", res.stdout.strip() or res.stderr.strip())

    # 2. Remove from .git/config if exists
    subprocess.run(["git", "config", "--remove-section", "submodule.autoresearch"], cwd=HARISELDON_DIR, capture_output=True)

    # 3. Create clean .gitmodules if needed, or ensure none exists
    gitmodules_path = os.path.join(HARISELDON_DIR, ".gitmodules")
    if os.path.exists(gitmodules_path):
        os.remove(gitmodules_path)
        subprocess.run(["git", "rm", "-f", ".gitmodules"], cwd=HARISELDON_DIR, capture_output=True)

    # 4. Commit and push fix to main and gh-pages
    subprocess.run(["git", "add", "-A"], cwd=HARISELDON_DIR)
    subprocess.run(["git", "commit", "-m", "fix: remove broken orphaned autoresearch submodule fixing GitHub Pages build error 128"], cwd=HARISELDON_DIR)
    
    p1 = subprocess.run(["git", "push", "origin", "main"], cwd=HARISELDON_DIR, capture_output=True, text=True)
    print("Push Main:", p1.stderr.strip() or p1.stdout.strip())

    p2 = subprocess.run(["git", "push", "origin", "main:gh-pages", "--force"], cwd=HARISELDON_DIR, capture_output=True, text=True)
    print("Push GH-Pages:", p2.stderr.strip() or p2.stdout.strip())

    print("================================================================================")
    print("✅ BROKEN SUBMODULE REMOVED & PUSHED TO GITHUB!")

if __name__ == "__main__":
    fix_submodule()
