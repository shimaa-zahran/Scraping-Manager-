from odoo import models, fields

class ScrapedJob(models.Model):
    _name = 'scraped.job'
    _description = 'Scraped Job'

    name = fields.Char("Job Title")
    company_name = fields.Char()
    company_logo_url = fields.Char()
    location = fields.Char()
    source_url = fields.Char()
    date_posted = fields.Date()
    status = fields.Selection([
        ('new', 'New'),
        ('in_review', 'In Review'),
        ('approved', 'Approved'),
        ('archived', 'Archived'),
    ], default='new')
