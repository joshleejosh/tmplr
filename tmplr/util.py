# -*- coding: utf-8 -*-
"""
Misc. low-level functions.
"""

import datetime
import os

def s2d(s):
    """
    String to date from the entry date format.
    """
    return datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')

def d2s(d):
    """
    Date to string in friendly format, without time.
    """
    return datetime.datetime.strftime(d, '%B %d, %Y')

def d2s_dt(d):
    """
    Date to string in entry date format.
    """
    return datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')

def d2s_rfc3339(d):
    """
    Date to string in the format expected by Atom feeds.
    """
    return d.isoformat('T') + 'Z'

def path2id(fn):
    """
    Get an entry ID from a filename.
    """
    return os.path.splitext(os.path.basename(fn))[0]
    #return re.sub('^.*/([^.]+)\..*$', '\\1', fn)

