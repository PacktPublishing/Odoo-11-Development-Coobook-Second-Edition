from odoo import models, api, fields


class SomeModel(models.Model):
    _name = 'some.model'

    @api.multi
    def create_company(self):
        today_str = fields.Date.contex_today()
        val1 = {'name': 'Eric Idel',
                'email': 'eric.idle@example.com',
                'date': today_str,
                }
        val2 = {'name': 'John Cleese',
                'email': 'john.cleese@example.com',
                'date': today_str,
                }
        company_val = {'name': 'Flying Circus',
                       'email': 'm.python@example.com',
                       'date': today_str,
                       'is_company': True,
                       'child_ids': [(0, 0, val1),
                                     (0, 0, val2),
                                     ],
                       }
        record = self.env['res.company'].create(company_val)
        return record
