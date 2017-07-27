import unittest
import tmplr.util

class UtilTest(unittest.TestCase):
    def test_path2id(self):
        self.assertEqual(tmplr.util.path2id('/foo/bar/baz.qux'), 'baz')
        self.assertEqual(tmplr.util.path2id('baz.qux'), 'baz')
        self.assertEqual(tmplr.util.path2id('baz'), 'baz')
        self.assertEqual(tmplr.util.path2id('.qux'), '.qux') # hmmmm...
        self.assertEqual(tmplr.util.path2id(''), '')

