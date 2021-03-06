# -*- coding: utf-8 -*-
"""
Yet another static site generator.
"""

import argparse
import json
from . import bootstrap

# ###################################################################### #
# ###################################################################### #
# ###################################################################### #

def main():
    """
    Process command-line args and call bootstrap.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('config', help='path to config file')
    parser.add_argument('command', help='new|build|watch|clean')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true')
    parser.add_argument('-f', '--force', dest='force', action='store_true')

    args = parser.parse_args()

    config = {}
    with open(args.config) as fp:
        config = json.load(fp)

    bootstrap.configure(config, args.verbose, args.force)
    bootstrap.run(args.command.upper())

if __name__ == "__main__":
    main()

