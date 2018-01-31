# 2018-01-29
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie
# get_features.py
# 提取特征写入CSV


# 提取图像的特征
from PIL import Image
import pandas as pd
import csv
import os

# 提取单张图像的特征
def get_features_single(img):
    # 提取特征
    # 30*30的图像
    global pixel_cnt_list
    pixel_cnt_list = []

    height, width = 30, 30
    # 统计30行每行的黑点数
    for y in range(height):
        pixel_cnt_x = 0
        for x in range(width):
            if img.getpixel((x, y)) == 0:  # 黑点
                pixel_cnt_x += 1
        pixel_cnt_list.append(pixel_cnt_x)
    # 统计30列每列的黑点数
    for x in range(width):
        pixel_cnt_y = 0
        for y in range(height):
            if img.getpixel((x, y)) == 0:  # 黑点
                pixel_cnt_y += 1
        pixel_cnt_list.append(pixel_cnt_y)
    return pixel_cnt_list

# 遍历文件夹提取特征存入CSV
# 取sample_nums个
def get_features_to_CSV(sample_nums):

    path_pngs = "F:/code/python/P_ML_handwritten_number/data/data_pngs/Generated_database/"
    path_csv = "F:/code/python/P_ML_handwritten_number/data/data_csv/"

    pngs_sum = 0

    # 读取图像文件
    with open(path_csv+"test1.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # 访问文件夹 1-9
        for i in range(1, 10):
            namedir = os.listdir(path_pngs+str(i))
            # 读到图像文件
            if os.path.isdir(path_pngs + str(i)):
                print(path_pngs+str(i), " ", "样本个数：", len(namedir))
                pngs_sum = pngs_sum + len(namedir)

                for j in range(0, (len(namedir))):

                    # 处理读取单个图像文件提取特征
                    img = Image.open(path_pngs+str(i)+"/"+namedir[j])
                    get_features_single(img)
                    pixel_cnt_list.append(namedir[j][0])

                    # 写入CSV
                    writer.writerow(pixel_cnt_list)
        print('\n', "样本总数pngs_sum:", pngs_sum)

    data = pd.read_csv(path_csv+"test1.csv")

    tmpdir = os.listdir(path_csv)

    # 以"test_+样本数.csv"重新命名CSV
    if "data_"+str(sample_nums)+".csv" in tmpdir:
        # 之前生成过data_XXX.csv，需要先删除掉
        os.remove(path_csv+"data_"+str(sample_nums)+".csv")
        os.rename(path_csv+"test1.csv", path_csv+"data_"+str(sample_nums)+".csv")
    else:
        os.rename(path_csv+"test1.csv", path_csv+"data_"+str(sample_nums)+".csv")

#from generate_handwritten_numbers import generate_nums
#from del_pngs import del_pngs

"""
for sample_nums in range(2700, 6000, 100):
    del_pngs()
    generate_nums(sample_nums)
    get_features_to_CSV(sample_nums)
"""