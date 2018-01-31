# 2018-01-29
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# del_pngs.py
# 删除路径下生成的图像文件

import os

path_pic = "F:/code/python/P_ML_handwritten_number/data/data_pngs/Generated_database/"

#删除路径下的图片
def del_pngs():
    for i in range(1, 10):
        namedir = os.listdir(path_pic+str(i))
        for tmppng in namedir:
            if( tmppng in namedir):
                os.remove(path_pic+str(i)+"/"+tmppng)
del_pngs()