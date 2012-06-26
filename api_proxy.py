#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
web interface to proxy original api access
'''
import web
import urllib2
from weibo import APIClient
from AutoTokenGenerator import AutoTokenGenerator
import WeiboTokenGenerator
import json

urls = (
        '/apiproxy/(.+)/(.+)', 'apiproxy'
        )

_HTTP_GET = 0
_HTTP_POST = 1

def weibo_api(url, method):
    '''
    get avaliable access token to proxy the url request.
    '''
    APP_KEY = '3231340587' # app key
    APP_SECRET = '94c4a0dc3c4a571b796ffddd09778cff' # app secret
    CALLBACK_URL = 'http://120.weibomanager.sinaapp.com/callback.php' # callback url
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    tokenGenerator = AutoTokenGenerator()
#    access_token,expires_in = tokenGenerator.generatorToken(1);
    access_token,expires_in = WeiboTokenGenerator.loginAndGetToken("xeoncode@gmail.com","5845211314");
#    print access_token,expires_in
    client.set_access_token(access_token=access_token,expires_in=expires_in)
    methodResult = getattr(client, url)()
#    encodedResult = str(methodResult).decode("UTF-8")
#    return encodedResult.encode("UTF-8")
    encodedResult = json.dumps(methodResult)
    return encodedResult

platform = {
            'weibo': weibo_api,
            }

app = web.application(urls, globals())

class apiproxy:
    def GET(self, site, proxy_url):
        api = platform.get(site)
        if api:
            return api(proxy_url, _HTTP_GET)
        raise web.HTTPError(404)
    
    def POST(self, site, proxy_url):
        api = platform.get(site)
        if api:
            return api(proxy_url, _HTTP_POST)
        raise web.HTTPError(404)
    
#application = app.wsgifunc()
'''
start debugging server
'''
if __name__ == '__main__':
    app.run()