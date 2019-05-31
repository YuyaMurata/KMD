import codecs
import os
import time
import sys

fd = 'komtrax'
rpath = "E:/vmshare/"+fd+"/"
path1 = "E:/vmshare/"+fd+"/cp932/"
path2 = "E:/vmshare/"+fd+"/utf8/"

def main():
    os.mkdir(path2)
    files = os.listdir(path1)

    start = time.time()

    for fname in files:
        print(fname)
        filename = fname.replace('NEW_', '').replace('.csv', '_DATA.csv')
        fin = codecs.open(path1+fname, 'r')
        fout = codecs.open(path2+filename, 'w', 'utf8')

        header = fin.readline()

        test = True
        for line in fin:
            test = False
            fout.write(line)

        if test:
            continue

        fin.close()
        fout.close()

    stop = time.time()

    print(str(stop-start)+'s')

def komtrax():
    files = os.listdir(rpath)
    start = time.time()

    for fname in files:
        if 'komtrax' in fname:
            continue
        print(fname)

        fpath1 = path1.replace(fd, fd + '/' + fname)
        fpath2 = path2.replace(fd, fd + '/' + fname)

        if not os.path.isdir(fpath2):
            os.mkdir(fpath2)

        csvs = os.listdir(fpath1)

        for csvname in csvs:
            print(csvname)

            fin = open(fpath1+csvname, 'r')
            fout = codecs.open(fpath2+csvname, 'w', 'utf8')

            #header
            fin.readline()

            for line in fin:
                fout.write(line)

            fin.close()
            fout.close()

    stop = time.time()
    print(str(stop - start) + 's')



if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        fd = args[1]

    #main()
    komtrax()