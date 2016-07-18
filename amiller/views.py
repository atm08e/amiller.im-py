import aiohttp_jinja2
from aiohttp import web

class SiteHandler:

    @aiohttp_jinja2.template('index.html')
    async def index(self, request):
        return {}