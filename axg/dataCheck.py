import os
import codecs
import linecache
import shutil
import codecs

#path = "G:/axg/csv/受注.csv"
path = "G:/axg/csv/PC200/PC200_KOMTRAX_CW_ERROR.csv"

with codecs.open(path, 'r', 'utf8') as f:
    for line in f:
        if 'PC200,8N1, ,311209' in line:
            print(line)