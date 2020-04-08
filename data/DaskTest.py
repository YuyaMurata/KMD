import dask.dataframe as dd
import codecs
import csv

path = "G:/取得データ_20200304/out/master/TG20M001.csv"

data = dd.read_csv(path, engine='python', sep=',', quotechar="'", header=None, encoding='UTF8').compute()

for d in data.values.tolist():
    print(d)