lstm_train.py：训练
数据集： 6498 ，数据集标签： 6498
训练集： (5198, 100) ，训练集标签： (5198, 3)
测试集： (1300, 100) ，测试集标签： (1300, 3)
del-179
neg-1374
neu-3972
pos-1422
训练：
1、- loss: 0.8427 - acc: 0.6208
2、- loss: 0.7488 - acc: 0.6705
3、- loss: 0.6858 - acc: 0.7093
4、- loss: 0.6365 - acc: 0.7311
5、- loss: 0.5882 - acc: 0.7555
6、- loss: 0.5450 - acc: 0.7790
7、- loss: 0.4779 - acc: 0.8082
测试：
Test score: 0.7429023111783541
Test accuracy: 0.7046153847987835

lstm_test.py：测试
negative: 2
neural 20
positive 8
negative/sum: 6.67%
neural/sum: 66.67%
positive/sum: 26.67%

reacll.py：计算模型召回率