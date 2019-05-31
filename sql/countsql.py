import codecs
import csv
import os

#path = "E:/vmshare/komtrax/"
path = "C:/Users/zz17390/Documents/NetBeansProjects/KomatsuAnalyze/resource/importset/layout/disable/"
#path = "C:/Users/zz17390/Documents/NetBeansProjects/KomatsuAnalyze/resource/importset/layout/enable/"

def main():
    files = os.listdir(path)
    for fd in files:
        if 'Layout' in fd:
            print('SELECT count(*) from ' + fd.replace("Layout_","").replace(".csv","")+";")


if __name__ == '__main__':
    main()