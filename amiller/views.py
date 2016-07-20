import logging

import markdown as markdown

import aiohttp_jinja2
import os
from aiohttp import web


class Handlers:
    def __init__(self):
        logging.info("Setting up {} !".format(__name__))

    def load_blog_post(self):
        folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'posts')
        #
        logging.info("Will search: {} for blog post markdown".format(folder))
        #
        return [self.load_markdown(os.path.join(folder, item))
                for item in os.listdir(folder)
                if item.endswith('.md')]

    def load_markdown(self, markdown_path):
        # TODO FIX PATH
        # logging.info(os.path.abspath(path='.'))
        logging.info('Loading markdown: {}'.format(markdown_path))
        with open(markdown_path, 'r') as fin:
            return fin.read()

    @staticmethod
    @aiohttp_jinja2.template('index.html')
    async def index(self, request):
        logging.info("rendering index template!")
        return {}
        #return {'tests': self.load_blog_post()}
