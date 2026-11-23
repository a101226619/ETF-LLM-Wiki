from pathlib import Path
import re,sys,json
root=Path(__file__).resolve().parents[1]
raw=list((root/'raw').glob('S*.md'))
html=(root/'slides/index.html').read_text(encoding='utf-8')
checks={
 '至少5份來源摘要':len(raw)>=5,
 '每份來源有官方網址':all('https://' in x.read_text(encoding='utf-8') for x in raw),
 '至少5個wiki主題':len(list((root/'wiki/topics').glob('*.md')))>=5,
 '12頁簡報':html.count('"title":')==12,
 '每頁具來源ID':html.count('"refs":')==12,
 '基本HTML標記':'<!doctype html>' in html.lower(),
 '互動程式存在':(root/'slides/app.js').exists(),
 '樣式檔存在':(root/'slides/style.css').exists(),
 '測驗邏輯存在':'data-answer' in (root/'slides/app.js').read_text(encoding='utf-8'),
 '來源索引存在':(root/'wiki/index.md').exists(),
}
for k,v in checks.items():print(('PASS' if v else 'FAIL')+' '+k)
print(f'{sum(checks.values())}/{len(checks)} passed')
sys.exit(0 if all(checks.values()) else 1)
