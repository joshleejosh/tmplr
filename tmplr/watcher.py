import os, time, collections
import consts, bootstrap
from util import *

def watch():
    print ('Watching for changes in %s every %d seconds...'%(consts.INDIR, consts.WATCH_RATE))
    try:
        trigger = False
        times = collections.defaultdict(float)
        for fn in os.listdir(consts.INDIR):
            times[fn] = os.path.getmtime(os.path.join(consts.INDIR, fn))
        while True:
            for fn in os.listdir(consts.INDIR):
                if fn == '%d.md'%consts.ARCHIVEID:
                    continue
                ts = os.path.getmtime(os.path.join(consts.INDIR, fn))
                if ts != times[fn]:
                    print ('Changed [%s] [%s]'%(fn, time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(ts))))
                    times[fn] = ts
                    trigger = True
            if trigger:
                bootstrap.run('BUILD')
                trigger = False
            time.sleep(consts.WATCH_RATE)
    except KeyboardInterrupt:
        print ('Done watching. Goodbye.')
        pass

