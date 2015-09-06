import os, datetime

VERBOSE=False
FORCE=False

BASEURL='http://localhost/'
TITLE='TMPLR'
BLURB='Yet another static site generator'
INDEX_TITLE = 'Tmplr Test Title'
NUM_INDEX_ENTRIES=7

INDIR='in'
OUTDIR='out'
TEMPLATEDIR='templates'
ASSETDIR='assets'

# Eh, don't fiddle with these.
ARCHIVEID=100000
FIRSTID=100010
NOW = datetime.datetime.utcnow()

# ############################################################ #

def setup_consts(args):
    global VERBOSE, FORCE, INDIR, OUTDIR, TEMPLATEDIR, ASSETDIR, BASEURL, TITLE, BLURB, INDEX_TITLE, NUM_INDEX_ENTRIES

    if args.has_key('verbose') and args['verbose']:
        VERBOSE=True
        if VERBOSE:
            print 'verbose output'

    if args.has_key('force') and args['force']:
        FORCE=True
        if VERBOSE:
            print 'force output'

    if args.has_key('indir') and args['indir']:
        INDIR=args['indir']
        if VERBOSE:
            print 'indir = %s'%INDIR
    if not os.path.exists(INDIR):
        raise Exception('ERROR: Missing input dir %s'%INDIR)

    if args.has_key('outdir') and args['outdir']:
        OUTDIR=args['outdir']
        if VERBOSE:
            print 'outdir = %s'%OUTDIR
    if not os.path.exists(OUTDIR):
        raise Exception('ERROR: Missing output dir %s' % OUTDIR)

    if args.has_key('templatedir') and args['templatedir']:
        TEMPLATEDIR=args['templatedir']
        if VERBOSE:
            print 'templatedir = %s'%TEMPLATEDIR
    if not os.path.exists(TEMPLATEDIR):
        raise Exception('ERROR: Missing template dir %s' % TEMPLATEDIR)

    if args.has_key('assetdir') and args['assetdir']:
        ASSETDIR=args['assetdir']
        if VERBOSE:
            print 'assetdir = %s'%ASSETDIR
    if not os.path.exists(ASSETDIR):
        raise Exception('ERROR: Missing asset dir %s' % ASSETDIR)

    if args.has_key('baseurl') and args['baseurl']:
        BASEURL=args['baseurl']
        if VERBOSE:
            print 'baseurl = %s'%BASEURL

    if args.has_key('title') and args['title']:
        TITLE=args['title']
        if VERBOSE:
            print 'title = %s'%TITLE

    if args.has_key('blurb') and args['blurb']:
        BLURB=args['blurb']
        if VERBOSE:
            print 'blurb = %s'%BLURB

    if args.has_key('index_title') and args['index_title']:
        INDEX_TITLE=args['index_title']
        if VERBOSE:
            print 'index_title = %s'%INDEX_TITLE

    if args.has_key('num_index_entries') and args['num_index_entries']:
        NUM_INDEX_ENTRIES=args['num_index_entries']
        if VERBOSE:
            print 'num_index_entries = %s'%NUM_INDEX_ENTRIES


