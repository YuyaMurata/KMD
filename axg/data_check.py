import pandas as pd
import csv
import linecache
import datetime

path = 'G:/取得データ_20200304/out/clensing/EQP経歴情報.csv'

def headerCheck(path):
    #head = linecache.getline(path, 1)
    #col_names = ['c{0:02d}'.format(i) for i in range(head.count(",")+1)]
    #print(col_names)

    data = pd.read_csv(path, sep=',', encoding='UTF8', header=None, engine='python', chunksize=1000000)
    for idx, row in data.get_chunk(1).iterrows():
        print(row)
        break

    a = input('select index > ')

    return a, data

def preprocess(idx, d):
    column = d.iloc[:,int(idx)].astype('str')
    return column

def dateCheck(idx, data):
    column = pd.concat((preprocess(idx, d) for d in data), ignore_index=True)
    print(idx+':'+str(len(column)))
    print(column.head(2))

    if '/' in str(column[1]):
        f = '%Y/%m/%d'
    elif '-' in str(column[1]):
        f = '%Y-%m-%d'
    else:
        f = '%Y%m%d'
    date = pd.to_datetime(column, format=f, errors='coerce').dropna()

    print(str(date.min())+' - '+str(date.max()))

if __name__ == '__main__':
    idx, data = headerCheck(path)
    dateCheck(idx, data)
