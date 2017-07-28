# -*- coding: utf-8 -*-
"""
Template management and processing.
"""

from __future__ import unicode_literals
from builtins import open
import os
import cgi
import datetime
import re
from . import consts, entry
from .util import d2s_rfc3339, d2s

RE_STRIP = re.compile(r'<[^>]*>')
RE_TEMPLATE_TAG = re.compile(r'\<@([^@]+)@\>')

G_TEMPLATES = {}

def setup():
    """
    Load templates for later access.
    """
    G_TEMPLATES.clear()
    for fn in os.listdir(consts.TEMPLATEDIR):
        tm = _read_template(os.path.join(consts.TEMPLATEDIR, fn))
        G_TEMPLATES[tm['id']] = tm

# ############################################################# #

def _linkify_tag(tag):
    return '<a href="tag/%s.html">%s</a>'%(tag, tag)

def _format_time(dt, fmt):
    dolower = doupper = False
    if fmt.find('%!l') != -1:
        dolower = True
        fmt = fmt.replace('%!l', '')
    if fmt.find('%!u') != -1:
        doupper = True
        fmt = fmt.replace('%!u', '')
    rv = datetime.datetime.strftime(dt, fmt)
    if dolower:
        rv = rv.lower()
    if doupper:
        rv = rv.upper()
    return rv

def _run_template_tag(key, ent):
    out = ''

    if key.endswith('-stripped'):
        nk = key[:-len('-stripped')]
        out = RE_STRIP.sub('', ent[nk])

    elif key.endswith('-escaped'):
        nk = key[:-len('-escaped')]
        out = cgi.escape(ent[nk])

    elif key.endswith('-rfc3339'):
        nk = key[:-len('-rfc3339')]
        out = d2s_rfc3339(ent[nk])

    elif key.find('-ftime:') != -1:
        nk = key[:key.find('-ftime:')]
        fmt = key[len(nk)+len('-ftime:'):]
        out = _format_time(ent[nk], fmt)

    elif key == 'date' or key == 'siteTimestamp':
        out = d2s(ent[key])

    elif key == 'tags':
        out = ', '.join(map(_linkify_tag, ent[key]))

    else:
        out = ent[key]
    return out

def run_template_entry(tk, en):
    """
    Process a template on an entry.
    """
    tm = G_TEMPLATES[tk]
    s = tm['template']
    for i in RE_TEMPLATE_TAG.findall(s):
        nv = _run_template_tag(i, en)
        s = re.sub(r'\<@' + i + r'@\>', nv, s)
    return s

def run_template_loop(tk, baseent, entries, numtodo=-1):
    """
    Process a template on a collection of entries.
    """
    ekeys = entry.sorted_entry_keys(entries)
    if numtodo == -1:
        numtodo = len(ekeys)
    tm = G_TEMPLATES[tk]
    s = tm['template']
    for i in RE_TEMPLATE_TAG.findall(s):
        nv = ''
        if i.startswith('loopentries-'):
            k = i[len('loopentries-'):]
            for key in ekeys[:numtodo]:
                nv += run_template_entry(k, entries[key]) + '\n'
        else:
            nv = _run_template_tag(i, baseent)
        s = re.sub(r'\<@' + i + r'@\>', nv, s)
    return s

def _read_template(fn):
    s = ''
    with open(fn, encoding='utf-8') as fp:
        s = fp.read()
    tail = os.path.split(fn)[-1]
    return {
        'id': tail,
        'template': s,
    }

