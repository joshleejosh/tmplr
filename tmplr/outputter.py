# -*- coding: utf-8 -*-
"""
The part where we actually generate the pages.
"""

from __future__ import unicode_literals
from builtins import open
import os
from . import consts, entry, template
from .util import s2d


def generate_entries():
    """
    Generate individual entry pages.
    """
    out = 0
    for iid, e in entry.get_entries().items():
        fn = os.path.join(consts.OUTDIR, e['slug'] + '.html')
        doit = True
        if os.path.exists(fn):
            ts = os.path.getmtime(fn)
            if ts > e['editTimestamp']:
                doit = False
        if doit or consts.FORCE:
            print('Generate entry %s'%iid)
            with open(fn, 'w', encoding='utf-8') as fp:
                fp.write(template.run_template_entry('htmlHead.html', e))
                fp.write(template.run_template_entry('entry.html', e))
                fp.write(template.run_template_entry('htmlFoot.html', e))
            out += 1
    return out

def generate_index():
    """
    Generate the index page.
    """
    print('Generate index')
    entries = entry.get_entries()
    fn = os.path.join(consts.OUTDIR, 'index.html')
    with open(fn, 'w', encoding='utf-8') as fp:
        ie = entry.empty_entry()
        ie['title'] = consts.INDEX_TITLE
        ie['blurb'] = consts.BLURB
        fp.write(template.run_template_entry('htmlHead.html', ie))
        fp.write(template.run_template_loop('index.html', ie, entries, consts.NUM_INDEX_ENTRIES))
        fp.write(template.run_template_entry('htmlFoot.html', ie))

    # write a faked entry back to the input dir(!)
    fn = os.path.join(consts.INDIR, '%d.md'%consts.ARCHIVEID)
    with open(fn, 'w', encoding='utf-8') as fp:
        template.run_template_entry('empty.md', ie)
        ekeys = entry.sorted_entry_keys(entries)
        for k in ekeys[:consts.NUM_INDEX_ENTRIES]:
            e = entries[k]
            url = '%s/%s.html'%(consts.BASEURL, e['slug'])
            fp.write('<a href="%s">%s</a>\n\n'%(url, e['title']))

def generate_archive_entry():
    """
    Create a meta-entry with links to all other entries.
    """
    aeid = consts.ARCHIVEID
    print('Generate archive as entry %d'%aeid)
    oute = entry.empty_entry()
    oute['id'] = aeid
    oute['title'] = consts.ARCHIVE_TITLE
    oute['slug'] = 'archive'
    oute['date'] = s2d('2013-09-25 12:00:00')
    oute['blurb'] = 'A list of all %s posts.'%consts.TITLE
    oute['url'] = '' + oute['slug'] + '.html'
    oute['body'] = '<ul class="archive">\n'
    entries = entry.get_entries()
    for k in entry.sorted_entry_keys(entries):
        oute['body'] += '<li><a href="%s">%s</a></li>\n'%(entries[k]['title'])
    oute['body'] += '</ul>\n'
    entries[oute['id']] = oute

def generate_archive():
    """
    Generate the archive page.
    """
    print('Generate archive')
    fn = os.path.join(consts.OUTDIR, 'archive.html')
    with open(fn, 'w', encoding='utf-8') as fp:
        ie = entry.empty_entry()
        ie['title'] = consts.ARCHIVE_TITLE
        ie['blurb'] = ''
        fp.write(template.run_template_entry('htmlHead.html', ie))
        fp.write(template.run_template_loop('archive.html', ie, entry.get_entries()))
        fp.write(template.run_template_entry('htmlFoot.html', ie))

def generate_feed():
    """
    Generate the site rss/atom feed.
    """
    print('Generate feed')
    fn = os.path.join(consts.OUTDIR, 'feed.xml')
    with open(fn, 'w', encoding='utf-8') as fp:
        ie = entry.empty_entry()
        ie['title'] = 'Feed'
        ie['blurb'] = 'Feed for %s'%consts.TITLE
        fp.write(template.run_template_loop('feed.xml',
                                            ie, entry.get_entries(),
                                            consts.NUM_INDEX_ENTRIES))

def generate_tags():
    """
    Generate a tag archive page.
    """
    print('Generate tags')
    for tag, eids in entry.G_TAGS.items():
        srcentries = entry.get_entries()
        entries = {}
        for eid in eids:
            entries[eid] = srcentries[eid]
        fn = os.path.join(consts.OUTDIR, 'tag', tag + '.html')
        with open(fn, 'w') as fp:
            ie = entry.empty_entry()
            ie['title'] = 'Posts tagged "%s"'%tag
            ie['blurb'] = 'Posts tagged "%s"'%tag
            fp.write(template.run_template_entry('htmlHead.html', ie))
            fp.write(template.run_template_loop('tag.html', ie, entries))
            fp.write(template.run_template_entry('htmlFoot.html', ie))

def regenerate():
    """
    Generate everything.
    """
    #generate_archive_entry()
    numprocessed = generate_entries()
    if numprocessed > 0:
        generate_index()
        generate_archive()
        generate_feed()
        #generate_tags()

