# Wanting to generate a simple commandline script ? Use below snipped to act as interface between the terminal and your program
# Argparse is one of the many examples to parse commandline arguments. Personally I like this module the most for parsing.

import argparse

def example_code(arguments_from_parser):
    print(arguments_from_parser)

parser = argparse.ArgumentParser(description='Testing parser, using the most default triggers and default syntax.')

# Required argument, stored in args.r
parser.add_argument('r', help="Required argument named args.r")

# '-f'and '--foo' are interchangable ways to 'trigger' this argument, using a short or long syntax. 
# The value will be stored in the Namespace using the long syntax so: args.foo (independent of the usage of -f or --foo)
# The value is required but can be placed anyware in the cmdline call to this program e.g -f 0 -b 1 is the same as -b 1 -f 0
parser.add_argument('-f','--foo', help='Description for foo argument, REQUIRED', required=True)
parser.add_argument('-b','--bar', help='Description for bar argument, REQUIRED', required=True)

# Usage of cmdline arguments, if called, will store a predetermined value
parser.add_argument('-a',action='store_true', help='If called, assign true')

#Usage of default args
parser.add_argument('-d','--debug', default=False, help="Debug argument, default is false.")

args = parser.parse_args()

# This Codeblock prevent parts of code being run when the modules are imported instead of run itself.
if __name__ == "__main__":
    example_code(args)