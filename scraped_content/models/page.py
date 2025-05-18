from odoo import models, fields

class ScrapedPage(models.Model):
    _name = 'scraped.page'
    _description = 'Scraped Page'

    title = fields.Char()
    content = fields.Text()
    source_url = fields.Char()
    status = fields.Selection([
        ('new', 'New'),
        ('in_review', 'In Review'),
        ('approved', 'Approved'),
        ('archived', 'Archived')
    ], default='new')
