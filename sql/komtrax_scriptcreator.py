import codecs
import csv
import os
import re

from sql.scriptcreator import scriptname

#Layout Folder Path
#path="G:/取得データ/データ/GCPSデータ/layout/"
path = "E:/vmshare/komtrax/"
filename = path+"import_komtrax_script.txt"

dpath = "/mnt/hgfs/vmshare/komtrax/"

def createtable(fw, scriptname):
    layout = csv.reader(open(path + 'Layout_' + scriptname + '.csv', 'r'), lineterminator='\n')

    fw.write("CREATE TABLE " + scriptname + " (\n")
    header = next(layout)
    list = []
    for row in layout:
        list.append(" " + row[2] + " STRING")

    str = ',\n'.join(list)
    fw.write(str)
    fw.write("\n)\n")
    fw.write(" PARTITIONED BY (KIND STRING)\n")
    fw.write(" ROW FORMAT DELIMITED FIELDS TERMINATED BY ','\n")
    fw.write("     LINES TERMINATED BY '\\n'\n")
    fw.write(" STORED AS TEXTFILE;\n\n")

def loadfile(fw, fd, f, table):
    part = fd.replace("komtrax/", '')
    # Read
    fw.write("LOAD DATA LOCAL INPATH '" + dpath + fd + '/' + f + "' INTO TABLE komtrax_" + table)
    fw.write("  PARTITION (KIND = '" + fd + "');\n\n")

def main():
    fw = open(filename, 'w')

    scripts = []
    files = os.listdir(path)
    for f in files:
        if "Layout" in f:
            script = f.replace('Layout_', '').replace('.csv', '')
            print(script)
            fw.write("-- /* "+script+" */\n")
            scripts.append(str(script))
            createtable(fw, script)

    root = os.listdir(path)
    for folder in root:
        if 'Layout' in folder or 'import' in folder:
            continue

        #print(folder)
        fw.write("-- /* "+folder+" */\n")

        files = os.listdir(path+"/"+folder+"/")
        for file in files:
            print(file)
            fd = file.split('.')[0]
            loadfile(fw, folder, file, fd)

    fw.close()


if __name__ == '__main__':
    main()