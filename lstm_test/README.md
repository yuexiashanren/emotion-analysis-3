reacll.py：预测结果写入y-pre.txt中
recall_re.py：计算召回率
finish_value.py：计算某周的最终情感值
lstm_train.py：训练
数据集： 6498 ，数据集标签： 6498
训练集： (5198, 100) ，训练集标签： (5198, 3)
测试集： (1300, 100) ，测试集标签： (1300, 3)
del-179
neg-1374
neu-3972
pos-1422
训练：
1、- loss: 0.8511 - acc: 0.6174
2、- loss: 0.7596 - acc: 0.6585
3、- loss: 0.6940 - acc: 0.7035
4、- loss: 0.6447 - acc: 0.7268
5、- loss: 0.6032 - acc: 0.7536
6、- loss: 0.5534 - acc: 0.7668
7、- loss: 0.5028 - acc: 0.7945
8、- loss: 0.4463 - acc: 0.8219
9、loss: 0.4091 - acc: 0.8386
10、- loss: 0.3460 - acc: 0.8655
测试：
Test score: 0.8162244809590853
Test accuracy: 0.7038461540295528

lstm_test.py：测试
negative: 4
neural 19
positive 7
negative/sum: 13.33%
neural/sum: 63.33%
positive/sum: 23.33%
