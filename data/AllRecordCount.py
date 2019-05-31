import csv
import os
import time
import unicodedata
import codecs
import sys

path="G:/取得データ/データ"
cnt = 0
total_rec = 0

def main():
    root = os.listdir(path)
    start = time.time()

    for folder in root:
        print(folder)
        dpath = path+"/"+folder+"/data/csv"
        df = os.listdir(dpath)
        for fd in df:
            if ".csv" in fd:
                csvCount(fd, dpath+"/"+fd)
            else:
                files = os.listdir(dpath+"/"+fd)
                for f in files:
                    csvCount(f, dpath + "/" + fd + "/" + f)


def csvCount(name, fpath):
    global cnt, total_rec
    cnt += 1
    rec = 0

    fr = open(fpath, 'r', errors='replace')
    csvdata = csv.reader(fr)
    for line in csvdata:
        rec += 1

    print("  "+name+","+str(rec))
    total_rec += rec


if __name__ == '__main__':
    start = time.time()

    main()

    stop = time.time() - start
    print("Time," + str(stop) + ", File Count,"+str(cnt))