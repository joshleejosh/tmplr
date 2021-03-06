# -*- coding: utf-8 -*-
"""
Base entry handling.
"""

from __future__ import unicode_literals
from builtins import open
import os
import copy
import collections
import markdown
from . import consts
from .util import path2id, s2d

ENTRY_SUFFIX = '.md'
G_ENTRIES = {}
G_TAGS = {}

def setup():
    """
    Load all entries from the input directory and initialize the global catalog.
    """
    G_ENTRIES.clear()
    G_TAGS.clear()
    for fn in os.listdir(consts.INDIR):
        e = read_entry(os.path.join(consts.INDIR, fn))
        if e['id'] != str(consts.ARCHIVEID):
            G_ENTRIES[e['id']] = e
            _read_tags(e)

def empty_entry():
    """
    Create an initialized entry dict.
    """
    rv = collections.defaultdict(str)
    rv.update({
        'id':str(consts.FIRSTID),
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
    })
    return rv

# ############################################################# #

def _parse_tags(ins):
    out = []
    for s in ins.split(','):
        s = s.strip().lower()
        if s and s not in out:
            out.append(s)
    return out

def read_entry(fn):
    """
    Create an entry object from the given file.
    """
    oute = empty_entry()
    with open(fn, encoding='utf-8') as fp:
        inhead = True
        oute['id'] = path2id(fn)
        oute['editTimestamp'] = os.path.getmtime(fn)
        for line in fp.readlines():
            if not inhead:
                oute['body'] += line
            else:
                line = line.strip()
                if not line:
                    inhead = False
                else:
                    a = line.split(':')
                    k = a[0].strip()
                    v = ':'.join(a[1:]).strip()

                    if k == 'date':
                        oute[k] = s2d(v)
                    elif k == 'tags':
                        oute[k] = _parse_tags(v)
                    else:
                        oute[k] = v

        oute['url'] = '' + oute['slug'] + '.html'
        oute['body'] = markdown.markdown(oute['body'], extensions=('markdown.extensions.smarty',))
    return oute

def sorted_entry_keys(entries):
    """
    Sort entry IDs from the global catalog.
    """
    out = list(entries.keys())
    out.sort()
    if consts.INDEX_REVERSE_TIME:
        out.reverse()
    return out

def _read_tags(entry):
    """
    Read tags from an entry and add them to the global catalog.
    """
    for tag in entry['tags']:
        if tag not in G_TAGS.keys():
            G_TAGS[tag] = [entry['id'],]
        else:
            G_TAGS[tag].append(entry['id'])

def get_entries():
    """
    Get all past and present entries. Exclude postdated entries.
    """
    rv = {}
    for ent in G_ENTRIES.values():
        if ent['date'] <= consts.NOW:
            newe = copy.deepcopy(ent)
            rv[newe['id']] = newe
    return rv

