# Scraping-Manager-
This project provides a complete setup to:

- Scrape public web content (LinkedIn jobs, TechCrunch articles, VentureBeat pages)
- Push scraped data into Odoo models via XML-RPC
- Manage and review imported content through a custom Odoo module

---

## ✅ 1. Setup Instructions

### Prerequisites
python scrape_venturebeat_about.py

- Python 3.8+
- Odoo 17+
- PostgreSQL (running with your Odoo instance)
- Odoo development environment set up locally
- Internet access for scraping

### Install Required Python Packages

```bash
pip install requests beautifulsoup4
2. How to Run the Scrapers
python scrape_techcrunch.py
python scraper_linkedin.py
python scrape_venturebeat_about.py


3. How to Push Data to Odoo
A. Edit Configuration in pusher_to_odoo.py
url = "http://localhost:8017"
db = "your_database"
username = "admin"
password = "admin"

B. Run the Push Script
python pusher_to_odoo.py

4. How to Install and Use the Custom Odoo Module
A. Copy the Module into Odoo's Addons Folder
B. Update the App List
In Odoo UI: go to Apps > Update Apps List

C. Install the Module
Search for Scraped Content and click Install.

D. Access Your Data
Use the Odoo menu to find:

Scraping Manager → Jobs

Scraping Manager → Blogs

Scraping Manager → Pages






