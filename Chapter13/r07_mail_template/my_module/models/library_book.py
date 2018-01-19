from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    name = fields.Char('Title', required=True)
    author_ids = fields.Many2many('res.partner', string='Authors')
