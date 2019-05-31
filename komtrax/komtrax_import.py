import os
import re
import csv

path = "E:/vmshare/komtrax"

def main():
    list = os.listdir(path)
    for kisy in list:
        if not re.search('[0-9]',kisy) is None:
            print(kisy)
            fw = open(path+fd+'/'+kisy+'/import_'+kisy+".txt", 'w')
            for f in os.listdir(path+fd+'/'+kisy):
                print(f)
                csvdata = csv.reader(open(path+fd+'/'+kisy+'/'+f, 'r'), quotechar='"', lineterminator='\n')


if __name__ == '__main__':
    main()