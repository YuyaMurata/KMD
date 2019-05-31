import os
import codecs

rpath = 'G:/取得データ/データ/'

'''#KOMPAS
fd = rpath+'KOMPASデータ/data/utf8/'
file = rpath+'KOMPASデータ/layout/filename_kompas_all.csv'
header = rpath+'KOMPASデータ/layout/Layout_kompas_all.csv'
'''
'''#GCPS
fd = rpath+'GCPSデータ/data/utf8/'
file = rpath+'GCPSデータ/layout/filename_komatsucare_all.csv'
header = rpath+'GCPSデータ/layout/Layout_komatsucare_all.csv'
'''
''''#KOSMIC
fd = rpath+'KOSMICデータ/data/utf8/'
file = rpath+'KOSMICデータ/layout/filename_kosmic_all.csv'
header = rpath+'KOSMICデータ/layout/Layout_kosmic_all.csv'
'''
'''#KUEC
fd = rpath+'KUECデータ/data/utf8/'
file = rpath+'KUECデータ/layout/filename_kuec_all.csv'
header = rpath+'KUECデータ/layout/Layout_kuec_all.csv'
'''
'''#KOWA
fd = rpath+'KOWAデータ/data/utf8/'
file = rpath+'KOWAデータ/layout/filename_kowa_all.csv'
header = rpath+'KOWAデータ/layout/Layout_kowa_all.csv'
'''
'''#EQP
fd = rpath+'EQPデータ/data/utf8/'
file = rpath+'EQPデータ/layout/filename_eqp_all.csv'
header = rpath+'EQPデータ/layout/Layout_eqp_all.csv'
'''
'''
#KOMTRAX
fd = rpath+'KOMTRAXデータ/data/utf8/'
file = rpath+'KOMTRAXデータ/layout/filename_komtrax_all.csv'
header = rpath+'KOMTRAXデータ/layout/Layout_komtrax_all.csv'
'''
#LOADMAP
fd = rpath+'LOADMAPデータ/data/utf8/'
file = rpath+'LOADMAPデータ/layout/filename_loadmap_all.csv'
header = rpath+'LOADMAPデータ/layout/Layout_loadmap_all.csv'


destaxg = 'G:/axg/csv/'
root = os.listdir(fd)

#ファイル名対応表
filedict = {}
with open(file, 'r') as name:
    for line in name:
        filedict[line.split(',')[0]] = line.split(',')[1].strip()
for (k, v) in filedict.items():
    print(k+':'+v)
del filedict['FILE']

def KOMPAS_GCPS_KOSMIC_KUEC_KOWA_EQP():
    # ファイル名 -> ヘッダ
    headdict = {}
    with open(header, 'r') as head:
        for line in head:
            key = line.split(',')[0]
            if key not in headdict:
                headdict[key] = []
            headdict[key].append(line.split(',')[1].replace('\'', ''))
    for (k, v) in headdict.items():
        print(k + ':' + str(v))

    print(root)

    #ファイルの結合
    for r in root:
        #ファイルの取得
        files = os.listdir(fd+r+'/')
        fn = files[0].replace('.csv', '')

        #GCPS,KOSMIC,KUEC,EQP時は無視
        if all((s not in fn) for s in ['_', 'コマツケア', 'KOSMIC', 'sell_used', '_20170726']):
            fn = fn.split('_')[1]

        with open(destaxg+filedict[fn]+'.csv', 'wb') as csv:
            #header
            csv.write((','.join(headdict[fn])+'\n').encode())

            #データ結合
            for f in files:
                with open(fd+r+'/'+f, 'rb') as data:
                    for d in data:
                        d = d.replace(',,'.encode(), ', ,'.encode())
                        d = d.replace(',,'.encode(), ', ,'.encode())
                        d = d.replace(',\n'.encode(), ', \n'.encode())
                        csv.write(d)

def KOMTRAX():
    # ファイル名 -> ヘッダ
    headdict = {}
    with open(header, 'r') as head:
        for line in head:
            key = line.split(',')[0]

            #KOMPASに準拠
            code = line.split(',')[2].replace('\'', '')
            if code == 'KISY':
                code = '機種'
            if code == 'TYP':
                code = '型'
            if code == 'SYHK':
                code = '小変形'
            if code == 'KIBAN':
                code = '機番'

            if key not in headdict:
                headdict[key] = []

            headdict[key].append(code)
    for (k, v) in headdict.items():
        print(k + ':' + str(v))

    print(root)

    #ファイル結合
    for (f, v) in filedict.items():
        fcnt = 0
        cnt = 0
        with open(destaxg+v+'.csv', 'wb') as csv:
            # header
            csv.write((','.join(headdict[f]) + '\n').encode())
            fcnt+=1

            for r in root:
                # ファイルの取得
                files = os.listdir(fd + r)

                for file in files:
                    fn = file.replace('.csv', '')

                    #結合対象ファイル外を除外
                    if f not in fn:
                        continue

                    #print(fn)

                    #データ統合
                    with open(fd+r+'/'+file, 'rb') as data:
                        for d in data:
                            cnt+=1
                            d = d.replace(',,'.encode(), ', ,'.encode())
                            d = d.replace(',,'.encode(), ', ,'.encode())
                            d = d.replace(',\n'.encode(), ', \n'.encode())
                            csv.write(d)

            print(f+',-,'+str(fcnt)+','+str(cnt))

if __name__ == '__main__':
    KOMPAS_GCPS_KOSMIC_KUEC_KOWA_EQP()
    #KOMTRAX()