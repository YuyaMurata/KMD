import os
import shutil
import codecs
import re


#ファイルが格納される親フォルダ
path_fd = 'C:/UiPath/LoadMap/output/'
transpath_fd = 'G:/取得データ/データ/LOADMAPデータ/data/master/csv/'
csvpath_fd = 'G:/取得データ/データ/LOADMAPデータ/data/csv/'

#ファイルを変換するシェル
shell_cnt = 'parser/py_c87_count.bat'
shell_hour = 'parser/py_c87_hour.bat'

vmap = {}

def trans():
    root = os.listdir(path_fd)

    for file in root:
        if '.' in file:
            continue

        print(file)

        try:
            ''' Count File
            print('Trans_CNT>')
            os.system(shell_cnt.replace('/', '\\')+' '+path_fd.replace('/', '\\')+file)
            #os.rename(path_fd+file+"_output_count.csv", path_fd+file.replace(".txt", "")+"_output_count.csv")
            outfile1 = path_fd+file+"_output_count.csv"
            shutil.move(outfile1, outpath_fd)
            '''
            print('Trans_HOUR>')
            os.system(shell_hour.replace('/', '\\')+' '+path_fd.replace('/', '\\')+file)
            #os.rename(path_fd + file + "_output_hour.csv", path_fd + file.replace(".txt", "") + "_output_hour.csv")
            outfile2 = path_fd + file + "_output_hour.csv"
            shutil.move(outfile2, transpath_fd)
        except:
            print('no create!')

def rec(f, id, line):
    initvmap(f, id)
    s = line.replace(' ', '').replace(',\n', '\n')[:-1]
    vmap[f][id] = s

def initvmap(f, id):
    if f not in vmap:
        vmap[f] = {id : ''}

def outvmap():
    #print(vmap)

    for key in vmap:
        i=0
        #print(key)
        # フォルダ作成
        path = csvpath_fd + key + '/'
        if not os.path.isdir(path):
            os.makedirs(path)

        with codecs.open(path+key+'.csv', 'a', 'utf8') as csv:
            print(key+'='+str(len(vmap[key])))

            for id in vmap[key]:
                lines = vmap[key][id].split('\n')
                for line in lines:
                    ids = id.split('-')

                    #lineのクレンジング
                    if '～' in line:
                        line = line.replace('～', '_')
                        if line[0] != '_':
                            line = '_' + line

                    csv.write(str(i)+','+ids[0]+','+ids[1]+',,'+ids[2]+','+line+'\n')
                    i += 1

def layout():
    root = os.listdir(transpath_fd)
    file = root[0]
    with open(transpath_fd+ '/'+file, 'r') as f:
        print(id)
        lines = f.readlines()

    print('FILE,EXPLAIN,CODE,TYPE,LENGTH')

    template('LOADMAP_DATE')
    print('LOADMAP_DATE,DATE,DATE,CHAR,99')

    template('LOADMAP_SMR')
    print('LOADMAP_SMR,行名,CN,CHAR,99')
    print('LOADMAP_SMR,SMR,SMR,CHAR,99')

    s = lines[11].replace(' ', '').replace(',\n', '\n')[:-1]
    template('LOADMAP_実エンジン回転VSエンジントルク')
    for r in s.split(','):
        r = cleansing(r)
        print('LOADMAP_実エンジン回転VSエンジントルク,'+r+','+r+',CHAR,99')

    s = lines[27].replace(' ', '').replace(',\n', '\n')[:-1]
    template('LOADMAP_作業機操作状況')
    for r in s.split(','):
        r = cleansing(r)
        print('LOADMAP_作業機操作状況,'+r+','+r+',CHAR,99')

    s = lines[32].replace(' ', '').replace(',\n', '\n')[:-1]
    template('LOADMAP_ポンプ圧(MAX)')
    for r in s.split(','):
        r = cleansing(r)
        print('LOADMAP_ポンプ圧(MAX),'+r+','+r + ',CHAR,99')

    s = lines[37].replace(' ', '').replace(',\n', '\n')[:-1]
    template('LOADMAP_ポンプ圧(F)')
    for r in s.split(','):
        r = cleansing(r)
        print('LOADMAP_ポンプ圧(F),'+r+','+r + ',CHAR,99')

    s = lines[42].replace(' ', '').replace(',\n', '\n')[:-1]
    template('LOADMAP_ポンプ圧(R)')
    for r in s.split(','):
        r = cleansing(r)
        print('LOADMAP_ポンプ圧(R),'+r+','+r + ',CHAR,99')

    s = lines[47].replace(' ', '').replace(',\n', '\n')[:-1]
    template('LOADMAP_作業モード選択状況')
    for r in s.split(','):
        r = cleansing(r)
        print('LOADMAP_作業モード選択状況,'+r+','+r + ',CHAR,99')

    s = lines[52].replace(' ', '').replace(',\n', '\n')[:-1]
    template('LOADMAP_エンジン水温VS作動油温')
    for r in s.split(','):
        r = cleansing(r)
        print('LOADMAP_エンジン水温VS作動油温,'+r+','+r + ',CHAR,99')

    s = lines[69].replace(' ', '').replace(',\n', '\n')[:-1]
    template('LOADMAP_ポンプ斜板(F)')
    for r in s.split(','):
        r = cleansing(r)
        print('LOADMAP_ポンプ斜板(F),'+r+','+r + ',CHAR,99')

    s = lines[77].replace(' ', '').replace(',\n', '\n')[:-1]
    template('LOADMAP_ポンプ斜板(R)')
    for r in s.split(','):
        r = cleansing(r)
        print('LOADMAP_ポンプ斜板(R),'+r+','+r + ',CHAR,99')

    s = lines[85].replace(' ', '').replace(',\n', '\n')[:-1]
    template('LOADMAP_可変マッチング')
    for r in s.split(','):
        r = cleansing(r)
        print('LOADMAP_可変マッチング,'+r+','+r + ',CHAR,99')

def template(f):
    print(f + ',INDEX,INDEX,CHAR,99')
    print(f+',機種,KISY,CHAR,99')
    print(f + ',型,TYP,CHAR,99')
    print(f + ',小変形,SYHK,CHAR,99')
    print(f + ',機番,KIBAN,CHAR,99')

def cleansing(r):
    if '～' in r:
        r = r.replace('～', '_')
        if r[0] != '_':
            r = '_' + r

    return r

def splitData():
    root = os.listdir(transpath_fd)

    print('num_file='+str(len(root)))

    for file in root:
        id = file.split('_')[0]

        with open(transpath_fd+ '/'+file, 'r') as f:
            print(id)
            lines = f.readlines()

        #GET DATE
        #print(lines[1].split('日'))
        rec('LOADMAP_DATE', id, lines[1].split('(')[0].replace('creation date : ', '').replace('年','').replace('月',''))

        #SMR
        #print(lines[7])
        rec('LOADMAP_SMR', id, lines[7])

        #実エンジン回転VSエンジントルク
        #print(lines[10])
        #print(''.join(lines[11:24]))
        rec('LOADMAP_実エンジン回転VSエンジントルク',id, ''.join(lines[12:24]))

        # 作業機操作状況
        #print(lines[26])
        #print(''.join(lines[27:29]))
        rec('LOADMAP_作業機操作状況', id, lines[28])

        # ポンプ圧(MAX)
        #print(lines[31])
        #print(''.join(lines[32:34]))
        rec('LOADMAP_ポンプ圧(MAX)', id, lines[33])

        # ポンプ圧(F)
        #print(lines[36])
        #print(''.join(lines[37:39]))
        rec('LOADMAP_ポンプ圧(F)', id, lines[38])

        # ポンプ圧(R)
        #print(lines[41])
        #print(''.join(lines[42:44]))
        rec('LOADMAP_ポンプ圧(R)', id, lines[43])

        # 作業モード選択状況
        #print(lines[46])
        #print(''.join(lines[47:49]))
        rec('LOADMAP_作業モード選択状況', id, lines[48])

        # エンジン水温VS作動油温
        #print(lines[51])
        #print(''.join(lines[52:61]))
        rec('LOADMAP_エンジン水温VS作動油温', id, ''.join(lines[53:61]))

        # ポンプ斜板(F)
        #print(lines[68])
        #print(''.join(lines[69:74]))
        rec('LOADMAP_ポンプ斜板(F)', id, ''.join(lines[70:74]))

        # ポンプ斜板(R)
        #print(lines[76])
        #print(''.join(lines[77:82]))
        rec('LOADMAP_ポンプ斜板(R)', id, ''.join(lines[78:82]))

        # 可変マッチング
        #print(lines[84])
        #print(''.join(lines[85:87]))
        rec('LOADMAP_可変マッチング', id, lines[86])

    outvmap()

if __name__ == '__main__':
    #マスターのバイナリをCSV二変換
    #trans()
    splitData()
    layout()

