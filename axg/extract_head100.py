import codecs

inpath = 'C:/Users/zz17807/OneDrive - Komatsu Ltd/共同研究/データ確認/'
file = 'TCJUT107.csv'

with codecs.open(inpath+file, 'rb', 'UTF8') as f:
    with codecs.open(inpath+'head100_'+file, 'wb', 'SJIS') as fw:
        for i in range(0,100):
            fw.write(f.readline())