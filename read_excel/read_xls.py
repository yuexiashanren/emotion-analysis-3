'''
读取表格中属于各种情感值的数据，存储到./neg/neu/pos/del.csv中
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
print ("课前预习总行数",nrows1)
ncols1 = sheet1.ncols    #获取列总数
print ("课前预习总列数",ncols1)
nrows2 = sheet2.nrows    # 获取行总数
print ("课后作业总行数",nrows2)
ncols2 = sheet2.ncols    #获取列总数
print ("课后作业总列数",ncols2)
nrows3 = sheet3.nrows    # 获取行总数
print ("每周总结总行数",nrows3)
ncols3 = sheet3.ncols    #获取列总数
print ("每周总结总列数",ncols3)
nrows4 = sheet4.nrows    # 获取行总数
print ("实验练习总行数",nrows4)
ncols4 = sheet4.ncols    #获取列总数
print ("实验练习总列数",ncols4)

sum = 0
pos_sum = 0
neu_sum = 0
neg_sum = 0
del_sum = 0
f_neg = open('neg.csv', 'w', encoding='utf-8')
f_neu = open('neu.csv', 'w', encoding='utf-8')
f_pos = open('pos.csv', 'w', encoding='utf-8')
f_del = open('del.csv', 'w', encoding='utf-8')

#课前预习筛选
for i in range(nrows1):
    #获取情感倾向列的标签值(行列序号从0开始)
	choose1 = sheet1.cell_value(i,7)
	text_str = sheet1.cell_value(i,6)
	if(choose1 == 1):
		sum += 1
		pos_sum += 1
		f_pos.write(str(text_str))
		f_pos.write('\n')
	elif(choose1 == 0):
		sum += 1
		neu_sum += 1
		f_neu.write(str(text_str))
		f_neu.write('\n')
	elif(choose1 == -1):
		sum += 1
		neg_sum += 1
		f_neg.write(str(text_str))
		f_neg.write('\n')
	else:
		#None
		
		sum += 1
		del_sum += 1
		f_del.write(str(text_str))
		f_del.write('\n')
		
#课后作业筛选
for i in range(nrows2):
    #获取情感倾向列的标签值(行列序号从0开始)
	choose2 = sheet2.cell_value(i,7)
	text_str = sheet2.cell_value(i,6)
	if(choose2 == 1):
		sum += 1
		pos_sum += 1
		f_pos.write(str(text_str))
		f_pos.write('\n')
	elif(choose2 == 0):
		sum += 1
		neu_sum += 1
		f_neu.write(str(text_str))
		f_neu.write('\n')
	elif(choose2 == -1):
		sum += 1
		neg_sum += 1
		f_neg.write(str(text_str))
		f_neg.write('\n')
	else:
		#None
		
		sum += 1
		del_sum += 1
		f_del.write(str(text_str))
		f_del.write('\n')
		
#每周总结筛选
for i in range(nrows3):
    #获取情感倾向列的标签值(行列序号从0开始)
	choose3 = sheet3.cell_value(i,6)
	text_str = sheet3.cell_value(i,5)
	if(choose3 == 1):
		sum += 1
		pos_sum += 1
		f_pos.write(str(text_str))
		f_pos.write('\n')
	elif(choose3 == 0):
		sum += 1
		neu_sum += 1
		f_neu.write(str(text_str))
		f_neu.write('\n')
	elif(choose3 == -1):
		sum += 1
		neg_sum += 1
		f_neg.write(str(text_str))
		f_neg.write('\n')
	else:
		#None
		
		sum += 1
		del_sum += 1
		f_del.write(str(text_str))
		f_del.write('\n')
		
#实验练习筛选
for i in range(nrows4):
    #获取情感倾向列的标签值(行列序号从0开始)
	choose4 = sheet4.cell_value(i,7)
	text_str = sheet4.cell_value(i,6)
	if(choose4 == 1):
		sum += 1
		pos_sum += 1
		f_pos.write(str(text_str))
		f_pos.write('\n')
	elif(choose4 == 0):
		sum += 1
		neu_sum += 1
		f_neu.write(str(text_str))
		f_neu.write('\n')
	elif(choose4 == -1):
		sum += 1
		neg_sum += 1
		f_neg.write(str(text_str))
		f_neg.write('\n')
	else:
		#None
		
		sum += 1
		del_sum += 1
		f_del.write(str(text_str))
		f_del.write('\n')
		

f_pos.close()
f_neu.close()
f_neg.close()
f_del.close()
print("累计语料",sum)#6947//6786
print("累计pos语料",pos_sum)#1422
print("累计neu语料",neu_sum)#3972
print("累计neg语料",neg_sum)#1374
print("累计del语料",del_sum)#179
