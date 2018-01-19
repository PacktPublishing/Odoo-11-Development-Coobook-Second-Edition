# -*- coding: utf-8 -*-
# © 2015 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import exceptions, models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _auth_method_base_group_user(cls):
        cls._auth_method_user()
        if not request.env.user.has_group('base.group_user'):
            raise exceptions.AccessDenied()

    # this is for the exercise
    @classmethod
    def _auth_method_groups(cls, group_xmlids=None):
        cls._auth_method_user()
        if not any(map(request.env.user.has_group, group_xmlids or [])):
            raise exceptions.AccessDenied()

    @classmethod
    def _authenticate(cls, auth_method='user'):
        if auth_method.startswith('groups(') and auth_method.endswith(')'):
            super(IrHttp, cls)._authenticate(auth_method='user')
            cls._auth_method_groups(
                map(str.strip, auth_method[7:-1].split(','))
            )
            return auth_method
        return super(IrHttp, cls)._authenticate(auth_method=auth_method)
