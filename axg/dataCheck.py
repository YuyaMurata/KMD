import os
import codecs
import linecache
import shutil

path = "G:/取得データ/データ/KOMTRAXデータ/data/utf8/PC200/CW_SERVICE_METER.csv"

with open(path, 'r') as f:
    for line in f:
        if 'PC200,8N1,,314601,' in line:
            print(line)