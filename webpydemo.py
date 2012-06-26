#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Tony.Shao'

import web
urls = (
    "/hello", "hello"
    )
def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")
app = web.application(urls, globals())
app.notfound = notfound
class hello:
    def GET(self):
        raise web.notfound
#        return "hello"


if __name__ == "__main__":
    app.run()