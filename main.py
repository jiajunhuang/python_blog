# coding: utf-8

import os
import logging

import tornado.web
import tornado.ioloop
import tornado.autoreload

from config import Config

from tornado.options import define, options, parse_command_line
define("debug", default=False, type=bool, help="debug is set to True if this option is set")
define("port", default=8080, type=int, help="port=8080")
parse_command_line()


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", top_part=Config().top_part)


class PostHandler(tornado.web.RequestHandler):
    def get(self):
        article = {
            "title": "这是一片文章的标题",
            "content": "我是内容"
        }
        self.render("post.html", top_part=Config().top_part, article=article)


class AboutMeHandler(tornado.web.RequestHandler):
    def get(self):
        article = {
            "title": "关于我",
            "content": "这里是我的介绍"
        }
        self.render("post.html", top_part=Config().top_part, article=article)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/post", PostHandler),
            (r"/aboutme", PostHandler),
        ]
        settings = {
            "template_path": Config().template_path,
            "static_path": Config().static_path,
            "cookie_secret": "cfHo1VmQ8z9kut.wMVwympjbM",
            "debug": options.debug,
        }
        if os.path.exists(Config().posts_path):
            tornado.autoreload.watch(Config().posts_path)
            settings.update({
                "autoreload": True,
            })
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = Application()
    app.listen(options.port)
    logging.warn("server has been listen at port %s with debug set to %s." % (options.port, options.debug))
    tornado.ioloop.IOLoop.current().start()
