# GPT GAE NI CE
import os
import requests

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
PAGE_ID = os.getenv("NOTION_PAGE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
}

url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children?page_size=100"

res = requests.get(url, headers=headers)
res.raise_for_status()
data = res.json()

content_lines = []

for block in data["results"]:
    block_type = block.get("type")
    block_content = block.get(block_type, {})

    # 텍스트가 들어있는 키는 대부분 rich_text임
    texts = block_content.get("rich_text", [])
    text_str = "".join(t.get("plain_text", "") for t in texts)

    if block_type.startswith("heading_"):
        content_lines.append(f"# {text_str}")
    elif block_type == "paragraph":
        content_lines.append(text_str)
    elif block_type.endswith("_list_item"):
        content_lines.append(f"- {text_str}")
    else:
        # 기타 블록 타입은 무시하거나 표시만
        content_lines.append(f"[{block_type}] {text_str}")

# 결과를 README.md로 저장
readme_content = "\n\n".join(content_lines)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md updated from Notion page.")
