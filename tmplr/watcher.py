import os, time, collections
import tmplr.consts, tmplr.bootstrap
from tmplr.util import *

def watch():
    print ('Watching for changes in %s every %d seconds...'%(tmplr.consts.INDIR, tmplr.consts.WATCH_RATE))
    try:
        trigger = False
        times = collections.defaultdict(float)
        for fn in os.listdir(tmplr.consts.INDIR):
            times[fn] = os.path.getmtime(os.path.join(tmplr.consts.INDIR, fn))
        while True:
            for fn in os.listdir(tmplr.consts.INDIR):
                if fn == '%d.md'%tmplr.consts.ARCHIVEID:
                    continue
                ts = os.path.getmtime(os.path.join(tmplr.consts.INDIR, fn))
                if ts != times[fn]:
                    print ('Changed [%s] [%s]'%(fn, time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(ts))))
                    times[fn] = ts
                    trigger = True
            if trigger:
                tmplr.bootstrap.run('BUILD')
                trigger = False
            time.sleep(tmplr.consts.WATCH_RATE)
    except KeyboardInterrupt:
        print ('Done watching. Goodbye.')
        pass

