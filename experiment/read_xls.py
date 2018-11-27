'''
读取课前预习/课后作业/每周总结/实验练习.xls中的数据，
分别存储到class_before/class_after/week_every/experiment_exercise/下的neg/neu/pos/del.csv中
'''
# -*- coding: utf-8 -*-
import xlrd

xlsfile1 = r"课前预习.xls"# 打开课前预习
xlsfile2 = r"课后作业.xls"# 打开课后作业
xlsfile3 = r"每周总结.xls"# 打开每周总结
xlsfile4 = r"实验练习.xls"# 打开实验练习

book1 = xlrd.open_workbook(xlsfile1)#得到Excel文件的book对象，实例化对象
book2 = xlrd.open_workbook(xlsfile2)
book3 = xlrd.open_workbook(xlsfile3)
book4 = xlrd.open_workbook(xlsfile4)

sheet1 = book1.sheet_by_index(0) # 通过sheet索引获得课前预习sheet对象
sheet2 = book2.sheet_by_index(0)
sheet3 = book3.sheet_by_index(0)
sheet4 = book4.sheet_by_index(0)
#sheet1 = book.sheet_by_name(sheet_name)# 通过sheet名字来获取sheet对象，输出等效于sheet0
'''
print ("sheet[1]类别",type(sheet0))
sheet_name = book.sheet_names()[0]# 获得指定索引的sheet表名字
print ("sheet[1]名字",sheet_name)
'''

nrows1 = sheet1.nrows    # 获取行总数
ncols1 = sheet1.ncols    #获取列总数
print ("课前预习行/列数",nrows1,ncols1)

nrows2 = sheet2.nrows    # 获取行总数
ncols2 = sheet2.ncols    #获取列总数
print ("课后作业行/列数",nrows2,ncols2)

nrows3 = sheet3.nrows    # 获取行总数
ncols3 = sheet3.ncols    #获取列总数
print ("每周总结行/列数",nrows3,ncols3)

nrows4 = sheet4.nrows    # 获取行总数
ncols4 = sheet4.ncols    #获取列总数
print ("实验练习行/列数",nrows4,ncols4)

sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0

#课前预习数据
pos_sum_1 = 0
neu_sum_1 = 0
neg_sum_1 = 0
del_sum_1 = 0
f_neg_1 = open('./class_before/neg.csv', 'w', encoding='utf-8')
f_neu_1 = open('./class_before/neu.csv', 'w', encoding='utf-8')
f_pos_1 = open('./class_before/pos.csv', 'w', encoding='utf-8')
f_del_1 = open('./class_before/del.csv', 'w', encoding='utf-8')

#课后作业数据
pos_sum_2 = 0
neu_sum_2 = 0
neg_sum_2 = 0
del_sum_2 = 0
f_neg_2 = open('./class_after/neg.csv', 'w', encoding='utf-8')
f_neu_2 = open('./class_after/neu.csv', 'w', encoding='utf-8')
f_pos_2 = open('./class_after/pos.csv', 'w', encoding='utf-8')
f_del_2 = open('./class_after/del.csv', 'w', encoding='utf-8')

#每周总结数据
pos_sum_3 = 0
neu_sum_3 = 0
neg_sum_3 = 0
del_sum_3 = 0
f_neg_3 = open('./week_every/neg.csv', 'w', encoding='utf-8')
f_neu_3 = open('./week_every/neu.csv', 'w', encoding='utf-8')
f_pos_3 = open('./week_every/pos.csv', 'w', encoding='utf-8')
f_del_3 = open('./week_every/del.csv', 'w', encoding='utf-8')

#实验练习数据
pos_sum_4 = 0
neu_sum_4 = 0
neg_sum_4 = 0
del_sum_4 = 0
f_neg_4 = open('./experiment_exercise/neg.csv', 'w', encoding='utf-8')
f_neu_4 = open('./experiment_exercise/neu.csv', 'w', encoding='utf-8')
f_pos_4 = open('./experiment_exercise/pos.csv', 'w', encoding='utf-8')
f_del_4 = open('./experiment_exercise/del.csv', 'w', encoding='utf-8')

#课前预习数据筛选
for i in range(nrows1):
    #获取情感倾向列的标签值(行列序号从0开始)
	choose1 = sheet1.cell_value(i,7)
	text_str = sheet1.cell_value(i,6)
	if(choose1 == 1):
		sum_1 += 1
		pos_sum_1 += 1
		f_pos_1.write(str(text_str))
		f_pos_1.write('\n')
	elif(choose1 == 0):
		sum_1 += 1
		neu_sum_1 += 1
		f_neu_1.write(str(text_str))
		f_neu_1.write('\n')
	elif(choose1 == -1):
		sum_1 += 1
		neg_sum_1 += 1
		f_neg_1.write(str(text_str))
		f_neg_1.write('\n')
	else:
		#None
		sum_1 += 1
		del_sum_1 += 1
		f_del_1.write(str(text_str))
		f_del_1.write('\n')
	
#课后作业数据筛选
for i in range(nrows2):
    #获取情感倾向列的标签值(行列序号从0开始)
	choose2 = sheet2.cell_value(i,7)
	text_str = sheet2.cell_value(i,6)
	if(choose2 == 1):
		sum_2 += 1
		pos_sum_2 += 1
		f_pos_2.write(str(text_str))
		f_pos_2.write('\n')
	elif(choose2 == 0):
		sum_2 += 1
		neu_sum_2 += 1
		f_neu_2.write(str(text_str))
		f_neu_2.write('\n')
	elif(choose2 == -1):
		sum_2 += 1
		neg_sum_2 += 1
		f_neg_2.write(str(text_str))
		f_neg_2.write('\n')
	else:
		#None
		sum_2 += 1
		del_sum_2 += 1
		f_del_2.write(str(text_str))
		f_del_2.write('\n')
		
#每周总结筛选
for i in range(nrows3):
    #获取情感倾向列的标签值(行列序号从0开始)
	choose3 = sheet3.cell_value(i,6)
	text_str = sheet3.cell_value(i,5)
	if(choose3 == 1):
		sum_3 += 1
		pos_sum_3 += 1
		f_pos_3.write(str(text_str))
		f_pos_3.write('\n')
	elif(choose3 == 0):
		sum_3 += 1
		neu_sum_3 += 1
		f_neu_3.write(str(text_str))
		f_neu_3.write('\n')
	elif(choose3 == -1):
		sum_3 += 1
		neg_sum_3 += 1
		f_neg_3.write(str(text_str))
		f_neg_3.write('\n')
	else:
		#None	
		sum_3 += 1
		del_sum_3 += 1
		f_del_3.write(str(text_str))
		f_del_3.write('\n')

#实验练习数据筛选
for i in range(nrows4):
    #获取情感倾向列的标签值(行列序号从0开始)
	choose4 = sheet4.cell_value(i,7)
	text_str = sheet4.cell_value(i,6)
	if(choose4 == 1):
		sum_4 += 1
		pos_sum_4 += 1
		f_pos_4.write(str(text_str))
		f_pos_4.write('\n')
	elif(choose4 == 0):
		sum_4 += 1
		neu_sum_4 += 1
		f_neu_4.write(str(text_str))
		f_neu_4.write('\n')
	elif(choose4 == -1):
		sum_4 += 1
		neg_sum_4 += 1
		f_neg_4.write(str(text_str))
		f_neg_4.write('\n')
	else:
		#None
		sum_4 += 1
		del_sum_4 += 1
		f_del_4.write(str(text_str))
		f_del_4.write('\n')

#课前预习结果
f_pos_1.close()
f_neu_1.close()
f_neg_1.close()
f_del_1.close()
print("课前预习累计语料",sum_1)#2051##403/1283/353/12
print("累计pos/neu/neg/del语料",pos_sum_1,neu_sum_1,neg_sum_1,del_sum_1)

#课后作业结果
f_pos_2.close()
f_neu_2.close()
f_neg_2.close()
f_del_2.close()
print("课后作业累计语料",sum_2)#1952##405/1137/366/17
print("累计pos/neu/neg/del语料",pos_sum_2,neu_sum_2,neg_sum_2,del_sum_2)

#每周总结结果
f_pos_3.close()
f_neu_3.close()
f_neg_3.close()
f_del_3.close()
print("每周总结累计语料",sum_3)#1930##455/1104/365/6
print("累计pos/neu/neg/del语料",pos_sum_3,neu_sum_3,neg_sum_3,del_sum_3)

#实验练习结果
f_pos_4.close()
f_neu_4.close()
f_neg_4.close()
f_del_4.close()
print("实验练习累计语料",sum_4)#1041##159/448/290/144
print("累计pos/neu/neg/del语料",pos_sum_4,neu_sum_4,neg_sum_4,del_sum_4)

#综合结果
print("综合累计语料",sum_1+sum_2+sum_3+sum_4)#6947
print("累计pos/neu/neg/del语料",pos_sum_1+pos_sum_2+pos_sum_3+pos_sum_4,
								neu_sum_1+neu_sum_2+neu_sum_3+neu_sum_4,
								neg_sum_1+neg_sum_2+neg_sum_3+neg_sum_4,
								del_sum_1+del_sum_2+del_sum_3+del_sum_4)
								#1422/3972/1374/179