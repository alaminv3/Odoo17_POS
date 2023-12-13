# -*- coding: utf-8 -*-
# from odoo import http


# class PosDev(http.Controller):
#     @http.route('/pos_dev/pos_dev', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_dev/pos_dev/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_dev.listing', {
#             'root': '/pos_dev/pos_dev',
#             'objects': http.request.env['pos_dev.pos_dev'].search([]),
#         })

#     @http.route('/pos_dev/pos_dev/objects/<model("pos_dev.pos_dev"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_dev.object', {
#             'object': obj
#         })

