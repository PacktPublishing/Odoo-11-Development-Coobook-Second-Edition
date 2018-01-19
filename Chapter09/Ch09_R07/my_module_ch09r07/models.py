from odoo import models, api, fields, tools


class LibraryBookLoanStatistics(models.Model):
    _name = 'library.book.loan.statistics'
    _auto = False

    book_id = fields.Many2one('library.book', 'Book', readonly=True)
    loan_id = fields.Many2one('library.book.loan', 'Loan', readonly=True)
    author_id = fields.Many2one('res.partner', 'Author', readonly=True)
    reader_id = fields.Many2one('library.member', 'Reader', readonly=True)
    reader_age = fields.Integer(
        'Reader age', readonly=True,
        group_operator='avg',
        help="the age of the reader when he borrowed the book"
    )

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        query = """
        CREATE OR REPLACE VIEW library_book_loan_statistics AS (
        SELECT
            loan_id+author.res_partner_id*(SELECT MAX(id) FROM library_book_loan)
                AS id,
            loan.book_id AS book_id,
            loan.id AS loan_id,
            author.res_partner_id AS author_id,
            reader.id AS reader_id,
            EXTRACT(YEAR FROM age(loan.create_date, reader.date_of_birth))
                AS reader_age
        FROM library_book_loan AS loan
        JOIN library_book AS book ON (loan.book_id = book.id)
        JOIN library_book_res_partner_rel AS author
            ON (book.id = author.library_book_id)
        JOIN library_member as reader ON (loan.member_id = reader.id)
        )
        """
        self.env.cr.execute(query)
