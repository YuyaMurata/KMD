import csv
import os
import time
import unicodedata
import codecs
import sys

path = "E:/vmshare/komtrax"

def main():
    root = os.listdir(path)
    start = time.time()

    for folder in root:
        #if 'BR100JG' != folder:
        #    continue

        if 'Layout' in folder or 'import' in folder:
            continue
        print(folder)
        kisy = os.listdir(path+"/"+folder+'/utf8')
        for file in kisy:
            #print(file)
            f = codecs.open(path+"/"+folder+"/utf8/"+file, 'r', 'utf8')
            line = f.readline()
            if 'DWH_INSERT_TIME' in line:
                print(line)
                fw = codecs.open(path+"/"+folder+"/utf8/"+file.replace('.csv','_DATA.csv'), 'w', 'utf8')
                for line in f:
                    fw.write(line)
                fw.close()
            f.close()
            #os.remove(path+"/"+folder+"/utf8/"+file)

    stop = time.time()
    print(str(stop-start)+'s')

if __name__ == '__main__':
    main()