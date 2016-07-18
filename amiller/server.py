import asyncio

import aiohttp_jinja2
import jinja2
from aiohttp import web

import logging

class Server:

    async def index(self):
        pass

    async def blod(self):
        pass

    async def favorites(self):
        pass

    async def resume(self):
        pass

    async def fishing(self):
        pass

    async def snow(self):
        pass

    async def about(self):
        pass

    async def add_routes(self):
        pass

    async def init(self):
        app = web.Application()
        app.router.add_route('GET', '/', self.index)
        app.router.add_route('GET', '/blog', self.blog)
        app.router.add_route('GET', '/favorites', self.favorites)
        app.router.add_route('GET', '/resume', self.resume)
        app.router.add_route('GET', '/fishing', self.fishing)
        app.router.add_route('GET', '/snow', self.snow)
        app.router.add_route('GET', '/about', self.about)
        return app



async def init(loop):
    # setup application and extensions
    app = web.Application(loop=loop)
    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('aiohttpdemo_polls', 'templates'))
    # load config from yaml file
    ##conf = load_config(str(PROJ_ROOT / 'config' / 'polls.yaml'))

    # create connection to the database
    #pg = await init_postgres(conf['postgres'] ||, loop)

    #async def close_pg(app):
    #    pg.close()
    #    await pg.wait_closed()

    #app.on_cleanup.append(close_pg)

    # setup views and routes
    #handler = SiteHandler(pg)
    #setup_routes(app, handler, PROJ_ROOT)
    #setup_middlewares(app)

    host, port = conf['host'], conf['port']
    return app, host, port


def main():
    # init logging
    logging.basicConfig(level=logging.DEBUG)

    loop = asyncio.get_event_loop()
    app, host, port = loop.run_until_complete(init(loop))

if __name__ == '__main__':
     main()