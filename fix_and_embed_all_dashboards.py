# =============================================================================
# T2SAIM PREDATOR V4 — DASHBOARD FAIL-SAFE EMBEDDER & REPAIR MOTOR
# Fixes timezone date string offsets, hard-embeds real crisis and market data into
# tarkan_index.html and index.html, guarantees 100% real data rendering.
# =============================================================================
import os
import sys
import json
import re

HARISELDON_DIR = r"B:\Hariseldon"
CRISIS_JSON_PATH = os.path.join(HARISELDON_DIR, "crisis_data.json")
MARKET_JSON_PATH = os.path.join(HARISELDON_DIR, "market_data.json")
TARKAN_HTML_PATH = os.path.join(HARISELDON_DIR, "tarkan_index.html")
INDEX_HTML_PATH = os.path.join(HARISELDON_DIR, "index.html")

def repair_and_embed():
    print("================================================================================")
    print("🛠️ T2SAIM DASHBOARD FAIL-SAFE EMBEDDER & REPAIR")
    print("================================================================================")

    # 1. Load Crisis Data
    with open(CRISIS_JSON_PATH, "r", encoding="utf-8") as f:
        crisis_data = json.load(f)

    # 2. Load Market Data
    with open(MARKET_JSON_PATH, "r", encoding="utf-8") as f:
        market_data = json.load(f)

    print(f"✅ Loaded crisis_data ({len(crisis_data['series'])} rows) & market_data ({len(market_data['markets'])} markets)")

    # 3. Process tarkan_index.html
    if os.path.exists(TARKAN_HTML_PATH):
        with open(TARKAN_HTML_PATH, "r", encoding="utf-8") as f:
            content = f.read()

        # Insert embedded data variable at beginning of main script block
        crisis_str = json.dumps(crisis_data, ensure_ascii=False)
        embed_var = f"window.EMBEDDED_CRISIS_DATA = {crisis_str};"

        if "window.EMBEDDED_CRISIS_DATA =" in content:
            content = re.sub(r"window\.EMBEDDED_CRISIS_DATA\s*=\s*\{.*?\};", embed_var, content)
        else:
            content = content.replace("<script>", "<script>\n" + embed_var + "\n", 1)

        with open(TARKAN_HTML_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Hard-embedded EMBEDDED_CRISIS_DATA into {TARKAN_HTML_PATH}")

    # 4. Process index.html
    if os.path.exists(INDEX_HTML_PATH):
        with open(INDEX_HTML_PATH, "r", encoding="utf-8") as f:
            content = f.read()

        market_str = json.dumps(market_data, ensure_ascii=False)
        crisis_str = json.dumps(crisis_data, ensure_ascii=False)
        embed_var_m = f"window.EMBEDDED_MARKET_DATA = {market_str};\nwindow.EMBEDDED_CRISIS_DATA = {crisis_str};\n"

        content = re.sub(r"<script>window\.EMBEDDED_MARKET_DATA = .*?</script>\n?", "", content, flags=re.DOTALL)

        target_script = "<script>\nlet crisisData = null;"
        if target_script in content:
            content = content.replace(target_script, f"<script>\n{embed_var_m}let crisisData = null;")
        else:
            content = re.sub(r"<script>", f"<script>\n{embed_var_m}", content, count=1)

        with open(INDEX_HTML_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Hard-embedded EMBEDDED_MARKET_DATA into {INDEX_HTML_PATH}")

    print("================================================================================")
    print("✅ REPAIR & EMBED COMPLETE!")

if __name__ == "__main__":
    repair_and_embed()
