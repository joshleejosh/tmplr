import consts, helpers, outputter, entry, template

def configure(args):
    consts.setup_consts(args)

# Assumes configure() has been called.
def run(command):
    entry.setup()
    template.setup()

    if command == 'CLEAN':
        print 'Clean stray files out of output dir %s'%consts.OUTDIR
        helpers.clean_output()

    elif command == 'NEW':
        #print 'Create a new entry in note dir %s'%consts.INDIR
        entry.new_entry()

    elif command == 'BUILD':
        outputter.regenerate()
        helpers.copy_assets()

    else:
        print 'Invalid command [%s]'%arg

