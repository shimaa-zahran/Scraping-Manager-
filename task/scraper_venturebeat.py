import requests
from bs4 import BeautifulSoup
import json


def scrape_venturebeat_about():
    url = "https://venturebeat.com/about/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    main_content = soup.select_one("article.page .entry-content")

    if not main_content:
        print("⚠️ Content not found.")
        return

    paragraphs = main_content.find_all(["p", "ul", "ol"])
    text_blocks = []

    for tag in paragraphs:
        if tag.name == "p":
            text_blocks.append(tag.get_text(strip=True))
        elif tag.name in ["ul", "ol"]:
            items = [li.get_text(strip=True) for li in tag.find_all("li")]
            text_blocks.extend(items)

    full_text = "\n".join(text_blocks)

    data = [{
        "title": "About VentureBeat",
        "source_url": url,
        "summary": text_blocks[0] if text_blocks else "",
        "content": full_text,
        "date_published": ""  # No date on static pages
    }]

    with open("venturebeat_about.json", "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Scraped VentureBeat About page successfully.")


if __name__ == "__main__":
    scrape_venturebeat_about()
