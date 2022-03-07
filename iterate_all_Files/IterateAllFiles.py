# Method to combine a PATHNAME and Glob regex basic
# Replace PATHNAME with a starting place like C:/
# Replace GLOB with a regex like structure to catch all files e.g. *.txt for all txt files
# Replace RECURSIVE with false if only the given PATHNAME with GLOB should be checked, otherwise use 'True' for a recursive loop into each lower folder

# Personal note: To scan ALL files, only change the do_something_with_filepath method and do not alter PATHNAME and GLOB.
# The imported 'Observer.py' will be used to keep track of the scanned files and returns an overview.

import glob
import os
from Observer import Observer

PATHNAME = r"C:\Users\%s\Downloads" % os.getlogin()
GLOB = r"\**"
RECURSIVE = True

def main():
    
    print("[*] Initializing Observer")
    obsvr = Observer()
    
    print("[*] Starting the iteration loop")
    for filepath in glob.iglob(PATHNAME + GLOB, recursive=RECURSIVE):
        obsvr.process_filename(filepath)
        do_something_with_filepath(filepath)
    
    print("[*] Printing Observed Files")
    obsvr.return_stats()

def do_something_with_filepath(path):
    if path.endswith(".exe"):
        print(f"\t{path}")

# This Codeblock prevent parts of code being run when the modules are imported instead of run itself.
if __name__ == "__main__":
    main()
