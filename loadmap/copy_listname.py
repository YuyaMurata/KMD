import os
import shutil

mode = 'Lmode10'
path = "C:/Users/zz17807/OneDrive - Komatsu Ltd/共同研究/負荷情報検証/温度/水温/"+mode+"%/"
sidlist = path+'PC200_loadmap_'+mode+'.csv'

spath = "C:/Users/zz17807/OneDrive - Komatsu Ltd/車両負荷マップ/file/"
mpath = "C:/Users/zz17807/OneDrive - Komatsu Ltd/共同研究/190819/負荷情報/"

with open(sidlist, 'r') as f:
    for line in f:
        sid = line.replace('\n', '').replace('-10-', '-10- -')
        fd = spath
        root = os.listdir(fd)
        for load in root:
            if sid in load:
                if '_エンジン水温.csv' in load :
                    shutil.copyfile(fd+load, path+load)

        #root = os.listdir(mpath)
        #for master in root:
        #    if sid in master:
        #        shutil.copyfile(mpath + master, path + master)