import os, copy, markdown, collections
import tmplr.consts, tmplr.template
from tmplr.util import *

ENTRY_SUFFIX = '.md'
gEntries = {}
gTags = {}

def setup():
    gEntries.clear();
    gTags.clear()
    for fn in os.listdir(tmplr.consts.INDIR):
        e = read_entry(os.path.join(tmplr.consts.INDIR, fn))
        if e['id'] != str(tmplr.consts.ARCHIVEID):
            gEntries[e['id']] = e
            read_tags(e)

""" Create an initialized entry dict """
def empty_entry():
    rv = collections.defaultdict(str)
    rv.update({
        'id':str(tmplr.consts.FIRSTID),
        'title': '',
        'slug': '',
        'blurb': '',
        'date': tmplr.consts.NOW,
        'body':'',
        'tags':[],
        'url':'',
        'siteTitle':tmplr.consts.TITLE,
        'siteBlurb':tmplr.consts.BLURB,
        'siteTimestamp': tmplr.consts.NOW,
        'baseurl':tmplr.consts.BASEURL,
        'editTimestamp':tmplr.consts.NOW,
    })
    return rv

# ############################################################# #

def parse_tags(ins):
    out = []
    for s in ins.split(','):
        s = s.strip().lower()
        if s and s not in out:
            out.append(s)
    return out

def read_entry(fn):
    oute = empty_entry()
    with open(fn) as fp:
        inHead = True
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
        oute['body'] = markdown.markdown(oute['body'], extensions=('markdown.extensions.smarty',))
    return oute

def sorted_entry_keys(entries):
    out = list(entries.keys())
    out.sort()
    if tmplr.consts.INDEX_REVERSE_TIME:
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
    for eid,entry in gEntries.items():
        if entry['date'] <= tmplr.consts.NOW:
            newe = copy.deepcopy(entry)
            rv[newe['id']] = newe
    return rv;

# ############################################################# #

# Create a new entry file in INDIR
def new_entry():
    newId = tmplr.consts.FIRSTID
    for e in gEntries.keys():
        if int(e) > newId:
            newId = int(e)
    newId += 1

    e = empty_entry()
    e['id'] = str(newId)
    e['slug'] = datetime.datetime.strftime(tmplr.consts.NOW, '%B-%d-%Y').lower()
    e['date'] = tmplr.consts.NOW
    e['title'] = 'New Entry %s'%e['id']
    s = tmplr.template.run_template_entry('empty.md', e)

    fn = os.path.join(tmplr.consts.INDIR, str(newId) + ENTRY_SUFFIX)
    print (fn)
    with open(fn, 'w') as fp:
        fp.write(s)

