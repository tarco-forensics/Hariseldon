import re

with open('B:/Hariseldon/dashboards/betting_analyzer.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = re.compile(r'(<div class="code-block code-block-tabbed".*?<button class="copy-btn"[^>]*>Kopyala</button>).*?(</div>\s*</div>\s*<div id="tab)', re.DOTALL)
replacement = r'\1\n<div style="padding:40px; text-align:center; color:#ef4444; border:1px dashed #ef4444; margin:20px;">\n<br/><strong>[ T2SAIM PROTOCOL: PROPRIETARY FORMULA REDACTED ]</strong><br/><br/>Bu algoritma blogu (Arbitraj, EV, Kelly, vb.) gizlilik protokolleri geregi yayindan kaldirilmistir.<br/>Sadece ANA KOMUTANLIK erisimine aciktir.<br/><br/></div>\n\2'

html = pattern.sub(replacement, html)

# Handle the last tab which might not be followed by <div id="tab
pattern2 = re.compile(r'(<div class="code-block code-block-tabbed".*?<button class="copy-btn"[^>]*>Kopyala</button>).*?(</div>\s*</div>\s*<div class="card")', re.DOTALL)
html = pattern2.sub(replacement, html)


with open('B:/Hariseldon/dashboards/betting_analyzer.html', 'w', encoding='utf-8') as f:
    f.write(html)
