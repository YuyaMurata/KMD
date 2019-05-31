import os
import csv

path = "C:/Users/zz17390/vmshare/parts/cp932/"


def main():
    files = os.listdir(path)
    for fname in files:
        csvdata = csv.reader(open(path + fname, 'r'), quotechar="'", lineterminator='\n')
        print(fname)
        i = 0

        for row in csvdata:
            i += 1

            print(row[18])

            exit(0)

    print(str(i) + '件')


if __name__ == '__main__':
    main()
