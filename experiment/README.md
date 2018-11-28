class_before：课前预习分类后的数据
class_after：课后作业分类后的数据
week_every：每周总结分类后的数据
experiment_exercise：实验练习分类后的数据
data/：总体分类后的数据neg/neu/pos/del.csv
weeks/：所有数据按周次分类后的数据（01-13/del.txt）

read_xls.py：处理xx.xls中的数据，分别进行分类存储到before/after/week/experiment
read_xls_all.py：处理xx.xls中的数据，总体进行分类存储到data/
read_week_all.py：处理xx.xls中的数据，总体进行分类存储到weeks/
show_week.py：数据的综合情感分析（时间维度）



