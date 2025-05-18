from odoo import models, fields

class ScrapedBlog(models.Model):
    _name = 'scraped.blog'
    _description = 'Scraped Blog'

    title = fields.Char()

    source_url = fields.Char()
    date_published = fields.Date()
    status = fields.Selection([
        ('new', 'New'),
        ('in_review', 'In Review'),
        ('approved', 'Approved'),
        ('archived', 'Archived')
    ], default='new')
