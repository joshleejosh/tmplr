import tmplr.consts, tmplr.helpers, tmplr.outputter, tmplr.entry, tmplr.template, tmplr.watcher

def configure(args, v, f):
    tmplr.consts.setup_consts(args, v, f)

# Assumes configure() has been called.
def run(command):
    tmplr.entry.setup()
    tmplr.template.setup()

    if command == 'CLEAN':
        print('Clean stray files out of output dir %s'%tmplr.consts.OUTDIR)
        tmplr.helpers.clean_output()

    elif command == 'NEW':
        #print('Create a new entry in note dir %s'%tmplr.consts.INDIR)
        tmplr.entry.new_entry()

    elif command == 'BUILD':
        tmplr.outputter.regenerate()
        tmplr.helpers.copy_assets()

    elif command == 'WATCH':
        tmplr.watcher.watch()

    else:
        print('Invalid command [%s]'%arg)

