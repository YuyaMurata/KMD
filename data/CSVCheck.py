import os
import time
import datetime
import csv

path = "C:/Users/zz17390/vmshare/EQP_M/cp932/"

def main():
    files = os.listdir(path)
    for fname in files:
        csvdata = csv.reader(open(path+fname, 'r'), lineterminator='\n')
        print(fname)
        i = 0

        leng = 0
        try:
            for row in csvdata:
                if i == 0:
                    leng = len(row)
                i += 1

                try:
                    if leng != len(row):
                      raise ValueError
                    #print(stamp)
                except:
                    print(fname+":"+str(i)+' - '+row)
        except:
            print(str(i))
            exit(0)
        print(str(i)+'件')


if __name__ == '__main__':
    main()