import argparse
import bootstrap, consts, helpers, outputter, entry, template

# ###################################################################### #
# ###################################################################### #
# ###################################################################### #

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help="new|build|clean")
    parser.add_argument('-v' , '--verbose'   , dest='verbose'     , action='store_true' )
    parser.add_argument('-f' , '--force'     , dest='force'       , action='store_true' )
    parser.add_argument('-o' , '--output'    , dest='outdir'      )
    parser.add_argument('-i' , '--input'     , dest='indir'       )
    parser.add_argument('-t' , '--templates' , dest='templatedir' )
    parser.add_argument('-a' , '--assets'    , dest='assetdir'    )
    parser.add_argument('-u' , '--baseurl'   , dest='baseurl'     )

    args = parser.parse_args()
    bootstrap.configure({
        'verboase':args.verbose,
        'force':args.force,
        'outdir':args.outdir,
        'indir':args.indir,
        'templatedir':args.templatedir,
        'assetdir':args.assetdir,
        'baseurl':args.baseurl,
    })
    bootstrap.run(args.command.upper())

