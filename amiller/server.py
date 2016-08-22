import asyncio
import logging
import time
import pathlib
import markdown
import os
import sys

from aiohttp import web

# To get a grip on our parent module
script_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from amiller.ApiHandler import ApiHandler
from amiller.routes import *

# TODO PROJECT ROOT
PROJ_ROOT = pathlib.Path(__file__).parent

class Server:
    async def init_markdown_engine(app):
        pass
        #
        # setup template engine
        #aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('amiller','templates'))
        #
        # Setup markdown filter
        #md = markdown.Markdown(extensions=['meta'])
        #env = aiohttp_jinja2.get_env(app)
        #env.filters['markdown'] = lambda text: md.convert(text)
        #env.globals['get_title'] = lambda: md.Meta['title'][0] # TODO change to get?
        #env.trim_blocks = True
        #env.lstrip_blocks = True

    async def init(loop):
        logging.info("Project Root:{}".format(PROJ_ROOT))

        # setup application and extensions
        app = web.Application(loop=loop)

        # load markdown
        await Server.init_markdown_engine(app)

        # Load the snowboard_gallery json from disk
        snowboarding_gallery = None

        # Load the fishing gallery json from disk
        fishing_gallery = None

        # Load blog posts markup from disk
        blog_posts = None

        # Build api functions, and inject resources
        handler = ApiHandler(snowboarding_gallery=snowboarding_gallery, fishing_gallery=fishing_gallery,
                             blog_posts=blog_posts)

        # Setup routes and link them to the api_handler
        await Server.setup_routes(app, handler)

        host, port = 'localhost', 8088
        return app, host, port

    @staticmethod
    def run():
        #
        start_time = time.time()
        # init logging
        logging.basicConfig(level=logging.INFO)
        #
        loop = asyncio.get_event_loop()
        app, host, port = loop.run_until_complete(Server.init(loop))
        #
        logging.info("Running web app now. Boot time: {}".format(time.time()-start_time))
        #
        web.run_app(app, host=host, port=port)

    async def setup_routes(app, handler):
        add_route = app.router.add_route
        for route in routes(handler):
            logging.info(route)
            add_route(*route)

if __name__ == '__main__':
    Server.run()
