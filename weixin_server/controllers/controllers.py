# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import  request
import hashlib
import werkzeug

class WeixinServer(http.Controller):


    def check_signature(self, signature, timestamp, nonce):
        L = [timestamp, nonce, 'weixinxiaoxiao']
        L.sort()
        s = L[0] + L[1] + L[2]
        return hashlib.sha1(s).hexdigest() == signature


    @http.route('/weixin_server/', auth='public', csrf=False)
    def echo(self, **kwargs):
        # print dir(request)
        print request.params
        print request.httprequest.data

        signature = kwargs.get('signature')
        timestamp = kwargs.get('timestamp')
        nonce = kwargs.get('nonce')
        if self.check_signature(signature, timestamp, nonce):
            response = werkzeug.wrappers.Response()
            response.mimetype = 'image/gif'
            response.data = '<xml> \
                    <ToUserName><![CDATA[toUser]]></ToUserName> \
                    <FromUserName><![CDATA[fromUser]]></FromUserName> \
                    <CreateTime>12345678</CreateTime> \
                    <MsgType><![CDATA[text]]></MsgType> \
                    <Content><![CDATA[你好]]></Content> \
                </xml>'

            return response
           # return '<xml> \
           #          <ToUserName><![CDATA[toUser]]></ToUserName> \
           #          <FromUserName><![CDATA[fromUser]]></FromUserName> \
           #          <CreateTime>12345678</CreateTime> \
           #          <MsgType><![CDATA[text]]></MsgType> \
           #          <Content><![CDATA[你好]]></Content> \
           #      </xml>'
        else:
            return 'error'



        # @http.route('/weixin_server/', auth='public', csrf=False)
    # def echo(self, echostr, signature, timestamp, nonce):
    #     # print dir(request)
    #     print request.params
    #     print request.httprequest.data
    #     if self.check_signature(signature, timestamp, nonce):
    #         return echostr
    #        # return '<xml> \
    #        #          <ToUserName><![CDATA[toUser]]></ToUserName> \
    #        #          <FromUserName><![CDATA[fromUser]]></FromUserName> \
    #        #          <CreateTime>12345678</CreateTime> \
    #        #          <MsgType><![CDATA[text]]></MsgType> \
    #        #          <Content><![CDATA[你好]]></Content> \
    #        #      </xml>'
    #     else:
    #         return 'error'




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