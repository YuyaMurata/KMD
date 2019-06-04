import os
import codecs
import linecache
import shutil

inpath = 'G:/axg/csv/'
kisy = 'PC200'

def extract():
    root = os.listdir(inpath)
    print('num_file='+str(len(root)))

    path = inpath+kisy+'/'

    if not os.path.isdir(path):
        print(path)
        os.makedirs(path)

    for file in root:
        if '.csv' not in file:
            continue

        print(file)
        with codecs.open(inpath+file, 'r', 'utf8') as f:
            h = next(f)
            print(h)
            if '機種' not in h:
                shutil.copy(inpath+file, path+file)
                continue

            i = h.split(',').index('機種')

            with codecs.open(path+kisy+'_'+file, 'w', 'utf8') as fw:
                fw.write(h)
                for line in f:
                    if line.split(',')[i] == kisy:
                        fw.write(line)



if __name__ == '__main__':
    extract()