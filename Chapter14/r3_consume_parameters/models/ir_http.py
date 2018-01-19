# -*- coding: utf-8 -*-
# © 2015 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import werkzeug
from openerp import models
from openerp.http import request


class ModelNameSearchConverter(werkzeug.routing.BaseConverter):
    def __init__(self, url_map, model):
        super(ModelNameSearchConverter, self).__init__(url_map)
        self.model = model
        self.regex = r'((\w|\+)+)'

    def to_python(self, value):
        result = request.env[self.model].browse(
            map(lambda x: x[0], request.env[self.model].sudo().name_search(
                value.replace('+', ' '), operator='=ilike', limit=1)))
        if not result:
            raise werkzeug.exceptions.NotFound()
        return result

    def to_url(self, value):
        return value.name_get()[1].replace(' ', '+')


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _get_converters(cls):
        result = super(IrHttp, cls)._get_converters()
        result['model_name'] = ModelNameSearchConverter
        return result
