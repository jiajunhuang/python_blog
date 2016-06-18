# coding: utf-8

import os
import hmac
import hashlib
import json

import tornado.web
import git

from config import Config


class GithubWebHooksHandler(tornado.web.RequestHandler):
    def get(self):  # github webhooks ping
        self.finish()

    def post(self):
        if not os.path.exists(Config().github_webhook_secret_path):
            self.finish()
            return

        data = json.loads(self.request.body)
        if not self._validate_signature(data):
            self.finish()
            return

        # 下面的操作是阻塞的-。- 暂且不用celery试试看
        repo = git.Repo(__file__)
        repo.pull()

        for submodule in repo.submodules:
            submodule.update(init=True)

    def _validate_signature(self, data):
        sha_name, signature = self.request.headers.get('X-Hub-Signature').split('=')
        if sha_name != 'sha1':
            return False

        # HMAC requires its key to be bytes, but data is strings.
        mac = hmac.new(Config().github_secret_key, msg=data, digestmod=hashlib.sha1)
        return hmac.compare_digest(mac.hexdigest(), signature)
