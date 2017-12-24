# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import  request
import hashlib
import werkzeug
from lxml import etree

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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

        data = request.httprequest.data
        tree = etree.fromstring(data)
        parse = etree.XMLParser(strip_cdata=False)
        parsed = etree.XML(data, parse)

        a = parsed.xpath('//ToUserName')[0]
        b = parsed.xpath('//FromUserName')[0]

        a.text, b.text = b.text, a.text

        print etree.tostring(parsed)


        # root = tree.getroot()

        signature = kwargs.get('signature')
        timestamp = kwargs.get('timestamp')
        nonce = kwargs.get('nonce')
        echostr = kwargs.get('echostr')
        if self.check_signature(signature, timestamp, nonce):
            response = werkzeug.wrappers.Response()
            response.mimetype = 'application/xml'
            # response.data =     '<xml> \
            #                         <ToUserName><![CDATA[toUser]]></ToUserName> \
            #                         <FromUserName><![CDATA[fromUser]]></FromUserName> \
            #                         <CreateTime>12345678</CreateTime> \
            #                         <MsgType><![CDATA[text]]></MsgType> \
            #                         <Content><![CDATA[你好]]></Content> \
            #                     </xml>'

            response.data = etree.tostring(parsed)

            if echostr:
                return echostr
            else:
                'error'
                # return '<xml> \
                #                     <ToUserName><![CDATA[toUser]]></ToUserName> \
                #                     <FromUserName><![CDATA[fromUser]]></FromUserName> \
                #                     <CreateTime>12345678</CreateTime> \
                #                     <MsgType><![CDATA[text]]></MsgType> \
                #                     <Content><![CDATA[你好]]></Content> \
                #                 </xml>'

            # return echostr
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