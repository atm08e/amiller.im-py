import json
import logging

import markdown as markdown

import aiohttp_jinja2
import os
from aiohttp import web


class ApiHandler:
    gallery = None
    def __init__(self, snowboarding_gallery, fishing_gallery, blog_posts):
        logging.info("Setting up {} !".format(__name__))
        print(type(snowboarding_gallery))
        self.gallery=snowboarding_gallery

    @aiohttp_jinja2.template('index.html')
    async def index(self, request):
        logging.info("rendering index template!")
        return {}
        #return {'tests': self.load_blog_post()}

    async def snowboarding(self, request):

        # TODO only in dev mode
        headers = {
            web.hdrs.ACCESS_CONTROL_ALLOW_ORIGIN: 'https://amiller-api.apps.mia.ulti.io'
        }
        #print(self.gallery)

        #print(json.dumps(self.gallery))
        return web.json_response(self.gallery, headers=headers)


