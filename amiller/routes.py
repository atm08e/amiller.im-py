import logging
from collections import namedtuple


def routes(handler):
    # TODO generator
    return [
        ('GET', '/', handler.index)
    ]

def static_routes():
    # TODO generator
    # TODO static routes defined here
    return [

    ]