# 2018-01-29
# By TimeStamp
# cnblogs: http://www.cnblogs.com/AdaminXie/
# test_single_png.py
# 利用模型检测单张png的标记

from PIL import Image

path_testpng = "F:/code/python/P_ML_handwritten_number/"

path_2 = "F:/code/python/P_web_spider/ecnu_vericodes/single_nums/"


img = Image.open(path_testpng+"new_6.png")

#img.show()

# get features
from Generate_handwriten_number import get_features
features_test_png = get_features.get_features_single(img)
print(features_test_png)

# ML ways
import ML_models
ML_models.pre_data(5800)

ss_LR, LR = ML_models.way_LR()
ss_LSVC, LSVC = ML_models.way_LSVC()
ss_MLPC, MLPC = ML_models.way_MLPC()
ss_SGDC, SGDC = ML_models.way_SGDC()

X_test_single_LR = ss_LR.transform([features_test_png])
print("LR", '\t', LR.predict(X_test_single_LR))

X_test_single_LSVC = ss_LSVC.transform([features_test_png])
print("LSVC", '\t', LSVC.predict(X_test_single_LSVC))

X_test_single_MLPC = ss_MLPC.transform([features_test_png])
print("MLPC", '\t', MLPC.predict(X_test_single_LSVC))

X_test_single_SGDC = ss_SGDC.transform([features_test_png])
print("SGDC", '\t', SGDC.predict(X_test_single_SGDC))