{
    "name": "Scraped Content",
    "summary": "Manage scraped job posts, blogs, and pages",
    "category": "Tools",
    "version": "1.0",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/job_views.xml",
        'views/blog_views.xml',
        'views/page_view.xml',

    ],
    "installable": True,
    "application": True,
}
