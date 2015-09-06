import os, cgi
import consts, entry
from util import *

reStrip = re.compile('<[^>]*>')
reTemplateTag = re.compile('\<@([^@]+)@\>')

gTemplates = {}

def setup():
    gTemplates.clear()
    for fn in os.listdir(consts.TEMPLATEDIR):
        tm = read_template(os.path.join(consts.TEMPLATEDIR, fn))
        gTemplates[tm['id']] = tm

# ############################################################# #

def linkify_tag(tag):
    return '<a href="tag/%s.html">%s</a>'%(tag, tag)

def run_template_tag(key, entry):
    out = ''
    if key.endswith('-stripped'):
        nk = key[:key.find('-stripped')]
        out = reStrip.sub('', entry[nk])

    elif key.endswith('-escaped'):
        nk = key[:key.find('-escaped')]
        out = cgi.escape(entry[nk])

    elif key.endswith('-rfc3339'):
        nk = key[:key.find('-rfc3339')]
        out = d2s_rfc3339(entry[nk])

    elif key == 'date' or key == 'siteTimestamp':
        out = d2s(entry[key])

    elif key == 'tags':
        out = ', '.join(map(linkify_tag, entry[key]))

    else:
        out = entry[key]
    return out

def run_template_entry(tk, en):
    tm = gTemplates[tk]
    s = tm['template']
    for i in reTemplateTag.findall(s):
        nv = run_template_tag(i, en)
        s = re.sub('\<@'+i+'@\>', nv, s)
    return s

def run_template_loop(tk, baseEntry, entries, numToDo=-1):
    ekeys = entry.sorted_entry_keys(entries)
    if numToDo == -1:
        numToDo = len(ekeys)
    tm = gTemplates[tk]
    s = tm['template']
    for i in reTemplateTag.findall(s):
        nv = ''
        if i.startswith('loopentries-'):
            k = i[len('loopentries-'):]
            for key in ekeys[:numToDo]:
                nv += run_template_entry(k, entries[key]) + '\n'
        else:
            nv = run_template_tag(i, baseEntry)
        s = re.sub('\<@'+i+'@\>', nv, s)
    return s

def read_template(fn):
    s = open(fn).read()
    tail = os.path.split(fn)[-1]
    return {
        'id': tail,
        'template': s,
    }

