# 2018-02-22
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# test_single_png_from_saved_models.py

# 利用保存到本地的训练好的模型，来检测单张png的标记
# 之前的需要每次测试时候都要重新训练一遍，这个将训练好的模型保存到本地直接调用

from sklearn.externals import joblib
# 用于数据预加工标准化
from sklearn.preprocessing import StandardScaler

# 用于数据预加工标准化
from sklearn.preprocessing import StandardScaler
from PIL import Image

path_test_png = "F:/code/python/P_ML_handwritten_number/"

img = Image.open(path_test_png+"6.png")

#img.show()

# get features
from Generate_handwriten_number import get_features
features_test_png = get_features.get_features_single(img)
#print(features_test_png)

path_saved_models = "F:/code/python/P_ML_handwritten_number/data/data_models/"

# LR
LR = joblib.load(path_saved_models + "model_LR.m")
predict_LR = LR.predict([features_test_png])
print("LR:", predict_LR)

# LSVC
LSVC = joblib.load(path_saved_models + "model_LSVC.m")
predict_LSVC = LSVC.predict([features_test_png])
print("LSVC:", predict_LSVC)

# MLPC
MLPC = joblib.load(path_saved_models + "model_MLPC.m")
predict_MLPC = MLPC.predict([features_test_png])
print("MLPC:", predict_MLPC)

# SGDC
SGDC = joblib.load(path_saved_models + "model_SGDC.m")
predict_SGDC = SGDC.predict([features_test_png])
print("SGDC:", predict_SGDC)