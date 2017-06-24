import os, os.path, subprocess, shutil, glob, re
import outputter, entry, consts

PROCC='/usr/bin/processing-java'
PROCDIR='shrdr'

def copy_assets():
    for f in glob.glob(os.path.join(consts.ASSETDIR, '*')):
        if not os.path.isdir(f):
            shutil.copy(f, consts.OUTDIR)

"""
Scrub out files that don't correspond to actual entries.
"""
def clean_output():
    todel = []
    for fn in glob.glob(os.path.join(consts.OUTDIR, '*.html')):
        fslug = re.sub('\.html.*$', '', re.sub('^.*\/', '', fn))
        if fslug == 'archive' or fslug == 'index':
            continue
        hit = False
        for id,e in entry.get_entries().items():
            if fslug == e['slug']:
                hit = True
                break
        if not hit:
            todel.append(fn)

    for fn in todel:
        print ('Deleting stray file %s'%fn)
        os.remove(fn)

