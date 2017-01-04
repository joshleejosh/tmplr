import datetime, re, os

def s2d(s):
    return datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')

def d2s(d):
    return datetime.datetime.strftime(d, '%B %d, %Y')

def d2s_dt(d):
    return datetime.datetime.strftime(d, '%Y-%m-%d %H:%M:%S')

def d2s_rfc3339(d):
    return d.isoformat('T') + 'Z'

def path2id(fn):
    return os.path.splitext(os.path.basename(fn))[0]
    #return re.sub('^.*/([^.]+)\..*$', '\\1', fn)

