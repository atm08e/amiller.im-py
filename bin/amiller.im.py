#!/usr/bin/python3.5
import os, sys

script_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(script_dir, '..'))

from amiller.server import Server

if __name__ == '__main__':
    a = Server()
    a.run()