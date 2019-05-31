import codecs
import csv
import os

path = "E:/vmshare/"
scriptname = "as契約"
fd = 'allsupport'
filepath = path+fd+'/'
filename = filepath+"import_"+scriptname+"_script.txt"

def createtable(fw):
    layout = csv.reader(open(filepath + 'Layout_' + scriptname + '.csv', 'r'), lineterminator='\n')

    fw.write("CREATE TABLE " + scriptname + " (\n")
    header = next(layout)
    list = []
    for row in layout:
        list.append(" " + row[2] + " STRING")

    str = ',\n'.join(list)
    fw.write(str)
    fw.write("\n)\n")
    fw.write(" PARTITIONED BY (company STRING)\n")
    fw.write(" ROW FORMAT DELIMITED FIELDS TERMINATED BY ','\n")
    fw.write("     LINES TERMINATED BY '\\n'\n")
    fw.write(" STORED AS TEXTFILE;\n\n")


def loadfile(fw, f):
    part = f.split('_')[0]
    # Read
    fw.write("LOAD DATA LOCAL INPATH '/root/data/" + fd + '/utf8/' + f + "' INTO TABLE " + scriptname)
    fw.write("  PARTITION (company = '"+part+"');\n\n")

def main():
    fw = open(filename, 'w')

    createtable(fw)

    files = os.listdir(filepath+'utf8/')
    for f in files:
        loadfile(fw, f)

    fw.close()


if __name__ == '__main__':
    main()