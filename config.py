# coding: utf-8

import os

from utils.singleton import Singleton

# 这里是首页的大部分内容，例如箴言，等等。将在启动项目的时候导入，并且
# 缓存在内存中。


class Config(metaclass=Singleton):
    # 顶栏所需要的信息
    top_part = dict(
        navbar=[
            ("首页", "/"),
            ("Github", "https://github.com/jiajunhuang"),
            ("关于我", "/aboutme")
        ],  # navbar这一栏的内容，将按照列表的顺序生成
        index_title="Jiajun's Blog",  # 网站首页的标题，以及顶部的标题
        subtitle="你的眼睛能看多远",  # 网站顶部的标题下面的话
        avatar_img="static/img/avatar.png",  # 网站顶部的头像
        announcement="Stand on the shoulders of giants, observing details of the world.",  # 网站首页旁边的公告栏
    )

    template_path = os.path.join(os.path.dirname(__file__), "templates")  # 模板的路径
    static_path = os.path.join(os.path.dirname(__file__), "static")  # 静态文件的路径
    posts_path = os.path.join(os.path.dirname(__file__), "posts")  # posts文件夹的路径
    article_img_path = os.path.join(posts_path, "img")  # 纯文本文件中 .. image:: img.png 的存储路径

    def article_path(self, filename):  # 获取某篇文章的具体路径
        return os.path.join(self.posts_path, filename)

    @staticmethod
    def article_url(filename):  # 生成文章url所用的函数
        return os.path.join("./article", filename)
