import os
import codecs
import linecache
import shutil
import zipfile

#inpath = 'G:/axg/csv/'
inpath = 'G:/取得データ_20200304/KOMTRAXデータ/銭さん/ACT/'
kisy = 'PC200'
typ = [b'8', b'8N1', b'10']

def extract():
    root = os.listdir(inpath)
    print('num_file='+str(len(root)))

    path = inpath+kisy+'/temp/'

    if not os.path.isdir(path):
        print(path)
        os.makedirs(path)

    for file in root:
        if '.csv' not in file:
            continue

        #処理ファイルの限定
        if 'LOADMAP' not in file:
            continue

        print(file)
        with codecs.open(inpath+file, 'r', 'utf8') as f:
            h = next(f)
            print(h)
            if '機種' not in h:
                shutil.copy(inpath+file, path+file)
                continue

            i = h.split(',').index('機種')
            if '型式' in h:
                j = h.split(',').index('型式')
            else :
                j = h.split(',').index('型')

            with codecs.open(path+kisy+'_'+file, 'w', 'utf8') as fw:
                fw.write(h)
                for line in f:
                    if line.split(',')[i] == kisy :#and line.split(',')[j] in typ:
                        fw.write(line)

def extractZip():
    root = os.listdir(inpath)
    for file in root:
        with zipfile.ZipFile(inpath+file, 'r') as zf:
            for zfile in zf.namelist():
                with zf.open(zfile) as f:
                    with codecs.open(inpath+'CW_ACT_PC200.csv', 'ab') as fw:
                        h = f.readline().split(b'|')
                        fw.write(b','.join(h))
                        for line in f:
                            s = line.split(b'|')
                            if kisy.encode() == s[h.index(b'KIND')]:
                                if s[h.index(b'TYPE')] in typ:
                                    fw.write(line.replace(b'|', b','))

if __name__ == '__main__':
    #extract()
    extractZip()