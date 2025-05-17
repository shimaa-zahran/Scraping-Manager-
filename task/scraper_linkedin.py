import requests
from bs4 import BeautifulSoup
import json

def scrape_linkedin_jobs(query="odoo developer", location="Remote"):

    base_url = "https://www.linkedin.com/jobs/search"
    params = {
        "keywords": query,
        "location": location,
        "trk": "public_jobs_jobs-search-bar_search-submit",
    }

    response = requests.get(base_url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')


    jobs = []
    for job_card in soup.find_all("div", class_="base-card"):
        try:
            title = job_card.find("h3").text.strip()
            company = job_card.find("h4").text.strip()
            img_tag = job_card.find("img")
            logo_url = img_tag.get("src") if img_tag else None

            location = job_card.find("span", class_="job-search-card__location").text.strip()
            link = job_card.find("a", class_="base-card__full-link")["href"]
            date = job_card.find("time")["datetime"] if job_card.find("time") else None

            jobs.append({
                "job_title": title,
                "company_name": company,
                "company_logo_url": logo_url,
                "location": location,
                "source_url": link,
                "date_posted": date
            })
        except Exception as e:
            print(f"Skipping a job card due to error: {e}")

    with open("linkedin_jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)

    print(f"Saved {len(jobs)} job postings to linkedin_jobs.json")

if __name__ == "__main__":
    scrape_linkedin_jobs()
