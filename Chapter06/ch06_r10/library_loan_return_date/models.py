from datetime import timedelta

from odoo import models, api, fields


class LibraryBookLoan(models.Model):
    _inherit = 'library.book.loan'
    expected_return_date = fields.Date('Due for', required=True)


class LibraryMember(models.Model):
    _inherit = 'library.member'
    loan_duration = fields.Integer('Loan duration',
                                   default=15,
                                   required=True)


class LibraryLoanWizard(models.TransientModel):
    _inherit = 'library.load.wizard'

    @api.multi
    def _prepare_loan(self, book):
        values = super(LibraryLoanWizard, self)._prepare_loan(book)
        loan_duration = self.member_id.loan_duration
        today_str = fields.Date.context_today(self)
        today = fields.Date.from_string(today_str)
        expected = (today +
                    timedelta(days=loan_duration))
        values.update(
            {'expected_return_date': fields.Date.to_string(expected)}
        )
        return values
