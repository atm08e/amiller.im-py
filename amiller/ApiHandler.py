import json
import logging

import markdown as markdown

import aiohttp_jinja2
import os
from aiohttp import web


class ApiHandler:
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
            {"aspectRatio": 1.3389121338912133, "height": 478, "width": 640,
              "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_161107-640x478.jpg",
              "lightboxImage": {"srcset": [
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_161107-3200x2393.jpg 3200w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_161107-1600x1196.jpg 1600w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_161107-1280x957.jpg 1280w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_161107-800x598.jpg 800w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_161107-640x478.jpg 640w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_161107-400x299.jpg 400w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_161107-320x239.jpg 320w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_161107-256x191.jpg 256w"],
                                "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_161107-320x239.jpg"}},
             {"aspectRatio": 1.3333333333333333, "height": 480, "width": 640,
              "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_083317-640x480.jpg",
              "lightboxImage": {"srcset": [
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_083317-2592x1944.jpg 2592w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_083317-1600x1200.jpg 1600w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_083317-1280x960.jpg 1280w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_083317-800x600.jpg 800w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_083317-640x480.jpg 640w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_083317-400x300.jpg 400w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_083317-320x240.jpg 320w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_083317-256x192.jpg 256w"],
                                "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_083317-320x240.jpg"}},
             {"aspectRatio": 1.0, "height": 480, "width": 480,
              "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_144150-480x480.jpg",
              "lightboxImage": {"srcset": [
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_144150-2400x2400.jpg 2400w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_144150-1200x1200.jpg 1200w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_144150-960x960.jpg 960w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_144150-600x600.jpg 600w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_144150-480x480.jpg 480w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_144150-300x300.jpg 300w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_144150-240x240.jpg 240w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_144150-192x192.jpg 192w"],
                                "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160221_144150-240x240.jpg"}},
             {"aspectRatio": 1.3389121338912133, "height": 478, "width": 640,
              "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105056-640x478.jpg",
              "lightboxImage": {"srcset": [
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105056-3200x2393.jpg 3200w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105056-1600x1196.jpg 1600w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105056-1280x957.jpg 1280w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105056-800x598.jpg 800w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105056-640x478.jpg 640w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105056-400x299.jpg 400w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105056-320x239.jpg 320w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105056-256x191.jpg 256w"],
                                "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105056-320x239.jpg"}},
             {"aspectRatio": 1.3389121338912133, "height": 478, "width": 640,
              "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105102-640x478.jpg",
              "lightboxImage": {"srcset": [
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105102-3200x2393.jpg 3200w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105102-1600x1196.jpg 1600w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105102-1280x957.jpg 1280w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105102-800x598.jpg 800w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105102-640x478.jpg 640w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105102-400x299.jpg 400w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105102-320x239.jpg 320w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105102-256x191.jpg 256w"],
                                "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160223_105102-320x239.jpg"}},
             {"aspectRatio": 1.3389121338912133, "height": 478, "width": 640,
              "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_115546-640x478.jpg",
              "lightboxImage": {"srcset": [
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_115546-3200x2392.jpg 3200w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_115546-1600x1196.jpg 1600w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_115546-1280x956.jpg 1280w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_115546-800x598.jpg 800w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_115546-640x478.jpg 640w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_115546-400x299.jpg 400w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_115546-320x239.jpg 320w",
                  "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_115546-256x191.jpg 256w"],
                                "src": "https://s3.amazonaws.com/akiaimqvtavzolsx3gla-test/IMG_20160224_115546-320x239.jpg"}}

        ]
        return web.json_response(data=data, headers=headers)


