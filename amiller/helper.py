import os
import yaml

async def load_config(fname):
    async with open(fname, 'rt') as f:
        data = await yaml.load(fname)
        return data

async def load_resources(config):
    # TODO put everything in memory
    pass

async def load_gallery_list():


async def load_gallery_resources():
    pass