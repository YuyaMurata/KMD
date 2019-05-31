import os
import gzip
import shutil
import zipfile

path = "G:/取得データ/KOMTRAX データ/KOMTRAXスクラップ車両データ/"

def gunzip(file, root):
    folder = file.split('_')[1].split('.')[0]
    if not os.path.isdir(root + '/' + folder):
        os.makedirs(root + '/' + folder)
    out = root + '/' + folder + '/' + file[:-7] + '.csv'

    with gzip.open(file, 'rb') as f_in:
        with open(out, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def unzip(file, out):
    with zipfile.ZipFile(file) as f_in:
        f_in.extractall(out)

def main():
    for root, dirs, files in os.walk(path):
        for file in files:
            if '.zip' not in file:
                continue

            print(file)

            if 'zip' in file:
                unzip(root + '/' + file, root)
            else:
                gunzip(root + '/' + file, root)


if __name__ == '__main__':
    main()