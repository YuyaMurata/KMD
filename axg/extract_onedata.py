import os
import codecs
import re
import shutil

path = "G:/axg/csv/"
id = 'PC200-8- -351185'

def extract():
    root = os.listdir(path)
    print('num_file='+str(len(root)))

    outpath = path + 'temp/'

    if not os.path.isdir(outpath):
        print(outpath)
        os.makedirs(outpath)

    for file in root:
        if '.csv' not in file:
            continue

        #処理ファイルの限定
        if 'KOMTRAX_CW_SERVICE_METER' not in file:
            continue

        print(file)
        with codecs.open(path+file, 'r', 'utf8') as f:
            h = next(f)
            print(h)
            if '機種' not in h:
                continue

            i = h.split(',').index('機種')
            if '型式' in h:
                j = h.split(',').index('型式')
            else :
                j = h.split(',').index('型')
            k = h.split(',').index('機番')

            with codecs.open(outpath+id+'_'+file, 'w', 'sjis') as fw:
                fw.write(h)
                for line in f:
                    if line.split(',')[i] == id.split('-')[0] and line.split(',')[k] == id.split('-')[3]:
                        fw.write(line)

if __name__ == '__main__':
    extract()