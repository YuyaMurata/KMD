import codecs
import re

def create():
    dic = {}
    with codecs.open("G:/axg/csv/EQP車両マスタ.csv", 'r', 'utf8', 'ignore') as eqp:
        for line in eqp:
            s = line.split(',')[0]+'-'+line.split(',')[3]
            dic[s] = line.replace(',,',', ,').split(',')[0:4]

    print(dic)

    mt = {}
    with codecs.open("G:/axg/csv/KOMPAS車両マスタ.csv", 'r', 'utf8', 'ignore') as kompas:
        for line in kompas:
            s = line.split(',')[1] + '-' +line.split(',')[2]

            if s not in dic.keys():
                continue

            mt[s] = line.split(',')[18]

            print(s)

    with codecs.open("G:/axg/csv/製造データ_201703.csv", 'r', 'utf8', 'ignore') as product:
        for line in product:
            s = line.split(',')[0]
            d = line.split(',')[1]

            if s not in mt.keys():
                continue

            if mt[s] == '':
                mt[s] = d+'01'.encode()

    #CSV
    with codecs.open("G:/axg/csv/車両マスタ.csv", 'w', 'utf8', 'ignore') as syaryo:
        for (k, v) in mt.items():
            s = ','.join(dic[k])+','+v+'\n'
            syaryo.write(s)

def kisy(k,ptn):
    with codecs.open("G:/axg/csv/車両マスタ.csv", 'r', 'utf8') as syaryo:
        with codecs.open("G:/axg/csv/"+k+"_車両マスタ.csv", 'w', 'utf8') as kisymaster:
            #print(next(syaryo))
            kisymaster.write(next(syaryo))
            for line in syaryo:
                m = re.match(ptn, line)
                if m:
                    #print(line)
                    kisymaster.write(line)

if __name__ == '__main__':
    #create()
    kisy('PC200','^PC200,(8|10),(N1|\s).*')
