# 2018-01-29
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# plot_from_csv.py
# 从存放样本数-精度的CSV中读取数据，绘制图形


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# CSV路径
path_csv = "F:/code/python/P_ML_handwritten_number/data/score_csv/"

# 存储x轴坐标
x_array = []

# 存储精度
LR_score_arr = []
LSVC_score_arr = []
MLPC_score_arr = []
SGDC_score_arr = []

# 读取CSV数据
column_names = ["samples", "acc_LR", "acc_LSVC", "acc_MLPC", "acc_SGDC"]
rd_csv = pd.read_csv(path_csv + "score_100to5800.csv", names=column_names)

print(rd_csv.shape)

for i in range(len(rd_csv)):
    x_array.append(float(rd_csv["samples"][i]))
    LR_score_arr.append(float(rd_csv["acc_LR"][i]))
    LSVC_score_arr.append(float(rd_csv["acc_LSVC"][i]))
    MLPC_score_arr.append(float(rd_csv["acc_MLPC"][i]))
    SGDC_score_arr.append(float(rd_csv["acc_SGDC"][i]))

################ 5次线性拟合 ################
xray = np.array(x_array)
y_LR = np.array(LR_score_arr)
y_LSVC = np.array(LSVC_score_arr)
y_MLPC = np.array(MLPC_score_arr)
y_SGDC = np.array(SGDC_score_arr)

z1 = np.polyfit(xray, y_LR, 5)
z2 = np.polyfit(xray, y_LSVC, 5)
z3 = np.polyfit(xray, y_MLPC, 5)
z4 = np.polyfit(xray, y_SGDC, 5)

p1 = np.poly1d(z1)
p2 = np.poly1d(z2)
p3 = np.poly1d(z3)
p4 = np.poly1d(z4)

y_LR_vals = p1(xray)
y_LSVC_vals = p2(xray)
y_MLPC_vals = p3(xray)
y_SGDC_vals = p4(xray)
#################################

# 标明线条说明
plt.annotate("— LR", xy=(5030, 0.34), color='b', size=12)
plt.annotate("— LSVC", xy=(5030, 0.26), color='r', size=12)
plt.annotate("— MLPC", xy=(5030, 0.18), color='g', size=12)
plt.annotate("— SGDC", xy=(5030, 0.10), color='black', size=12)

# 画拟合曲线
plt.plot(xray, y_LR_vals, color='b')
plt.plot(xray, y_LSVC_vals, color='r')
plt.plot(xray, y_MLPC_vals, color='g')
plt.plot(xray, y_SGDC_vals, color='black')

# 画离散点
plt.plot(xray, y_LR, color='b', linestyle='None', marker='.', label='y_test', linewidth=100)
plt.plot(xray, y_LSVC, color='r', linestyle='None', marker='.', label='y_test', linewidth=0.01)
plt.plot(xray, y_MLPC, color='g', linestyle='None', marker='.', label='y_test', linewidth=0.01)
plt.plot(xray, y_SGDC, color='black', linestyle='None', marker='.', label='y_test', linewidth=0.01)

# 绘制y=1参考线
plt.plot([0, 6000], [1, 1], 'k--')

# 设置y轴坐标范围
plt.ylim(0, 1.1)

# 标明xy轴
plt.xlabel('samples')
plt.ylabel('accuracy')

plt.show()
