from odoo import models, fields, api


class LibraryMember(models.Model):
    _name = 'library.member'
    _inherit = 'mail.thread'
    name = fields.Char('Name', required=True)
    email = fields.Char('Email address', required=True)
    loan_ids = fields.One2many(
        'library.book.loan', 'member_id', 'Loans',
        domain=[('state', '=', 'ongoing')]
    )
    nb_late_loans = fields.Integer(
        'Late loans',
        compute="_get_late_loans_count",
    )

    @api.depends('loan_ids')
    def _get_late_loans_count(self):
        today = fields.Date.context_today(self)
        for rec in self:
            rec.nb_late_loans = self.env['library.book.loan'].search_count(
                [('member_id', '=', rec.id),
                 ('state', '=', 'ongoing'),
                 ('expected_return_date', '<', today),
                 ]
            )
