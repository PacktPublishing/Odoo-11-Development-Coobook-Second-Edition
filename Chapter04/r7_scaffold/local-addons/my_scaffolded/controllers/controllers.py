# -*- coding: utf-8 -*-
from odoo import http

# class MyScaffolded(http.Controller):
#     @http.route('/my_scaffolded/my_scaffolded/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_scaffolded/my_scaffolded/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_scaffolded.listing', {
#             'root': '/my_scaffolded/my_scaffolded',
#             'objects': http.request.env['my_scaffolded.my_scaffolded'].search([]),
#         })

#     @http.route('/my_scaffolded/my_scaffolded/objects/<model("my_scaffolded.my_scaffolded"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_scaffolded.object', {
#             'object': obj
#         })