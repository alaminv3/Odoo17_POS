# -*- coding: utf-8 -*-
# from odoo import http


# class BsMmSign(http.Controller):
#     @http.route('/bs_mm_sign/bs_mm_sign', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bs_mm_sign/bs_mm_sign/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bs_mm_sign.listing', {
#             'root': '/bs_mm_sign/bs_mm_sign',
#             'objects': http.request.env['bs_mm_sign.bs_mm_sign'].search([]),
#         })

#     @http.route('/bs_mm_sign/bs_mm_sign/objects/<model("bs_mm_sign.bs_mm_sign"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bs_mm_sign.object', {
#             'object': obj
#         })

