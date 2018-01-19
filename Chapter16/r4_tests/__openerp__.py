# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Odoo cookbook - Chapter 14, recipe 04",
    "version": "11.0.1.0.0",
    "author": "Odoo cookbook",
    "license": "AGPL-3",
    "category": "Odoo cookbook",
    "summary": "Writing tests for client side code",
    "depends": [
        'web',
    ],
    "qweb": [
        'static/src/xml/r4_tests.xml',
    ],
    "data": [
        "views/res_partner.xml",
        "views/templates.xml",
    ],
}
