import glob
import os
import codecs
import re
import shutil

path = "G:/取得データ/KOMTRAX データ/"
out_csv = "G:/取得データ/データ/KOMTRAXデータ/data/csv/_FILE/"
split_csv = "G:/取得データ/データ/KOMTRAXデータ/data/csv/_SPLIT/"
valid_csv = "G:/取得データ/データ/KOMTRAXデータ/data/csv/_VALID/"

file_cnt = {}

#ファイルの集約
def aggregate_p(root, file):
    if 'csv' not in file:
        return

    #下記ファイルは対象から外す
    if 'CW_RECEIVE_MESSAGE' in file:
        return

    #print(file)
    if re.search('\_\d', file):
        fname = file[0:file.rfind('_')]
    else:
        fname = file.replace('.csv', '')

    #ファイル保存場所の作成
    out_path = out_csv+fname
    if(not os.path.exists(out_path)):
        os.mkdir(out_path)

    #ファイルをカウント
    if fname not in file_cnt:
        file_cnt[fname] = 0
    file_cnt[fname] += 1

    print(file + '=>' + fname+'_'+str(file_cnt[fname]))

    out = fname+'_'+str(file_cnt[fname])+'.csv'
    shutil.copyfile(root+'/'+file, out_path+'/'+out)

#機種ごとのファイル取得
def get_kisyfile(kisy, name):
    print(kisy)

    #フォルダ作成
    if not os.path.isdir(split_csv + kisy):
        os.makedirs(split_csv + kisy)

    #ファイル名を統一
    if re.search('\_\d', name):
        fname = name[0:name.rfind('_')]+'.csv'
    else:
        fname = name

    file = split_csv + kisy +'/' + fname

    #機種ファイルを読み込む
    kisyfile = codecs.open(file, 'ab', 'utf8')

    return kisyfile

#機種の分離
def split_p(fname, fcsv):
    temp = ''
    out = '\0'
    n = 0
    for data in fcsv:
        #ヘッダ情報の削除
        if 'DWH_INSERT_TIME' in data:
            continue

        #機種ごとにファイルを生成
        kisy = data.split(',')[4].replace('\"', '').replace(' ', '')
        if kisy != temp:
            out = get_kisyfile(kisy, fname)

        #一部データ表記が異なる部分が存在するため統一処理
        d = []
        for field in data.replace('\"', '').split(','):
            d.append(field.strip())

        out.write(','.join(d)+'\n')
        temp = kisy

        n += 1
        if n % 10000 == 0:
            print(str(n) + "件処理.")

def aggregate():
    for root, dirs, files in os.walk(path):
        # print(root)
        # print(dirs)
        # print(files)

        for file in files:
            aggregate_p(root, file)

    print(file_cnt)
    print(sum(file_cnt.values()))

def split():
    for root, dirs, files in os.walk(out_csv):
        # print(root)
        # print(dirs)

        for file in files:
            print(file)
            with codecs.open(root+'/'+file, 'rb', 'utf8') as f:
                split_p(file, f)

def validation():
    for root, dirs, files in os.walk(split_csv):
        #print(root)
        #print(dirs)
        #print(files)

        path = root.replace(split_csv, valid_csv)
        if not os.path.isdir(path):
            print(path)
            os.makedirs(path)

        for file in files:
            print(file)
            vmap = set()

            if os.path.isfile(path + '/' + file):
                continue

            with codecs.open(root + '/' + file, 'rb', 'utf8') as f:
                for line in f:
                    vmap.add(line)

            with codecs.open(path + '/' + file, 'wb', 'utf8') as csv:
                for line in vmap:
                    csv.write(line)

def main():
    #aggregate()
    #split()
    validation()


if __name__ == '__main__':
    main()