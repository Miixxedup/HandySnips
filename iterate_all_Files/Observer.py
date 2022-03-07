# This class will keep track of all the files seen and possible duplicates.

import os
from pprint import pprint
from collections import namedtuple

class Observer:
    def __init__(self):
        self.obsvr_tuple = namedtuple("Observer_Data", ['filename','filepaths'])
        self.files_dict = {}

    def process_filename(self, filepath):
        if os.path.isfile(filepath):
            
            # Collect last result from split
            filename = filepath.split("\\")[-1]
            
            # Update existing entry
            if filename in self.files_dict:
                self.files_dict[filename].append([(self.obsvr_tuple(filename, [filepath]))])
            # Add new
            else:
            
                self.files_dict[filename] = [(self.obsvr_tuple(filename, [filepath]))]
        else:
            pass
    
    # Returns an overview of all files found and 
    def return_stats(self):
        pprint(self.files_dict)




