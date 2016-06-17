# coding: utf-8

import os

# 这里是首页的大部分内容，例如箴言，等等。将在启动项目的时候导入，并且
# 缓存在内存中。


class Config:
    # 顶栏所需要的信息
    top_part = dict(
        navbar=[
            ("首页", "/"),
            ("Github", "https://github.com/jiajunhuang.com"),
            ("关于我", "/aboutme")
        ],  # navbar这一栏的内容，将按照列表的顺序生成
        index_title="Jiajun's Blog",  # 网站首页的标题，以及顶部的标题
        subtitle="你的眼睛能看多远",  # 网站顶部的标题下面的话
        avatar_img="static/img/avatar.png",  # 网站顶部的头像
        announcement="Stand on the shoulders of giants, observing details of the world.",  # 网站首页旁边的公告栏
    )

    template_path = os.path.join(os.path.dirname(__file__), "templates")
    static_path = os.path.join(os.path.dirname(__file__), "static")
