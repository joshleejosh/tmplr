import os
import tmplr.consts, tmplr.entry, tmplr.template
from tmplr.util import *


# ###################################################################### #
# ###################################################################### #
# ###################################################################### #

def generate_entries():
    out = 0
    for id,e in tmplr.entry.get_entries().items():
        fn = os.path.join(tmplr.consts.OUTDIR, e['slug'] + '.html')
        doit=True
        if os.path.exists(fn):
            ts = os.path.getmtime(fn)
            if ts > e['editTimestamp']:
                doit=False
        if doit or tmplr.consts.FORCE:
            print ('Generate entry %s'%id)
            with open(fn, 'w') as fp:
                fp.write(tmplr.template.run_template_entry('htmlHead.html', e))
                fp.write(tmplr.template.run_template_entry('entry.html', e))
                fp.write(tmplr.template.run_template_entry('htmlFoot.html', e))
            out += 1
    return out

def generate_index():
    print ('Generate index')
    entries = tmplr.entry.get_entries()
    fn = os.path.join(tmplr.consts.OUTDIR, 'index.html')
    with open(fn, 'w') as fp:
        ie = tmplr.entry.empty_entry()
        ie['title'] = tmplr.consts.INDEX_TITLE
        ie['blurb'] = tmplr.consts.BLURB
        fp.write(tmplr.template.run_template_entry('htmlHead.html', ie))
        fp.write(tmplr.template.run_template_loop('index.html', ie, entries, tmplr.consts.NUM_INDEX_ENTRIES))
        fp.write(tmplr.template.run_template_entry('htmlFoot.html', ie))

    # write a faked entry back to the input dir(!)
    fn = os.path.join(tmplr.consts.INDIR, '%d.md'%tmplr.consts.ARCHIVEID)
    with open(fn, 'w') as fp:
        s = tmplr.template.run_template_entry('empty.md', ie)
        ekeys = tmplr.entry.sorted_entry_keys(entries)
        for k in ekeys[:tmplr.consts.NUM_INDEX_ENTRIES]:
            e = entries[k]
            url = '%s/%s.html'%(tmplr.consts.BASEURL, e['slug'])
            fp.write('<a href="%s">%s</a>\n\n'%(url, e['title']))

# create a meta-entry with links to all other entries.
def generate_archive_entry():
    aeid = tmplr.consts.ARCHIVEID
    print ('Generate archive as entry %d'%aeid)
    oute = tmplr.entry.empty_entry()
    oute['id'] = aeid
    oute['title'] = tmplr.consts.ARCHIVE_TITLE
    oute['slug'] = 'archive'
    oute['date'] = s2d('2013-09-25 12:00:00')
    oute['blurb'] = 'A list of all %s posts.'%tmplr.consts.TITLE
    oute['url'] = '' + oute['slug'] + '.html'
    oute['body'] = '<ul class="archive">\n'
    entries = tmplr.entry.get_entries()
    for k in tmplr.entry.sorted_entry_keys(entries):
        oute['body'] += '<li><a href="%s">%s</a></li>\n'%(entries[k]['title'])
    oute['body'] += '</ul>\n'
    entries[oute['id']] = oute

def generate_archive():
    print ('Generate archive')
    fn = os.path.join(tmplr.consts.OUTDIR, 'archive.html')
    with open(fn, 'w') as fp:
        ie = tmplr.entry.empty_entry()
        ie['title'] = tmplr.consts.ARCHIVE_TITLE
        ie['blurb'] = ''
        fp.write(tmplr.template.run_template_entry('htmlHead.html', ie))
        fp.write(tmplr.template.run_template_loop('archive.html', ie, tmplr.entry.get_entries()))
        fp.write(tmplr.template.run_template_entry('htmlFoot.html', ie))

def generate_feed():
    print ('Generate feed')
    fn = os.path.join(tmplr.consts.OUTDIR, 'feed.xml')
    with open(fn, 'w') as fp:
        ie = tmplr.entry.empty_entry()
        ie['title'] = 'Feed'
        ie['blurb'] = 'Feed for %s'%tmplr.consts.TITLE
        fp.write(tmplr.template.run_template_loop('feed.xml', ie, tmplr.entry.get_entries(), tmplr.consts.NUM_INDEX_ENTRIES))

def generate_tags():
    print ('Generate tags')
    for tag,eids in gTags.items():
        srcentries = tmplr.entry.get_entries()
        entries = {}
        for eid in eids:
            entries[eid] = srcentries[eid]
        fn = os.path.join(tmplr.consts.OUTDIR, 'tag', tag + '.html')
        with open(fn, 'w') as fp:
            ie = tmplr.entry.empty_entry()
            ie['title'] = 'Posts tagged "%s"'%tag
            ie['blurb'] = 'Posts tagged "%s"'%tag
            fp.write(tmplr.template.run_template_entry('htmlHead.html', ie))
            fp.write(tmplr.template.run_template_loop('tag.html', ie, entries))
            fp.write(tmplr.template.run_template_entry('htmlFoot.html', ie))

def regenerate():
    #generate_archive_entry()
    numProcessed = generate_entries()
    if numProcessed > 0:
        generate_index()
        generate_archive()
        generate_feed()
        #generate_tags()

