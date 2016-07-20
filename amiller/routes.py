import logging
from collections import namedtuple

Route = namedtuple('Route', 'method, path, handler')

def routes(handler):
    return [
        ('GET', '/', getattr(handler, 'index')),
        #('GET', '/stats', 'stats')
    ]
def get_routes_generator(handler):
    logging.info("Generating Routes!")
    return (Route(*t)
        for t in routes(handler))