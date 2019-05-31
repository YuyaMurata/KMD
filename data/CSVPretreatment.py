import csv
import os
import time
import unicodedata
import codecs
import sys

import dakuten

rpath = "G:/取得データ/データ/KOMPASデータ/data/csv"
path = "G:/取得データ/データ/KOMPASデータ/data/utf8"
header = 'チェックNO'

def cleansing(i, err_list, kana, data):
    # csv_error 回避
    for ci in range(0, len(data)):
        data[ci] = data[ci].replace('，', '_').replace(',', '_').replace('\n', '_').strip()

    line = ','.join(data)
    line = line.replace('¥¥', '\\')
    #line = line.replace('.', '_')

    if str(i) in err_list:
        print('Error Fix! {')
        print('\t' + line)
        for key in kana.keys():
            line = line.replace(key, kana[key])
        print('\tfix : ' + line)
        print('}')

    # 正規化
    line = str(line).replace('　', '')
    line = unicodedata.normalize('NFKC', line)

    if len(err_list) != 0:
        line = str(line).replace('゜', '')
        line = str(line).replace('ﾟ', '')
        line = str(line).replace('゛', '')
        line = str(line).replace('ﾞ', '')
        line = str(line).replace('´', '')
        line = str(line).replace('゚', '')
        line = str(line).replace('゙', '')
        line = str(line).replace(' ́', '')

    line = str(line).replace(' ', '').replace('\'','').strip()

    return line


def main(source, target, error):
    more = False

    #fr = open(source, 'r')
    fr = codecs.open(source, 'r', encoding='cp932', errors='replace')
    csvdata = csv.reader(fr, quotechar='"')
    fw = codecs.open(target, 'w', encoding='utf8')
    fe = codecs.open(error, 'w', encoding='utf8')

    err_list = []
    try:
        fe_index = codecs.open(error+"_index.csv", 'r', encoding='utf8')
        err_list = fe_index.read().split(',')
    except:
        fe_index = codecs.open(error+"_index.csv", 'w', encoding='utf8')

    print(err_list)

    kana = dakuten.DakutenTrans().get()

    start = time.time()
    i = 0
    d = []
    test = ""
    try:
        for data in csvdata:
            d = data
            try:
                #remove header
                if header in data or "機種" in data:
                    continue

                i += 1
                # Cleansing
                s = cleansing(i, err_list, kana, data) + '\n'
                test = s
                fw.write(s)

                if i % 10000 == 0:
                    print(str(i) + '件　データ処理。')
            except Exception as e:
                print('----------------')
                print(e)
                print('--')
                line = ','.join(data)
                try:
                    print(str(i) + ":" + line)
                    fe.write(str(i) + ":" + line + '\n')
                    if len(err_list) == 0:
                        fe_index.write(str(i) + ',')
                        more = True
                except Exception as e:
                    print(str(i))
                    print(e)


    except Exception as e:
        print(str(i))
        print(d)
        print(e)
        exit(0)


    stop = time.time()
    print('t=' + str(i) + ' time=' + str(stop - start))

    fr.close()
    fw.close()
    fe.close()
    fe_index.close()

    return more

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        path = rpath+args[1]

    flg = True

    totalstart = time.time()
    root = os.listdir(rpath)
    for folder in root:

        start = time.time()

        print(folder)

        if (folder  == 'AllSupport'):
            continue
        '''else:
            flg = False
            print('処理開始!')
        '''

        source = rpath+"/"+folder
        files = os.listdir(source)

        target = path+"/"+folder
        try:
            os.makedirs(target+"/utf8/")
            os.makedirs(target+"/error")
        except:
            print("exist folder")
        error = target + "/error"

        for filename in files:
            print(filename)
            while main(source+"/"+filename, target+"/utf8/"+filename, error+"/"+filename):
                print("error_loop!")
                #exit(0)
        stop = time.time()
        print(folder+': time=' + str(stop - start))

    total = time.time() - totalstart
    print('total time=' + str(total))