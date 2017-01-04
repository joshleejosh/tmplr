import os, datetime

VERBOSE=False
FORCE=False

BASEURL='http://localhost/'
TITLE='tmplr'
BLURB='yet another static site generator'
INDEX_TITLE = 'tmplr index'
ARCHIVE_TITLE = 'tmplr archives'
NUM_INDEX_ENTRIES = 7

INDIR='in'
OUTDIR='out'
TEMPLATEDIR='templates'
ASSETDIR='assets'

WATCH_RATE=5

# Eh, don't fiddle with these.
ARCHIVEID=100000
FIRSTID=100010
NOW = datetime.datetime.utcnow()

# ############################################################ #

def setup_consts(args, forceVerbose, forceForce):
    global VERBOSE, FORCE, INDIR, OUTDIR, TEMPLATEDIR, ASSETDIR, BASEURL, TITLE, BLURB, INDEX_TITLE, ARCHIVE_TITLE, NUM_INDEX_ENTRIES, WATCH_RATE

    if (args.has_key('verbose') and args['verbose']) or forceVerbose:
        VERBOSE = True
        if VERBOSE:
            print 'verbose output'

    if (args.has_key('force') and args['force']) or forceForce:
        FORCE = True
        if VERBOSE:
            print 'force output'

    if args.has_key('indir') and args['indir']:
        INDIR = os.path.expandvars(args['indir'])
        if VERBOSE:
            print 'indir = %s'%INDIR
    if not os.path.exists(INDIR):
        raise Exception('ERROR: Missing input dir %s'%INDIR)

    if args.has_key('outdir') and args['outdir']:
        OUTDIR = os.path.expandvars(args['outdir'])
        if VERBOSE:
            print 'outdir = %s'%OUTDIR
    if not os.path.exists(OUTDIR):
        raise Exception('ERROR: Missing output dir %s' % OUTDIR)

    if args.has_key('templatedir') and args['templatedir']:
        TEMPLATEDIR = os.path.expandvars(args['templatedir'])
        if VERBOSE:
            print 'templatedir = %s'%TEMPLATEDIR
    if not os.path.exists(TEMPLATEDIR):
        raise Exception('ERROR: Missing template dir %s' % TEMPLATEDIR)

    if args.has_key('assetdir') and args['assetdir']:
        ASSETDIR = os.path.expandvars(args['assetdir'])
        if VERBOSE:
            print 'assetdir = %s'%ASSETDIR
    if not os.path.exists(ASSETDIR):
        raise Exception('ERROR: Missing asset dir %s' % ASSETDIR)

    if args.has_key('baseurl') and args['baseurl']:
        BASEURL = os.path.expandvars(args['baseurl'])
        if VERBOSE:
            print 'baseurl = %s'%BASEURL

    if args.has_key('title') and args['title']:
        TITLE = args['title']
        if VERBOSE:
            print 'title = %s'%TITLE

    if args.has_key('blurb') and args['blurb']:
        BLURB = args['blurb']
        if VERBOSE:
            print 'blurb = %s'%BLURB

    if args.has_key('index_title') and args['index_title']:
        INDEX_TITLE = args['index_title']
        if VERBOSE:
            print 'index_title = %s'%INDEX_TITLE

    if args.has_key('num_index_entries') and args['num_index_entries']:
        NUM_INDEX_ENTRIES = args['num_index_entries']
        if VERBOSE:
            print 'num_index_entries = %d'%NUM_INDEX_ENTRIES

    if args.has_key('archive_title') and args['archive_title']:
        ARCHIVE_TITLE = args['archive_title']
        if VERBOSE:
            print 'archive_title = %s'%ARCHIVE_TITLE

    if args.has_key('watch_rate') and args['watch_rate']:
        WATCH_RATE = args['watch_rate']
        if VERBOSE:
            print 'watch_rate = %d'%WATCH_RATE

