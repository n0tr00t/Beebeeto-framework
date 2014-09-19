#!/usr/bin/env python
# coding=utf-8
# windows2000@ff0000team

from random import randint






class BaseUserAgent(object):
    info = {
        'broswer_name': 'user agent details',
    }

    def randomly_get(self):
        return self.info.items()[randint(0, len(self.info) - 1)]


class Win(BaseUserAgent):
    info = {
        'ie6': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
    }


class IOS(BaseUserAgent):
    info = {
        'safari': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    }


class Android(BaseUserAgent):
    pass


class Linux(BaseUserAgent):
    pass




class ForgeHeaders(object):
    platforms = ['Win', 'IOS', 'Android', 'Linux']
    headers = {
        'Accept': '*/*',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        #'Referer':'http://www.baidu.com',
    }

    def __init__(self):
        platform = self.platforms[randint(0, len(self.platforms) - 1)]
        broswer, user_agent_details = eval('%s().randomly_get()' % platform)
        self.headers.setdefault('User-Agent', user_agent_details)

    def get_headers(self):
        return self.headers


if __name__ == '__main__':
    print ForgeHeaders().headers
    print
    print ForgeHeaders().get_headers()
