#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import re
import json
import hashlib
import requests
import urllib

postdata = {
    'entry': 'weibo',
    'gateway': '1',
    'from': '',
    'savestate': '7',
    'userticket': '1',
    'ssosimplelogin': '1',
    'vsnf': '1',
    'vsnval': '',
    'su': '',
    'service': 'miniblog',
    'servertime': '',
    'nonce': '',
    'pwencode': 'wsse',
    'sp': '',
    'encoding': 'UTF-8',
    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
    'returntype': 'META'
}


def __get_servertime():
    '''
            获取服务器时间和nonce随机数
    '''
    url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=dW5kZWZpbmVk&client=ssologin.js(v1.3.22)&_=1338798142642'
    data = requests.get(url).content;
    p = re.compile('\((.*)\)')
    try:
        json_data = p.search(data).group(1)
        data = json.loads(json_data)
        servertime = str(data['servertime'])
        nonce = data['nonce']
        return servertime, nonce
    except:
        print 'Get severtime error!'
        return None

def __get_pwd(pwd, servertime, nonce):
    '''
    password 经过了三次SHA1 加密， 且其中加入了 servertime 和 nonce 的值来干扰。
            即： 两次SHA1加密后， 将结果加上 servertime 和 nonce 的值， 再SHA1 算一次。
    '''
    pwd1 = hashlib.sha1(pwd).hexdigest()
    pwd2 = hashlib.sha1(pwd1).hexdigest()
    pwd3_ = pwd2 + servertime + nonce
    pwd3 = hashlib.sha1(pwd3_).hexdigest()
    return pwd3

def __get_user(username):
    '''
    username 经过了BASE64 计算
    '''
    username_ = requests.compat.quote(username)
    username = base64.encodestring(username_)[:-1]
    return username


def loginAndGetToken(username,pwd):
    
    session = requests.session()
    url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.3.22)'
    try:
        servertime, nonce = __get_servertime()
    except:
        return
    global postdata
    postdata['servertime'] = servertime
    postdata['nonce'] = nonce
    postdata['su'] = __get_user(username)
    postdata['sp'] = __get_pwd(pwd, servertime, nonce)
    postdata = urllib.urlencode(postdata)
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'}
    result = session.post(
        url = url,
        data = postdata,
        headers = headers
    )
    text = result.content
#    text = result.content.decode("GBK")
#    print text.encode("UTF-8")
    p = re.compile('location\.replace\(\'(.*?)\'\)')
    try:
        login_url = p.search(text).group(1)
#        print login_url
        response = session.get(login_url)
        response = session.get("https://api.weibo.com/oauth2/authorize?client_id=3231340587&redirect_uri=http://2.xweiboproxy.sinaapp.com%2Fcallback.php&response_type=code", allow_redirects=True)
#        print response.status_code
        data = json.loads(response.content)
        access_token = str(data['access_token'])
        print access_token
        return access_token
    except:
        return 0
