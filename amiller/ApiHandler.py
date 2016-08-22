import json
import logging

import markdown as markdown

import aiohttp_jinja2
import os
from aiohttp import web


class Handlers:
    def __init__(self, snowboarding_gallery, fishing_gallery, blog_posts):
        logging.info("Setting up {} !".format(__name__))

    @aiohttp_jinja2.template('index.html')
    async def index(self, request):
        logging.info("rendering index template!")
        return {}
        #return {'tests': self.load_blog_post()}

    async def snowboarding(self, request):

        # TODO only in dev mode
        headers = {
            web.hdrs.ACCESS_CONTROL_ALLOW_ORIGIN: 'http://localhost:3000'
        }

        data = [
                {
                    'src': 'http://snowbrains.com/wp-content/uploads/2014/01/url-2.jpeg',
                    'width': 1920,
                    'height': 1080,
                    'aspectRatio': 1,
                    'lightboxImage': {
                        'src': 'http://snowbrains.com/wp-content/uploads/2014/01/url-2.jpeg',
                        'srcset': [
                            'http://snowbrains.com/wp-content/uploads/2014/01/url-2.jpeg 1920w'
                        ]
                    }
                },
            {
                'src': 'http://snowbrains.com/wp-content/uploads/2014/01/url-2.jpeg',
                'width': 1920,
                'height': 1080,
                'aspectRatio': 1,
                'lightboxImage': {
                    'src': 'http://snowbrains.com/wp-content/uploads/2014/01/url-2.jpeg',
                    'srcset': [
                        'http://snowbrains.com/wp-content/uploads/2014/01/url-2.jpeg 1920w'
                    ]
                }
            }
            ]
        return web.json_response(data=data, headers=headers)


