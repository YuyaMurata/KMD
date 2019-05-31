import csv

path = "Layout_komatsucare"
def main():
    fr = csv.reader(open(path+"_all.csv", 'r'), quotechar='"')
    head = next(fr)

    tmp = "-1"
    i = 0
    layout = None
    for komcsv in fr:
        if tmp != komcsv[0]:
            i = 1
            if layout != None:
                layout.close()
            layout = open(path+"_"+komcsv[0]+".csv", 'w')
            layout.write("no, name ,code, type, size\n")

        if "\n" in komcsv[1]:
            komcsv[1] = komcsv[1].replace('\n', ' ')
        layout.write(str(i)+","+komcsv[1]+","+komcsv[2]+","+komcsv[3]+","+komcsv[4]+"\n")

        i += 1
        tmp = komcsv[0]

if __name__ == '__main__':
    main()