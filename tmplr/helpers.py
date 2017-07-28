# -*- coding: utf-8 -*-
"""
Misc. high-level functions.
"""

import os
import shutil
import glob
import re
import datetime
from . import consts, entry, template

def copy_assets():
    """
    Copy assets to the output dir.
    """
    for f in glob.glob(os.path.join(consts.ASSETDIR, '*')):
        if not os.path.isdir(f):
            shutil.copy(f, consts.OUTDIR)

def clean_output():
    """
    Scrub out files that don't correspond to actual entries.
    """
    todel = []
    for fn in glob.glob(os.path.join(consts.OUTDIR, '*.html')):
        fslug = re.sub(r'\.html.*$', '', re.sub(r'^.*\/', '', fn))
        if fslug == 'archive' or fslug == 'index':
            continue
        hit = False
        for e in entry.get_entries().values():
            if fslug == e['slug']:
                hit = True
                break
        if not hit:
            todel.append(fn)

    for fn in todel:
        print('Deleting stray file %s'%fn)
        os.remove(fn)

def new_entry():
    """
    Create a new entry file in INDIR
    """
    newid = consts.FIRSTID
    for e in entry.G_ENTRIES:
        if int(e) > newid:
            newid = int(e)
    newid += 1

    e = entry.empty_entry()
    e['id'] = str(newid)
    e['slug'] = datetime.datetime.strftime(consts.NOW, '%B-%d-%Y').lower()
    e['date'] = consts.NOW
    e['title'] = 'New Entry %s'%e['id']
    s = template.run_template_entry('empty.md', e)

    fn = os.path.join(consts.INDIR, str(newid) + entry.ENTRY_SUFFIX)
    print(fn)
    with open(fn, 'w') as fp:
        fp.write(s)

