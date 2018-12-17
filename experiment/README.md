class_before/：课前预习处理后的数据
class_after/：课后作业处理后的数据
week_every/：每周总结处理后的数据
experiment_exercise/：实验练习处理后的数据
knowledge_content/：知识点内容处理后的数据
difficult_degree/：知识点难度系数处理后的数据
data/：总体分类后的数据neg/neu/pos/del.csv
weeks/：所有数据按周次分类后的数据（01-13/del.txt）

read_xls.py：处理课前/课后/实验.xls中的数据，分别存储到before/after/week/experiment中的neg/neu/pos/del.csv中
read_xls_all.py：处理课前/课后/实验/每周.xls中的数据，分别存储到data/中的neg/neu/pos/del.csv中
read_week_all.py：处理课前/课后/实验/每周.xls中的数据，分别存储到weeks/中的01-13/del.txt中
show_week.py：数据的综合情感分析（时间维度）



