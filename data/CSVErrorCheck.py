import csv
import sys

path = "C:/Users/zz17390/vmshare/order/csv/"

def mycsv_reader(csv_reader):
    i=0
    while True:
        i += 1
        try:
            yield next(csv_reader)
        except csv.Error:
            # error handling what you want.
            print(str(i)+' : Error')
        pass
        continue
    return

if __name__ == '__main__':
    reader = mycsv_reader(csv.reader(open(path+'CA_TCJUT107.csv', 'rU')))
    sys.stdout =  open('error_check.csv', 'w')
    i = 0
    for line in reader:
        i += 1
        if 'Error' in line:
            print(str(i)+':')
            print(line)
    print(i)

    sys.stdout.close()