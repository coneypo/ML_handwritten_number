Simple example of handwritten numbers in Machine Learning
#########################################################

Introduction
************
介绍了如何生成手写体数字的数据, 提取特征;
借助 sklearn 机器学习模型建模, 进行识别手写体数字 1-9 模型的建立和测试.


About Source Code
*****************

#. Generate handwritten numbers

   #. generate_folders.py

      为数字 1-9 建立文件夹

   #. generate_handwritten_numbers.py

      生成手写体数字

#. Get features from number 1 to 9

   #. get_features.py

      提取生成的手写体数字的特征并且存入 CSV 中

#. Train and test Machine Learning models

   #. ml_ana.py

      利用提取出来的特征，训练不同的机器学习模型

   #. test_single_image.py

      利用训练好的模型，测试手写体数字


More
****

Author: coneypo

Mail: coneypo@foxmail.com

Thanks for your support.
