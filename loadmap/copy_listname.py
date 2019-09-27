import os
import shutil

mode = 'Emode90'
path = "C:/Users/zz17807/OneDrive - Komatsu Ltd/共同研究/負荷情報検証/ポンプ圧/"+mode+"%/"
sidlist = path+'PC200_loadmap_'+mode+'.csv'

spath = "C:/Users/zz17807/OneDrive - Komatsu Ltd/車両負荷マップ/PC200-10/PC200-10負荷情報_可視化/"
mpath = "C:/Users/zz17807/OneDrive - Komatsu Ltd/共同研究/190819/負荷情報/"

with open(sidlist, 'r') as f:
    for line in f:
        sid = line.replace('\n', '')
        fd = spath+sid+'/loadmap/'
        root = os.listdir(fd)
        for load in root:
            if 'エンジン水温' in load :
                if 'VS作動油温.csv.png' not in load:
                    shutil.copyfile(fd+load, path+sid+'_'+load)

        #root = os.listdir(mpath)
        #for master in root:
        #    if sid in master:
        #        shutil.copyfile(mpath + master, path + master)