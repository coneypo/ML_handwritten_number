# 2018-01-9
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# generate_folders_1to9.py
# 在目录下生成用来存放数字1-9的9个文件夹，分别用1-9命名

# 大写字母A-Z，小写字母a-z
# 注意windows下不区分字母大小写，Linux区分

import os

path_folders = "F:/code/python/P_ML_handwritten_number/data/data_pngs/Generated_database/"

# 1-9
for i in range(1, 10):
    if os.path.isdir(path_folders + str(i)):
        pass
    else:
        os.mkdir(path_folders+str(i))

"""
# A-Z
for i in range(65, 91):
    if os.path.isdir(path_folders + chr(i)):
        pass
    else:
        # print(i,": ",path_folders+chr(i))
        os.mkdir(path_folders+chr(i))

# a-z
for i in range(97, 123):
    if os.path.isdir(path_folders + chr(i)):
        pass
    else:
        # print(i,": ",path_folders+chr(i))
        os.mkdir(path_folders+chr(i))
"""