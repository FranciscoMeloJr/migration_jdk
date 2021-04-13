# Migration CLI
import argparse

import os
import sys

#Migration JDK python:
import migration_jdk11

# Create the parser
my_parser = argparse.ArgumentParser(description='Migration JDK 11 Helper', usage='python migration_cli.py -path')

my_parser.add_argument('-v',
                       '--verbose',
                       action='store_true',
                       help='shows debug logs')

my_parser.add_argument('-p', '--path', action='store', type=str, required=False, help='The path of the source directory to do the migration to JDK 11. In case none is given, current path is used')

my_parser.add_argument('-g', '--guide', action='store', type=str, required=False, help='This Migration Toolkit is based on Oracle JDK Migration Guide. Found on https://docs.oracle.com/en/java/javase/11/migrate/migration-guide.pdf')

my_parser.add_argument('-jmc', action='store', type=str, required=False, help='In JDK 11, JMC is available as a standalone package and not bundled in the JDK')

# Execute the parse_args() method
args = my_parser.parse_args()

if args.path:
	input_path = args.path
	if not os.path.isdir(input_path):
	    print('The path specified does not exist')
	    sys.exit()
	else:
		print "Path will be " + input_path
		migration_jdk11.main()
else:
	print('Migration JDK 11 Helper. Select one option: -h for Help')
	sys.exit()