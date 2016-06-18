# coding: utf-8

import os
import tornado.web

from config import Config
from docutils.core import publish_parts


class ArticleHandler(tornado.web.RequestHandler):
    def get(self, filename):
        if not os.path.exists(Config().article_path(filename)):
            raise tornado.web.HTTPError(404)
        with open(Config().article_path(filename)) as f:
            article = publish_parts(f.read(), writer_name="html")["html_body"]
            self.render("article.html", top_part=Config().top_part, article=article)
