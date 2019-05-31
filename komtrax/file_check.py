import os
import csv
import codecs

def komtrax_define():
    path = "C:/Users/zz17807/Documents/NetBeansProjects/KomatsuAnalyze/define/komtrax_data_define.csv"
    with codecs.open(path, 'r', 'utf8') as f:
        c = csv.reader(f)
        next(c)

        kmdef = {}
        for row in c:
            kmdef[row[0]] = row[3]

    print(kmdef)
    return kmdef

def header(p):
    _header = []
    for file in os.listdir(p):
        if 'Layout' in file:
            h = file.replace('Layout_', '').replace('komtrax_CW_', '').replace('.csv', '')
            _header.append(h)

    return _header

def komtrax():
    path = "E:/vmshare/komtrax"
    h = header(path)
    writeline("komtrax.csv", '機種,'+','.join(h))
    print(h)

    kmdef = komtrax_define()
    writeline('komtrax.csv', ','+ ','.join([kmdef[_h] for _h in h]))

    flg = True
    for root, dirs, files in os.walk(path):
        if flg: #komtraxフォルダのルート情報の読み込みを飛ばす
            flg = False
            continue

        print(root)
        #print(dirs)
        #print(files)

        d = []
        for _h in h:
            if 'CW_'+_h+'.csv' in files:
                d.append('1')
            else:
                d.append('0')
        writeline("komtrax.csv", root.replace('E:/vmshare/komtrax\\', '')+','+','.join(d))

def writeline(fname, s):
    with open(fname, 'a') as f:
        f.write(s+'\n')

if __name__ == '__main__':
    komtrax()