import gzip
import os
import codecs
import csv
import unicodedata
import linecache


path = 'G:/取得データ_20200304/'
outpath = path+'out/'

def aggregateFile(path):
    #出力先の作成
    out = outpath + 'master/'
    if not os.path.isdir(out):
        print(out)
        os.makedirs(out)

    #ファイルを種類ごとに集約
    for root, dirs, files in os.walk(path):
        print('num_file='+str(len(root)))
        if 'out' in root:
            continue

        #CSV以外の除去
        csvfiles = [s for s in files if '.csv' in s]

        for file in csvfiles:
            #file ID
            fid = out+file.split('_')[1].replace('.gz', '').replace('.csv', '')+'.csv'
            print(fid)

            #Resume
            if 'ERROR' not in file:
                continue

            #集約処理
            if '.gz' in file:
                with gzip.open(root+'/'+file, mode='rt') as f:
                    with codecs.open(fid, 'ab', 'UTF8') as fw:
                        for line in f:
                            fw.write(line.replace('\0', ''))
            else:
                try:
                    with open(root+'/'+file, 'r') as f:
                        with codecs.open(fid, 'ab', 'UTF8') as fw:
                            for line in f:
                                fw.write(line.replace('\0', ''))
                except UnicodeDecodeError:
                    with codecs.open(root+'/'+file, 'r', 'shift_jisx0213') as f:
                        with codecs.open(fid, 'ab', 'UTF8') as fw:
                            for line in f:
                                fw.write(line.replace('\0', ''))

def file_preprocess(path, f):
    with codecs.open(f, 'r', 'UTF8') as fr:
        head = linecache.getline(f, 1)
        if "','" in head:
            print('single : '+head) #(line.replace('\0','') for line in fr),
            data = csv.reader(fr, delimiter=",", quotechar="'")
        else:
            print('double : '+head)
            data = csv.reader(fr, delimiter=",", quotechar='"')
        linecache.clearcache()

        with codecs.open(path, 'w', 'UTF8') as fw:
            csvfw = csv.writer(fw, delimiter=",", escapechar='\\', quoting=csv.QUOTE_NONE)

            for d in data:
                for ci in range(0, len(d)):
                    # 各項目の修正  カンマと改行を削除
                    d[ci] = d[ci].replace('，', '').replace(',', '').replace('　', ' ').replace('\n', '').replace('\0','').strip()

                    #半角カタカナの排除
                    d[ci] = unicodedata.normalize('NFKC', d[ci])
                csvfw.writerow(d)


def preprocess(outpath):
    # 出力先の作成
    out = outpath + 'cleansing/'
    if not os.path.isdir(out):
        print(out)
        os.makedirs(out)

    master = outpath+'master/'
    files = os.listdir(master)

    # CSV以外の除去
    csvfiles = [s for s in files if '.csv' in s]

    for file in csvfiles:
        print(file)
        #クレンジングファイルが存在しないとき実行
        if not os.path.isfile(out+file):
            file_preprocess(out+file, master+file)

def columnCheck(file, line, header):
    if(len(line.split(',')) !=  len(header)):
        print(file + ':file header equal - ' + str(len(line.split(','))) + ' == ' + str(len(header)))
        print("    " + line.replace('\n', ''))
        print("    " + str(header))
        return False
    return True

def joinheader(outpath):
    #ヘッダが存在しない場合にヘッダを追加
    clean = outpath + 'cleansing/'
    header_path = outpath + 'layout/file_header.csv'
    header_dict = {}

    out = outpath + 'axg/'
    if not os.path.isdir(out):
        print(out)
        os.makedirs(out)

    with open(header_path, 'r') as h:
        h.readline()
        for line in h:
            s = [x for x in line.split(',') if not x.strip() == '']
            header_dict[s[0]+'.csv'] = s[1:len(s)]
    print(header_dict)

    files = os.listdir(clean)
    # CSV以外の除去
    csvfiles = [s for s in files if '.csv' in s]

    for file in csvfiles:
        print(file)

        if os.path.isfile(out + file):
           continue

        h = header_dict[file]
        with codecs.open(clean+file, 'r', 'UTF8') as f:
            with codecs.open(out+file, 'w', 'UTF8') as fw:
                line = f.readline()
                if(line.split(',')[0] == h[0]):
                    fw.write(','.join(h)+'\n')
                else:
                    fw.write(','.join(h)+'\n')
                    fw.write(line)

                for line in f:
                    if not columnCheck(file, line, h):
                        exit(0)
                    fw.write(line)



if __name__ == '__main__':
    #aggregateFile(path)
    #preprocess(outpath)
    joinheader(outpath)