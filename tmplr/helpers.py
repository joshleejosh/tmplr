# -*- coding: utf-8 -*-
import os, shutil, glob, re
from . import entry, consts

def copy_assets():
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
    newId = consts.FIRSTID
    for e in gEntries:
        if int(e) > newId:
            newId = int(e)
    newId += 1

    e = empty_entry()
    e['id'] = str(newId)
    e['slug'] = datetime.datetime.strftime(consts.NOW, '%B-%d-%Y').lower()
    e['date'] = consts.NOW
    e['title'] = 'New Entry %s'%e['id']
    s = template.run_template_entry('empty.md', e)

    fn = os.path.join(consts.INDIR, str(newId) + ENTRY_SUFFIX)
    print(fn)
    with open(fn, 'w') as fp:
        fp.write(s)

