# -*- coding: utf-8 -*-
from odoo import http

# class WeixinServer(http.Controller):
#     @http.route('/weixin_server/weixin_server/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/weixin_server/weixin_server/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('weixin_server.listing', {
#             'root': '/weixin_server/weixin_server',
#             'objects': http.request.env['weixin_server.weixin_server'].search([]),
#         })

#     @http.route('/weixin_server/weixin_server/objects/<model("weixin_server.weixin_server"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('weixin_server.object', {
#             'object': obj
#         })