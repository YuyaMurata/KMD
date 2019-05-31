import codecs
import csv
import os

path = "E:/vmshare/komtrax/"

def main():
    files = os.listdir(path)
    for fd in files:
        if 'Layout' in fd:
            print('DROP TABLE ' + fd.replace("Layout_","").replace(".csv","")+";")


if __name__ == '__main__':
    main()