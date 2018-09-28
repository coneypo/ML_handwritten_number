# created at 2018-01-29
# updated at 2018-09-28

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/ML_handwritten_number

# 利用保存到本地的训练好的模型，来检测单张 image 的标记

from sklearn.externals import joblib
from PIL import Image

img = Image.open("../test/test_1.png")

# Get features
from generate_datebase import get_features
features_test_png = get_features.get_features_single(img)

path_saved_models = "../data/data_models/"

# LR
LR = joblib.load(path_saved_models + "model_LR.m")
predict_LR = LR.predict([features_test_png])
print("LR:", predict_LR[0])

# LSVC
LSVC = joblib.load(path_saved_models + "model_LSVC.m")
predict_LSVC = LSVC.predict([features_test_png])
print("LSVC:", predict_LSVC[0])

# MLPC
MLPC = joblib.load(path_saved_models + "model_MLPC.m")
predict_MLPC = MLPC.predict([features_test_png])
print("MLPC:", predict_MLPC[0])

# SGDC
SGDC = joblib.load(path_saved_models + "model_SGDC.m")
predict_SGDC = SGDC.predict([features_test_png])
print("SGDC:", predict_SGDC[0])

