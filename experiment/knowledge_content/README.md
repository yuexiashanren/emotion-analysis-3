input_test.txt：输入的数据源
text_str.txt：模型的输入数据（未处理）
need_test.txt：模型的输入数据（已处理）
result_test.txt：输入数据的词向量表示

read_all.py：筛选所有由情感标签的数据存入input_test.txt
show_content.py：显示每一章节的情感分布
dedup.py：./units/unit1-7.txt词典的去重

结果：
单元 1
sum 2913
negative: 212
neural 2389
positive 312
negative/sum: 7.28%
neural/sum: 82.01%
positive/sum: 10.71%
单元 2
sum 1574
negative: 102
neural 1281
positive 191
negative/sum: 6.48%
neural/sum: 81.39%
positive/sum: 12.13%
单元 3
sum 2498
negative: 205
neural 2008
positive 285
negative/sum: 8.21%
neural/sum: 80.38%
positive/sum: 11.41%
单元 4
sum 695
negative: 92
neural 545
positive 58
negative/sum: 13.24%
neural/sum: 78.42%
positive/sum: 8.35%
单元 5
sum 2877
negative: 217
neural 2330
positive 330
negative/sum: 7.54%
neural/sum: 80.99%
positive/sum: 11.47%
单元 6
sum 2420
negative: 178
neural 1956
positive 286
negative/sum: 7.36%
neural/sum: 80.83%
positive/sum: 11.82%
单元 7
sum 482
negative: 23
neural 408
positive 51
negative/sum: 4.77%
neural/sum: 84.65%
positive/sum: 10.58%