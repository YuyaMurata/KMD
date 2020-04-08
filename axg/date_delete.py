import codecs

path = 'G:/取得データ/データ/KOMTRAXデータ/data/csv/_SPLIT/PC200/'
file = 'CW_GPS.csv'

date = 20170101

with codecs.open(path+file, 'rb', 'UTF8') as f:
    with codecs.open(path+file.replace('.csv', '_'+str(date)+'.csv'), 'wb', 'UTF8') as fw:
        for line in f:
            d = line.split(',')[0].split(' ')[0].replace('/', '')
            if int(d) < date:
                #列数が更新データと合わない場合の処理
                s = line.replace('\0', '').split(',')
                l = s[3:6]
                l.extend(s[7:len(s)])

                #列数を合わせたものをファイル出力
                fw.write(','.join(l))