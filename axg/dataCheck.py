import os
import codecs
import linecache
import shutil
import codecs

#path = "G:/axg/csv/受注.csv"
path = "G:/axg/error/komatsuDB_PC200/error_受注作業明細.csv"

with codecs.open(path, 'r', 'sjis') as f:
    for line in f:
        if 'FN,5A1560253,' in line:
            print(line)