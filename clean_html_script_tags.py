# =============================================================================
# T2SAIM HTML CLEANUP SCRIPT
# Cleans up duplicate </script> tags and formats embedded data cleanly
# =============================================================================
import os
import re

HARISELDON_DIR = r"B:\Hariseldon"
TARKAN_HTML = os.path.join(HARISELDON_DIR, "tarkan_index.html")

def clean_tarkan_html():
    if not os.path.exists(TARKAN_HTML):
        return

    with open(TARKAN_HTML, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the position of <script> and </html>
    script_idx = content.find("<script>")
    if script_idx == -1:
        return

    html_head = content[:script_idx].strip()
    script_body = content[script_idx:].strip()

    # Remove all </script> occurrences inside script_body except at the very end
    script_body_clean = script_body.replace("</script>", "")
    # Remove extra <script> tags if any
    script_body_clean = script_body_clean.replace("<script>", "")

    final_content = html_head + "\n\n<script>\n" + script_body_clean.strip() + "\n</script>\n</body>\n</html>\n"

    with open(TARKAN_HTML, "w", encoding="utf-8") as f:
        f.write(final_content)

    print(f"✅ Cleaned script tags in {TARKAN_HTML}")

if __name__ == "__main__":
    clean_tarkan_html()
