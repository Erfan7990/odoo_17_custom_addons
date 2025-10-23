# -*- coding: utf-8 -*-
# from odoo import http


# class CustomWebsite(http.Controller):
#     @http.route('/custom_website/custom_website', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_website/custom_website/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_website.listing', {
#             'root': '/custom_website/custom_website',
#             'objects': http.request.env['custom_website.custom_website'].search([]),
#         })

#     @http.route('/custom_website/custom_website/objects/<model("custom_website.custom_website"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_website.object', {
#             'object': obj
#         })

