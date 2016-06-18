# coding: utf-8

import os
import operator

from config import Config
from utils.singleton import Singleton


class Catalog(metaclass=Singleton):
    def __init__(self):
        catalog = []

        for filename in os.listdir(Config().posts_path):
            if filename[0] in "0123456789":  # 列出以规定日期格式开头的文章，这个方法好像有点傻-。-
                with open(os.path.join("./posts", filename)) as f:
                    title = None
                    date = filename.split(".")[0]
                    title = f.readline()
                    catalog.append((title, date, filename))

        self.catalog = sorted(catalog, key=operator.itemgetter(1), reverse=True)

    def __iter__(self):
        for item in self.catalog:
            yield item
