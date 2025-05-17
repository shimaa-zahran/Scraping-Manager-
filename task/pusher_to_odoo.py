import json
import xmlrpc.client

url = "http://localhost:8017"
db = "TEST6"
username = "admin"
password = "admin"
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common', allow_none=True)
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object', allow_none=True)


uid = common.authenticate(db, username, password, {})




def push_data(json_file, model_name, field_map):
    with open(json_file) as f:
        records = json.load(f)

    for record in records if isinstance(records, list) else [records]:
        data = {}

        for json_field, odoo_field in field_map.items():
            value = record.get(json_field)

            # Skip empty date fields to avoid errors
            if odoo_field == "date_published" and not value:
                continue

            data[odoo_field] = value

        data["status"] = "new"

        try:
            models.execute_kw(db, uid, password, model_name, 'create', [data])
            print(f"✅ Pushed: {data.get('title') or data.get('name')}")
        except Exception as e:
            print(f"❌ Error pushing record: {e}")
# Example usage:
# LinkedIn Jobs
push_data("linkedin_jobs.json", "scraped.job", {
    "job_title": "name",
    "company_name": "company_name",
    "company_logo_url": "company_logo_url",

    "location": "location",
    "source_url": "source_url",
    "date_posted": "date_posted"
})

# TechCrunch Blogs
push_data("techcrunch_blogs.json", "scraped.blog", {
    "title": "title",

    "source_url": "source_url",
    "date_published": "date_published"
})

# VentureBeat Static Page
push_data("venturebeat_about.json", "scraped.page", {
    "title": "title",
    "content": "content",
    "source_url": "source_url"
})
