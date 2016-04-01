import os, copy, markdown
import consts
from util import *

ENTRY_SUFFIX = '.md'
gEntries = {}
gTags = {}

def setup():
    gEntries.clear();
    gTags.clear()
    for fn in os.listdir(consts.INDIR):
        e = read_entry(os.path.join(consts.INDIR, fn))
        if e['id'] != str(consts.ARCHIVEID):
            gEntries[e['id']] = e
            read_tags(e)

""" Create an initialized entry dict """
def empty_entry():
    return {
        'id':consts.FIRSTID,
        'title': '',
        'slug': '',
        'blurb': '',
        'date': consts.NOW,
        'body':'',
        'tags':[],
        'url':'',
        'siteTitle':consts.TITLE,
        'siteBlurb':consts.BLURB,
        'siteTimestamp': consts.NOW,
        'baseurl':consts.BASEURL,
        'editTimestamp':consts.NOW,
    }

# ############################################################# #

def parse_tags(ins):
    out = []
    for s in ins.split(','):
        s = s.strip().lower()
        if s and s not in out:
            out.append(s)
    return out

def read_entry(fn):
    fp = open(fn)
    inHead = True
    oute = empty_entry()
    oute['id'] = path2id(fn)
    oute['editTimestamp'] = os.path.getmtime(fn)
    for line in fp.readlines():
        if not inHead:
            oute['body'] += line
        else:
            line = line.strip()
            if (line == ''):
                inHead = False
            else:
                a = line.split(':')
                k = a[0].strip()
                v = ':'.join(a[1:]).strip()

                if k == 'date':
                    oute[k] = s2d(v)
                elif k == 'tags':
                    oute[k] = parse_tags(v)
                else:
                    oute[k] = v

    oute['url'] = '' + oute['slug'] + '.html'
    oute['body'] = oute['body'].decode('utf-8').encode('ascii', 'xmlcharrefreplace')
    oute['body'] = markdown.markdown(oute['body'], extensions=('markdown.extensions.smarty',))

    return oute

def sorted_entry_keys(entries):
    out = entries.keys()
    out.sort()
    out.reverse()
    return out;

def read_tags(entry):
    for tag in entry['tags']:
        if tag not in gTags.keys():
            gTags[tag] = [entry['id'],]
        else:
            gTags[tag].append(entry['id'])

def get_entries():
    rv = {}
    for eid,entry in gEntries.iteritems():
        if entry['date'] <= consts.NOW:
            newe = copy.deepcopy(entry)
            rv[newe['id']] = newe
    return rv;

# ############################################################# #

ENTRY_HEADER = """title: %s
slug: %s
date: %s
blurb: %s
tags: %s

"""


# Create a new entry file in INDIR
def new_entry():
    newId = consts.FIRSTID
    for e in gEntries.iterkeys():
        if int(e) > newId:
            newId = int(e)
    newId += 1

    title = "Links for %s"%datetime.datetime.strftime(consts.NOW, '%B %e, %Y')
    slug = datetime.datetime.strftime(consts.NOW, '%B-%d-%Y').lower()
    ds = d2s_dt(consts.NOW)
    blurb = ''
    tags = ''

    fn = os.path.join(consts.INDIR, str(newId) + ENTRY_SUFFIX)
    print fn
    fp = file(fn, 'w')
    fp.write(ENTRY_HEADER%(title, slug, ds, blurb, tags))
    fp.close()

