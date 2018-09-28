# created at 2018-01-29
# updated at 2018-09-28

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/ML_handwritten_number

# 在目录下生成用来存放数字 1-9 的 9 个文件夹，分别用 num_1-9 命名

# 大写字母A-Z，小写字母a-z
# 注意windows下不区分字母大小写，Linux区分

import os

path_folders = "../data/data_images/"


def generate_folders(path_folders):
    # 1-9
    for i in range(1, 10):
        if os.path.isdir(path_folders + "num_" +str(i)):
            pass
        else:
            print(path_folders+"num_"+str(i))
            os.mkdir(path_folders+"num_"+str(i))

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

generate_folders(path_folders)