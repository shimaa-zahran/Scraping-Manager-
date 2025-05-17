import requests
from bs4 import BeautifulSoup
import json
import time

HEADERS = {"User-Agent": "Mozilla/5.0"}
BASE_URL = "https://techcrunch.com"

def scrape_articles():
    """Scrape latest news articles from the TechCrunch homepage"""
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []

    for li in soup.select("li.wp-block-post"):
        title_tag = li.select_one("h3.loop-card__title a")
        image_tag = li.select_one("figure img")


        if not title_tag:
            continue

        article_url = title_tag["href"]


        # Fetch article page
        detail_resp = requests.get(article_url, headers=HEADERS)
        detail_soup = BeautifulSoup(detail_resp.content, "html.parser")

        # Extract content
        content_div = detail_soup.find("div", class_="article-content")
        paragraphs = content_div.find_all("p") if content_div else []

        time_tag = detail_soup.find("time")
        pub_date = time_tag["datetime"] if time_tag and time_tag.has_attr("datetime") else ""

        articles.append({
            "title": title_tag.get_text(strip=True),
            "source_url": article_url,
            "image_url": image_tag["src"] if image_tag else "",

            "date_published": pub_date
        })

        time.sleep(1)  # Be respectful

    return articles

def scrape_topics():
    """Scrape topic links from the TechCrunch mega menu"""
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    topics = []
    for p in soup.select("p.wp-block-techcrunch-mega-menu-link"):
        a = p.find("a")
        if a:
            topic_name = a.get_text(strip=True)
            topic_url = a['href']
            full_url = BASE_URL + topic_url if topic_url.startswith("/") else topic_url
            topics.append({
                "title": topic_name,
                "source_url": full_url,
                "summary": f"TechCrunch topic: {topic_name}",
                "content": "",
                "date_published": ""
            })

    return topics

def scrape_techcrunch():
    print("🔍 Starting TechCrunch scraping...")
    article_data = scrape_articles()
    topic_data = scrape_topics()
    all_data = article_data + topic_data

    with open("techcrunch_blogs.json", "w") as f:
        json.dump(all_data, f, indent=2)

    print(f"✅ Finished scraping. {len(all_data)} total records saved to techcrunch_blogs.json.")

if __name__ == "__main__":
    scrape_techcrunch()
