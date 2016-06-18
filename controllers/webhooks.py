# coding: utf-8

import os
import tornado.web

from config import Config


class WebHooksHandler(tornado.web.RequestHandler):
    def get(self):  # github webhooks ping
        self.finish()

    def post(self):
        if not os.path.exists(Config().github_webhook_secret_path):
            self.finish()
