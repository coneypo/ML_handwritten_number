# Simple example of handwritten numbers in Machine Learning

Steps:
>	1. Generate handwritten numbers  
>> ```generate_folders.py``` &nbsp;  &nbsp;  &nbsp; &nbsp;   &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp; 为数字 1-9 建立文件夹            &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;               
>> ```generate_handwritten_numbers.py```  &nbsp; &nbsp;  &nbsp;  生成手写体数字

>	2. Get features from number 1 to 9 
>> ```get_features.py```   &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp; &nbsp; 提取生成的手写体数字的特征并且存入 CSV 中 

>	3. Train and test Machine Learning models
>> ```ml_and.py```   &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  利用提取出来的特征，训练不同的机器学习模型
>> ```test_single_image.py```   &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;   &nbsp;    &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp;  &nbsp; 利用训练好的模型，测试手写体数字

<br>

Author: coneypo

Thanks for your support.
