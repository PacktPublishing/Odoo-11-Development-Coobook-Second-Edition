from odoo import models, fields


class LibraryBookLoan(models.Model):
    _name = 'library.book.loan'
    book_id = fields.Many2one('library.book', 'Book',
                              required=True)
    member_id = fields.Many2one('library.member', 'Borrower',
                                required=True)
    expected_return_date = fields.Date('Due for', required=True)
    state = fields.Selection([('ongoing', 'Ongoing'),
                              ('done', 'Done')],
                             'State',
                             default='ongoing',
                             required=True)
