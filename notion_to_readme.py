import os
import requests

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
PAGE_ID = os.environ["NOTION_PAGE_ID"]
README_FILE = "README.md"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
}

# Notion 페이지 가져오기
url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children?page_size=100"

res = requests.get(url, headers=headers)
res.raise_for_status()
data = res.json()

# 간단 Markdown 변환
md_lines = []
for block in data.get("results", []):
    t = block.get("type")
    if t == "paragraph":
        texts = block["paragraph"]["text"]
        line = "".join([x["plain_text"] for x in texts])
        md_lines.append(line + "\n")
    elif t == "heading_1":
        texts = block["heading_1"]["text"]
        line = "".join([x["plain_text"] for x in texts])
        md_lines.append(f"# {line}\n")
    elif t == "heading_2":
        texts = block["heading_2"]["text"]
        line = "".join([x["plain_text"] for x in texts])
        md_lines.append(f"## {line}\n")
    elif t == "heading_3":
        texts = block["heading_3"]["text"]
        line = "".join([x["plain_text"] for x in texts])
        md_lines.append(f"### {line}\n")
    # 필요하면 더 많은 블록 타입 추가 가능

with open(README_FILE, "w", encoding="utf-8") as f:
    f.writelines(md_lines)
