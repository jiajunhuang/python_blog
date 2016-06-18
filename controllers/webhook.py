# coding: utf-8

import os
import tornado.web

from config import Config


class WebHookHandler(tornado.web.RequestHandler):
    def post(self):
        if not os.path.exists(Config().github_webhook_secret_path):
            self.finish()
