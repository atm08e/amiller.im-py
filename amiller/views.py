import logging

import aiohttp_jinja2
from aiohttp import web


class SiteHandler:
    def __init__(self):
        logging.info("Setting up {} !".format(__name__))

    @aiohttp_jinja2.template('index.html')
    async def index(self, request):
        logging.info("rendering index template!")
