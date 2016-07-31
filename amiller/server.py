import asyncio
import logging

import time

import markdown
import os
import sys

from aiohttp import web
import aiohttp_jinja2
import jinja2

# To get a grib on our parent module
script_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from amiller.views import Handlers
from amiller.routes import *

# TODO PROJECT ROOT
#PROJ_ROOT = pathlib.Path(__file__).parent.parent

class Server:

    @staticmethod
    async def signal_handlers():
        pass

    @staticmethod
    async def init_markdown_engine(app):
        #
        # setup template engine
        aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('amiller','templates'))
        #
        # Setup markdown filter
        md = markdown.Markdown(extensions=['meta'])
        env = aiohttp_jinja2.get_env(app)
        env.filters['markdown'] = lambda text: md.convert(text)
        env.globals['get_title'] = lambda: md.Meta['title'][0] # TODO change to get?
        #env.trim_blocks = True
        #env.lstrip_blocks = True

    @staticmethod
    async def init(loop):

        #
        # setup signal handlers

        #
        # setup application and extensions
        app = web.Application(loop=loop)

        #
        # load config from yaml file
        # conf = load_config(str(PROJ_ROOT / 'config' / 'polls.yaml'))


        #
        # load markdown
        await Server.init_markdown_engine(app)

        #
        # setup views and routes
        handler = Handlers()
        await Server.setup_routes(app, handler)

        #
        # create connection to the database
        # pg = await init_postgres(conf['postgres'] ||, loop)
        #
        # defer the closer
        # async def close_pg(app):
        #    pg.close()
        #    await pg.wait_closed()
        # app.on_cleanup.append(close_pg)

        # TODO add these to config
        host, port = 'localhost', 8088
        return app, host, port

    @staticmethod
    def run():
        #
        start_time = time.time()
        # init logging
        logging.basicConfig(level=logging.INFO)
        #
        # TODO - docs
        loop = asyncio.get_event_loop()
        app, host, port = loop.run_until_complete(Server.init(loop))
        #
        logging.info("Running web app now. Boot time: {}".format(time.time()-start_time))
        #
        web.run_app(app, host=host, port=port)

    @staticmethod
    async def setup_routes(app, handler):
        add_route = app.router.add_route
        for route in routes(handler):
            logging.info(route)
            add_route(*route)

        path = sys.path.append(os.path.join(script_dir, '..'))
        #app.router.add_static(prefix='/static/', path=str(path))
        # add_static_route = app.router.add_static
        # for static_route in static_routes():
        #     add_static_route(*static_route)


if __name__ == '__main__':
    Server.run()
