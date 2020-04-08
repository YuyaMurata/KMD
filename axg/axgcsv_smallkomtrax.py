import codecs

#inpath = 'G:/axg/csv/PC200/'
inpath = 'G:/取得データ_20200304/KOMTRAXデータ/銭さん/'

def extract(file, exidx):
    with codecs.open(inpath+file, 'r', 'utf8') as f:
        h = next(f).split(',')

        idx = [h.index(i) for i in exidx]

        with codecs.open(inpath + 'temp/SMALL_' + file, 'w', 'utf8') as fw:
            fw.write(','.join(exidx)+'\n')
            for line in f:
                s = line.split(',')
                fw.write(','.join([s[i] for i in idx])+'\n')

def extractidx(file, exidx):
    with codecs.open(inpath+file, 'r', 'utf8') as f:
        h = next(f).split(',')

        idx = exidx

        with codecs.open(inpath + 'temp/SMALL_' + file, 'w', 'utf8') as fw:
            f.readline()
            for line in f:
                s = line.split(',')
                fw.write(','.join([s[i] for i in idx])+'\n')

if __name__ == '__main__':
    #extract('PC200_KOMTRAX_CW_GPS.csv', ['機種', '型', '機番', 'GPS_TIME', 'LATITUDE', 'LONGITUDE'])
    #extract('PC200_KOMTRAX_CW_ACT_DATA.csv', ['機種', '型', '機番', 'ACT_DATE', 'ACT_COUNT', 'DAILY_UNIT'])
    #extract('PC200_KOMTRAX_CW_SERVICE_METER.csv', ['機種', '型', '機番', 'SMR_TIME', 'SMR_VALUE'])
    #extract('PC200_KOMTRAX_CW_ERROR.csv', ['機種', '型', '機番', 'ERROR_CODE', 'ERROR_TIME', 'T_TIME', 'COUNT', 'SMR_VALUE'])
    extract('fact_daily_error.csv', ['DateTime','ErrorId', 'ErrorSMR','STime','TTIME','Model','Serial','Country2Code'])
    extract('fact_daily_smr.csv', ['LocalDate', 'SMRValueInMinutes', 'Model', 'Serial', 'Country2Code'])
    extract('fact_gps.csv', [1, 2, 3, 4, 5, 18, 19, 20, 21, 27])