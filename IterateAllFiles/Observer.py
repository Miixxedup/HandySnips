# This class will keep track of all the files seen and possible duplicates.

import os
from pprint import pprint
from collections import namedtuple

class Observer:
    def __init__(self):
        self.obsvr_tuple = namedtuple("Observer_Data", ['filename','filepaths','occ'])
        self.files_tuples = []

    def process_filename(self, filepath):
        if os.path.isfile(filepath):
            # Collect last result from split
            filename = filepath.split("\\")[-1]
            
            for entry in self.files_tuples:
                # Update existing entry
                if entry.filename == filename:
                    entry.filepaths.append(filepath)
                    entry.occ = entry.occ + 1
            else:
                # Add new
                self.files_tuples.append(self.obsvr_tuple(filename, [filepath], 1))
        else:
            # Not a File
            pass
    
    def return_stats(self):
        pprint(self.files_tuples)




