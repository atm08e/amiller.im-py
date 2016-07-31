import logging
from collections import namedtuple


def routes(handler):
    return [
        ('GET', '/', handler.index)
    ]
