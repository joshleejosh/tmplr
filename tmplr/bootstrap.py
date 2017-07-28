# -*- coding: utf-8 -*-
"""
Command processing.
"""

from . import consts, helpers, outputter, entry, template, watcher

def configure(args, v, f):
    """
    Set up globals in `consts` from command line args.
    """
    consts.setup_consts(args, v, f)

def run(command):
    """
    Run the given command based on the current configuration.
    """
    entry.setup()
    template.setup()

    if command == 'CLEAN':
        print('Clean stray files out of output dir %s'%consts.OUTDIR)
        helpers.clean_output()

    elif command == 'NEW':
        #print('Create a new entry in note dir %s'%consts.INDIR)
        helpers.new_entry()

    elif command == 'BUILD':
        outputter.regenerate()
        helpers.copy_assets()

    elif command == 'WATCH':
        watcher.watch()

    else:
        print('Invalid command [%s]'%command)

