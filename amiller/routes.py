import logging
from collections import namedtuple


def routes(handler):
    # TODO generator
    return [
        ('GET', '/', handler.index),
        ('GET', '/snowboarding', handler.snowboarding)
    ]

def static_routes():
    # TODO generator
    # TODO static routes defined here
    return [

    ]