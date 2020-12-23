# -*- coding: utf-8 -*-
# from odoo import http

# class Openlearn(http.Controller):
#     @http.route('/openlearn/openlearn/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openlearn/openlearn/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openlearn.listing', {
#             'root': '/openlearn/openlearn',
#             'objects': http.request.env['openlearn.openlearn'].search([]),
#         })

#     @http.route('/openlearn/openlearn/objects/<model("openlearn.openlearn"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openlearn.object', {
#             'object': obj
#         })
