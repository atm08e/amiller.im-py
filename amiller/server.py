import asyncio
import logging
import os
import sys

from aiohttp import web
import aiohttp_jinja2
import jinja2

# To get a grib on our parent module
script_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from amiller.views import SiteHandler
from amiller.routes import setup_routes

# TODO PROJECT ROOT
#PROJ_ROOT = pathlib.Path(__file__).parent.parent

class Server:
    async def init(self, loop):
        #
        # setup application and extensions
        app = web.Application(loop=loop)
        #
        # setup template engine
        aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('amiller','templates'))

        #
        # load config from yaml file
        ##conf = load_config(str(PROJ_ROOT / 'config' / 'polls.yaml'))

        #
        # create connection to the database
        # pg = await init_postgres(conf['postgres'] ||, loop)

        #
        # defer the closer
        # async def close_pg(app):
        #    pg.close()
        #    await pg.wait_closed()

        #app.on_cleanup.append(close_pg)

        # setup views and routes
        handler = SiteHandler()
        setup_routes(app, handler, project_root=None)

        # TODO add these to config
        host, port = 'localhost', 8088
        return app, host, port


    def run(self):
        # init logging
        logging.basicConfig(level=logging.INFO)

        # TODO - docs
        loop = asyncio.get_event_loop()
        app, host, port = loop.run_until_complete(self.init(loop))

        web.run_app(app, host=host, port=port)

if __name__ == '__main__':
     a = Server()
     a.run()