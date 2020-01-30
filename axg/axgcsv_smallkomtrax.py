import codecs

inpath = 'G:/axg/csv/PC200/'

def extract(file, exidx):
    with codecs.open(inpath+file, 'r', 'utf8') as f:
        h = next(f).split(',')

        idx = [h.index(i) for i in exidx]

        with codecs.open(inpath + 'temp/SMALL_' + file, 'w', 'utf8') as fw:
            fw.write(','.join(exidx)+'\n')
            for line in f:
                s = line.split(',')
                fw.write(','.join([s[i] for i in idx])+'\n')

if __name__ == '__main__':
    #extract('PC200_KOMTRAX_CW_GPS.csv', ['機種', '型', '機番', 'GPS_TIME', 'LATITUDE', 'LONGITUDE'])
    #extract('PC200_KOMTRAX_CW_ACT_DATA.csv', ['機種', '型', '機番', 'ACT_DATE', 'ACT_COUNT', 'DAILY_UNIT'])
    extract('PC200_KOMTRAX_CW_SERVICE_METER.csv', ['機種', '型', '機番', 'SMR_TIME', 'SMR_VALUE'])
    #extract('PC200_KOMTRAX_CW_ERROR.csv', ['機種', '型', '機番', 'ERROR_CODE', 'ERROR_TIME', 'T_TIME', 'COUNT', 'SMR_VALUE'])