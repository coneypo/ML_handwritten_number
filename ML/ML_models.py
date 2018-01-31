# 2018-01-29
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# ML_models.py
# 利用数据集进行建模并测试性能

from sklearn.model_selection import train_test_split
import pandas as pd

from sklearn.preprocessing import StandardScaler  # 标准化

from sklearn.linear_model import LogisticRegression  # 线性模型中的Logistic回归模型
from sklearn.svm import LinearSVC  # SVM模型中的线性SVC模型
from sklearn.neural_network import MLPClassifier  # 神经网络模型中的多层网络模型
from sklearn.linear_model import SGDClassifier  # 线性模型中的随机梯度下降模型


# 从CSV中读取数据
def pre_data(sample_num):
    # CSV61维表头名
    column_names = []

    for i in range(0, 60):
        column_names.append("feature_" + str(i))
    column_names.append("true_number")

    # 读取csv
    path_csv = "F:/code/python/P_ML_handwritten_number/data/data_csv/"
    print(path_csv + "test_" + str(sample_num) + ".csv")
    data = pd.read_csv(path_csv + "data_" + str(sample_num) + ".csv", names=column_names)

    # 提取数据集
    global X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = train_test_split(
        data[column_names[0:60]],
        data[column_names[60]],
        test_size=0.25,  # 75%训练，25%测试
        random_state=33
    )


# LR, logistic regression, 逻辑斯特回归分类（线性模型）
def way_LR():
    X_train_LR = X_train
    y_train_LR = y_train

    X_test_LR = X_test
    y_test_LR = y_test

    # 数据预加工
    ss_LR = StandardScaler()
    X_train_LR = ss_LR.fit_transform(X_train_LR)
    X_test_LR = ss_LR.transform(X_test_LR)

    # 初始化LogisticRegression
    LR = LogisticRegression()

    # 调用LogisticRegression中的fit()来训练模型参数
    LR.fit(X_train_LR, y_train_LR)

    # 使用训练好的模型lr对X_test进行预测
    # 结果储存在y_predict_LR中
    global y_predict_LR
    y_predict_LR = LR.predict(X_test_LR)

    # 评分函数
    global score_LR
    score_LR = LR.score(X_test_LR, y_test_LR)
    print("The accurary of LR:", '\t', score_LR)

    return ss_LR, LR


# 多层感知机分类（神经网络）
def way_MLPC():
    X_train_MLPC = X_train
    y_train_MLPC = y_train

    X_test_MLPC = X_test
    y_test_MLPC = y_test

    ss_MLPC = StandardScaler()
    X_train_MLPC = ss_MLPC.fit_transform(X_train_MLPC)
    X_test_MLPC = ss_MLPC.transform(X_test_MLPC)

    MLPC = MLPClassifier(hidden_layer_sizes=(13, 13, 13), max_iter=500)
    MLPC.fit(X_train_MLPC, y_train_MLPC)

    global y_predict_MLPC
    y_predict_MLPC = MLPC.predict(X_test_MLPC)

    global score_MLPC
    score_MLPC = MLPC.score(X_test_MLPC, y_test_MLPC)
    print("The accurary of MLPC:", '\t', score_MLPC)

    return ss_MLPC, MLPC


# Linear SVC， Linear Supported Vector Classifier, 线性支持向量分类(SVM支持向量机)
def way_LSVC():
    X_train_LSVC = X_train
    y_train_LSVC = y_train

    X_test_LSVC = X_test
    y_test_LSVC = y_test

    ss_LSVC = StandardScaler()
    X_train_LSVC = ss_LSVC.fit_transform(X_train_LSVC)
    X_test_LSVC = ss_LSVC.transform(X_test_LSVC)

    LSVC = LinearSVC()
    LSVC.fit(X_train_LSVC, y_train_LSVC)

    global y_predict_LSVC
    y_predict_LSVC = LSVC.predict(X_test_LSVC)

    global score_LSVC
    score_LSVC = LSVC.score(X_test_LSVC, y_test_LSVC)
    print("The accurary of LSVC:", '\t', score_LSVC)

    return ss_LSVC, LSVC


# SGDC, stochastic gradient decent 随机梯度下降法求解(线性模型)
def way_SGDC():
    X_train_SGDC = X_train
    y_train_SGDC = y_train

    X_test_SGDC = X_test
    y_test_SGDC = y_test

    ss_SGDC = StandardScaler()
    X_train_SGDC = ss_SGDC.fit_transform(X_train_SGDC)
    X_test_SGDC = ss_SGDC.transform(X_test_SGDC)

    SGDC = SGDClassifier(max_iter=5)

    SGDC.fit(X_train_SGDC, y_train_SGDC)

    global y_predict_SGDC
    y_predict_SGDC = SGDC.predict(X_test_SGDC)

    global score_SGDC
    score_SGDC = SGDC.score(X_test_SGDC, y_test_SGDC)
    print("The accurary of SGDC:", '\t', score_SGDC)

    return ss_SGDC, SGDC

# 计算不同数据集大小下的模型精度
def compute_scores():

    score_list_LR = []
    score_list_MLPC = []
    score_list_LSVC = []
    score_list_SGDC = []

    for sample_nums in range(100, 5900, 100):
        pre_data(sample_nums)

        way_LR()
        way_LSVC()
        way_MLPC()
        way_SGDC()
        print('\n')

        score_list_LR.append(score_LR)
        score_list_MLPC.append(score_MLPC)
        score_list_LSVC.append(score_LSVC)
        score_list_SGDC.append(score_SGDC)

    print(score_list_LR)
    print(score_list_MLPC)
    print(score_list_LSVC)
    print(score_list_SGDC)

    return score_list_LR, score_list_MLPC, score_list_LSVC, score_list_SGDC

import csv
path_score_csv = "F:/code/python/P_ML_handwritten_number/data/score_csv/"

# 将数据集大小从100至5900对应的测试精度写入CSV中
def scores_to_csv():
    score_list_LR, score_list_MLPC, score_list_LSVC, score_list_SGDC = compute_scores()

    sample_nums= 100

    with open(path_score_csv + "score.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(score_list_LR)):
            data_to_csv = []
            data_to_csv.append(sample_nums)
            data_to_csv.append(score_list_LR[i])
            data_to_csv.append(score_list_MLPC[i])
            data_to_csv.append(score_list_LSVC[i])
            data_to_csv.append(score_list_SGDC[i])
            writer.writerow(data_to_csv)

            sample_nums+=100

#scores_to_csv()