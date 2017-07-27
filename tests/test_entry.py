# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from builtins import open
import unittest, sys, os, tempfile, shutil
import tmplr.entry

class EntryTest(unittest.TestCase):
    def setUp(self):
        if sys.version_info < (3, 0):
            self.assertCountEqual = self.assertItemsEqual
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        try:
            shutil.rmtree(self.tempdir)
        except OSError:
            pass

    def test_empty(self):
        fn = os.path.join(self.tempdir, 't')
        with open(fn, 'w') as fp:
            fp.write('')
        e = tmplr.entry.read_entry(fn)
        self.assertEqual(e['id'], 't')
        self.assertEqual(e['title'], '')
        self.assertEqual(e['slug'], '')
        self.assertEqual(e['blurb'], '')
        self.assertCountEqual(e['tags'], [])

    def test_read(self):
        fn = os.path.join(self.tempdir, 't')
        with open(fn, 'w', encoding='utf-8') as fp:
            fp.write("""title:Test Éntry    
slug: test-éntry    
date: 2016-09-27 15:27:38    
blurb: 	     A   tést post for testing.    
tags: test, unittést, tag test,     

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur.

Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
""")

        e = tmplr.entry.read_entry(fn)
        self.assertEqual(e['id'], 't')
        self.assertEqual(e['title'], 'Test Éntry')
        self.assertEqual(e['slug'], 'test-éntry')
        self.assertEqual(e['blurb'], 'A   tést post for testing.')
        self.assertCountEqual(e['tags'], ['test', 'unittést', 'tag test'])

