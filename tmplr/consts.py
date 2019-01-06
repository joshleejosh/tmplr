# -*- coding: utf-8 -*-
"""
Consts driven by the config file.
"""

import os
import datetime

VERBOSE = False
FORCE = False

BASEURL = 'http://localhost/'
TITLE = 'tmplr'
BLURB = 'yet another static site generator'
INDEX_TITLE = 'tmplr index'
ARCHIVE_TITLE = 'tmplr archives'
NUM_INDEX_ENTRIES = 7
INDEX_REVERSE_TIME = True

INDIR = 'in'
OUTDIR = 'out'
TEMPLATEDIR = 'templates'
ASSETDIR = 'assets'

WATCH_RATE = 5

# Eh, don't fiddle with these.
ARCHIVEID = 100000
FIRSTID = 100010
NOW = datetime.datetime.utcnow()

# ############################################################ #

def setup_consts(args, forceverbose, forceforce):
    """
    Set consts based on the given command-line args.
    """
    global VERBOSE, FORCE, INDIR, OUTDIR, TEMPLATEDIR, ASSETDIR, BASEURL, \
            TITLE, BLURB, INDEX_TITLE, ARCHIVE_TITLE, NUM_INDEX_ENTRIES, \
            INDEX_REVERSE_TIME, WATCH_RATE, NOW

    if ('verbose' in args and args['verbose']) or forceverbose:
        VERBOSE = True
        if VERBOSE:
            print('verbose output')

    if ('force' in args and args['force']) or forceforce:
        FORCE = True
        if VERBOSE:
            print('force output')

    if 'indir' in args and args['indir']:
        INDIR = os.path.expandvars(args['indir'])
        if VERBOSE:
            print('indir = %s'%INDIR)
    if not os.path.exists(INDIR):
        raise Exception('ERROR: Missing input dir %s'%INDIR)

    if 'outdir' in args and args['outdir']:
        OUTDIR = os.path.expandvars(args['outdir'])
        if VERBOSE:
            print('outdir = %s'%OUTDIR)
    if not os.path.exists(OUTDIR):
        raise Exception('ERROR: Missing output dir %s' % OUTDIR)

    if 'templatedir' in args and args['templatedir']:
        TEMPLATEDIR = os.path.expandvars(args['templatedir'])
        if VERBOSE:
            print('templatedir = %s'%TEMPLATEDIR)
    if not os.path.exists(TEMPLATEDIR):
        raise Exception('ERROR: Missing template dir %s' % TEMPLATEDIR)

    if 'assetdir' in args and args['assetdir']:
        ASSETDIR = os.path.expandvars(args['assetdir'])
        if VERBOSE:
            print('assetdir = %s'%ASSETDIR)
    if not os.path.exists(ASSETDIR):
        raise Exception('ERROR: Missing asset dir %s' % ASSETDIR)

    if 'baseurl' in args and args['baseurl']:
        BASEURL = os.path.expandvars(args['baseurl'])
        if VERBOSE:
            print('baseurl = %s'%BASEURL)

    if 'title' in args and args['title']:
        TITLE = args['title']
        if VERBOSE:
            print('title = %s'%TITLE)

    if 'blurb' in args and args['blurb']:
        BLURB = args['blurb']
        if VERBOSE:
            print('blurb = %s'%BLURB)

    if 'index_title' in args and args['index_title']:
        INDEX_TITLE = args['index_title']
        if VERBOSE:
            print('index_title = %s'%INDEX_TITLE)

    if 'num_index_entries' in args and args['num_index_entries']:
        NUM_INDEX_ENTRIES = args['num_index_entries']
        if VERBOSE:
            print('num_index_entries = %d'%NUM_INDEX_ENTRIES)

    if 'index_reverse_time' in args:
        INDEX_REVERSE_TIME = args['index_reverse_time']
        if VERBOSE:
            print('index_reverse_time = %s'%INDEX_REVERSE_TIME)

    if 'archive_title' in args and args['archive_title']:
        ARCHIVE_TITLE = args['archive_title']
        if VERBOSE:
            print('archive_title = %s'%ARCHIVE_TITLE)

    if 'watch_rate' in args and args['watch_rate']:
        WATCH_RATE = args['watch_rate']
        if VERBOSE:
            print('watch_rate = %d'%WATCH_RATE)

    if 'datetime_override' in args and args['datetime_override']:
        NOW = datetime.datetime.strptime(args['datetime_override'], '%Y-%m-%d %H:%M:%S')
        if VERBOSE:
            print('NOW = %s'%NOW)

