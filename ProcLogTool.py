#! python3
# Check ECM Proc logs for Manage invn qty/cost being OFF.
# Returns list of log files where a Proc IN occured and Manage invn qty/cost was OFF.
# Written by Zach Cutberth

import os
import fnmatch



for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '*.log'):
        if 'Processing In;' in open(filename).read():
            if 'Manage invn qty/cost, price, desc, committed: OFF,' in open(filename).read():
                print(filename)
                with open('results.txt', 'a') as results:
                    results.write(filename + '\n')
