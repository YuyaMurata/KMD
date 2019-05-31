import codecs
import os

fn = 'G:/axg/csv/KOMTRAX_CW_ACT_DATA.csv'
path = 'G:/取得データ/データ/KOMTRAXデータ/data/utf8/'

def file_check(file):
    flg = True
    check = 0
    with codecs.open(file, 'r', 'utf8') as f:
        for line in f:
            i = len(line.split(','))
            if flg:
                print('OK:'+str(i)+':'+line)
                check = i
                flg = False

            if check != i:
                print(str(i)+':'+line)

def files_cehck():
    for root, dirs, files in os.walk(path):
        #print(root)
        #print(dirs)
        #print(files)
        if 'CW_ERROR.csv' not in files:
            continue

        fpath = root+'/'+'CW_ERROR.csv'

        print(fpath)
        file_check(fpath)


if __name__ == '__main__':
    file_check(fn)
    #files_cehck()