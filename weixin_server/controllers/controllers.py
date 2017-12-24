# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import  request
import hashlib

class WeixinServer(http.Controller):


    def check_signature(signature, timestamp, nonce, token):
        L = [timestamp, nonce, token]
        L.sort()
        s = L[0] + L[1] + L[2]
        return hashlib.sha1(s).hexdigest() == signature

    @http.route('/weixin_server/', auth='public')
    def echo(self, signature, timestamp, nonce, token):
        print request
        print signature
        return 'ok'

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