# coding: utf-8

import logging

import tornado.web
import tornado.ioloop

from config import Config

from tornado.options import define, options, parse_command_line
define("debug", default=False, type=bool, help="debug is set to True if this option is set")
define("port", default=8080, type=int, help="port=8080")
parse_command_line()


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", top_part=Config().top_part)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler)
        ]
        settings = {
            "template_path": Config().template_path,
            "static_path": Config().static_path,
            "cookie_secret": "cfHo1VmQ8z9kut.wMVwympjbM",
            "debug": options.debug,
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = Application()
    app.listen(options.port)
    logging.warn("server has been listen at port %s with debug set to %s." % (options.port, options.debug))
    tornado.ioloop.IOLoop.current().start()
