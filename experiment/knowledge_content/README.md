input_test.txt：输入的数据源
text_str.txt：模型的输入数据（未处理）
need_test.txt：模型的输入数据（已处理）
result_test.txt：输入数据的词向量表示

read_all.py：筛选所有由情感标签的数据存入input_test.txt
show_content.py：显示每一章节的情感分布
dedup.py：./units/unit1-7.txt词典的去重

结果：
单元 1
sum 2938
negative: 214
neural 2406
positive 318
negative/sum: 7.28%
neural/sum: 81.89%
positive/sum: 10.82%
单元 2
sum 1574
negative: 102
neural 1281
positive 191
negative/sum: 6.48%
neural/sum: 81.39%
positive/sum: 12.13%
单元 3
sum 2497
negative: 205
neural 2004
positive 288
negative/sum: 8.21%
neural/sum: 80.26%
positive/sum: 11.53%
单元 4
sum 694
negative: 92
neural 542
positive 60
negative/sum: 13.26%
neural/sum: 78.10%
positive/sum: 8.65%
单元 5
sum 2876
negative: 217
neural 2326
positive 333
negative/sum: 7.55%
neural/sum: 80.88%
positive/sum: 11.58%
单元 6
sum 2953
negative: 238
neural 2364
positive 351
negative/sum: 8.06%
neural/sum: 80.05%
positive/sum: 11.89%
单元 7
sum 698
negative: 41
neural 588
positive 69
negative/sum: 5.87%
neural/sum: 84.24%
positive/sum: 9.89%