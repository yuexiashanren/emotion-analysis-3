'''
读取表格中属于各种情感值的数据，存储到情感倾向.csv中
'''
# -*- coding: utf-8 -*-
import xlrd
import numpy

xlsfile1 = r"../课前预习.xls"# 打开课前预习
xlsfile2 = r"../课后作业.xls"# 打开课后作业
xlsfile4 = r"../实验练习.xls"# 打开实验练习

book1 = xlrd.open_workbook(xlsfile1)#得到Excel文件的book对象，实例化对象
book2 = xlrd.open_workbook(xlsfile2)
book4 = xlrd.open_workbook(xlsfile4)

sheet1 = book1.sheet_by_index(0) # 通过sheet索引获得课前预习sheet对象
sheet2 = book2.sheet_by_index(0)
sheet4 = book4.sheet_by_index(0)

nrows1 = sheet1.nrows    # 获取行总数
ncols1 = sheet1.ncols    #获取列总数
print ("课前预习总/列数",nrows1,ncols1)

nrows2 = sheet2.nrows    # 获取行总数
ncols2 = sheet2.ncols    #获取列总数
print ("课后作业总行/列数",nrows2,ncols2)

nrows4 = sheet4.nrows    # 获取行总数
ncols4 = sheet4.ncols    #获取列总数
print ("实验练习总行/列数",nrows4,ncols4)

#每周的问题数量[课前，课后，实验]*周次
que_num = [[5,7,0], [5,0,0], [0,7,5], [5,7,5], [5,7,0], 
				[5,7,10], [5,7,0], [5,7,0], [5,7,0], [8,10,0], 
				[7,6,0], [5,7,0], [5,7,10]]
#初始化每周的学生人数[课前，课后，实验]*周次
stu_sum = [ [0] * 3 for i in range(13)]
#初始化每周的总成绩[课前，课后，实验]*周次
sco_sum = [ [0] * 3 for i in range(13)]
#初始化每周的平均成绩[课前，课后，实验]*周次
sco_ave = [ [0] * 3 for i in range(13)]

f = open('./dif_degree.txt', 'w', encoding='utf-8')

#课前预习筛选
for i in range(nrows1):
    #获取情感倾向列的标签值(行列序号从0开始)
	week = sheet1.cell_value(i,4)
	score = sheet1.cell_value(i,5)
	if(week == 1):
		sco_sum[0][0] += score
		stu_sum[0][0] += 1
	elif(week == 2):
		sco_sum[1][0] += score
		stu_sum[1][0] += 1
	elif(week == 3):
		sco_sum[2][0] += score
		stu_sum[2][0] += 1
	elif(week == 4):
		sco_sum[3][0] += score
		stu_sum[3][0] += 1
	elif(week == 5):
		sco_sum[4][0] += score
		stu_sum[4][0] += 1
	elif(week == 6):
		sco_sum[5][0] += score
		stu_sum[5][0] += 1
	elif(week == 7):
		sco_sum[6][0] += score
		stu_sum[6][0] += 1
	elif(week == 8):
		sco_sum[7][0] += score
		stu_sum[7][0] += 1
	elif(week == 9):
		sco_sum[8][0] += score
		stu_sum[8][0] += 1
	elif(week == 10):
		sco_sum[9][0] += score
		stu_sum[9][0] += 1
	elif(week == 11):
		sco_sum[10][0] += score
		stu_sum[10][0] += 1
	elif(week == 12):
		sco_sum[11][0] += score
		stu_sum[11][0] += 1
	elif(week == 13):
		sco_sum[12][0] += score
		stu_sum[12][0] += 1

#课后作业筛选
for i in range(nrows2):
    #获取情感倾向列的标签值(行列序号从1开始)
	week = sheet2.cell_value(i,4)
	score = sheet2.cell_value(i,5)
	if(week == 1):
		sco_sum[0][1] += score
		stu_sum[0][1] += 1
	elif(week == 2):
		sco_sum[1][1] += score
		stu_sum[1][1] += 1
	elif(week == 3):
		sco_sum[2][1] += score
		stu_sum[2][1] += 1
	elif(week == 4):
		sco_sum[3][1] += score
		stu_sum[3][1] += 1
	elif(week == 5):
		sco_sum[4][1] += score
		stu_sum[4][1] += 1
	elif(week == 6):
		sco_sum[5][1] += score
		stu_sum[5][1] += 1
	elif(week == 7):
		sco_sum[6][1] += score
		stu_sum[6][1] += 1
	elif(week == 8):
		sco_sum[7][1] += score
		stu_sum[7][1] += 1
	elif(week == 9):
		sco_sum[8][1] += score
		stu_sum[8][1] += 1
	elif(week == 10):
		sco_sum[9][1] += score
		stu_sum[9][1] += 1
	elif(week == 11):
		sco_sum[10][1] += score
		stu_sum[10][1] += 1
	elif(week == 12):
		sco_sum[11][1] += score
		stu_sum[11][1] += 1
	elif(week == 13):
		sco_sum[12][1] += score
		stu_sum[12][1] += 1
		
#实验练习筛选
for i in range(nrows4):
    #获取情感倾向列的标签值(行列序号从1开始)
	week = sheet4.cell_value(i,4)
	score = sheet4.cell_value(i,5)
	if(week == 1):
		sco_sum[0][2] += score
		stu_sum[0][2] += 1
	elif(week == 2):
		sco_sum[1][2] += score
		stu_sum[1][2] += 1
	elif(week == 3):
		sco_sum[2][2] += score
		stu_sum[2][2] += 1
	elif(week == 4):
		sco_sum[3][2] += score
		stu_sum[3][2] += 1
	elif(week == 5):
		sco_sum[4][2] += score
		stu_sum[4][2] += 1
	elif(week == 6):
		sco_sum[5][2] += score
		stu_sum[5][2] += 1
	elif(week == 7):
		sco_sum[6][2] += score
		stu_sum[6][2] += 1
	elif(week == 8):
		sco_sum[7][2] += score
		stu_sum[7][2] += 1
	elif(week == 9):
		sco_sum[8][2] += score
		stu_sum[8][2] += 1
	elif(week == 10):
		sco_sum[9][2] += score
		stu_sum[9][2] += 1
	elif(week == 11):
		sco_sum[10][2] += score
		stu_sum[10][2] += 1
	elif(week == 12):
		sco_sum[11][2] += score
		stu_sum[11][2] += 1
	elif(week == 13):
		sco_sum[12][2] += score
		stu_sum[12][2] += 1

for i in range(0,13):
	for j in range(0,3):
		if stu_sum[i][j] != 0:
			sco_ave[i][j] = '{:.2f}'.format(sco_sum[i][j]/stu_sum[i][j])
		else:
			sco_ave[i][j] = '{:.2f}'.format(0)
print("总成绩：",sco_sum)
print("学生：",stu_sum)

for i in range(0,13):
	sco_ave[i] = list(map(float,sco_ave[i]))
print("平均成绩：",sco_ave)
print("题目数量：",que_num)
print("题目正确率：",sco_ave[0][0]/que_num[0][0])
'''
print("实际学生人数：",nrows1+nrows2+nrows4)
s = 0
for i in range(0,13):
	s += sum(stu_sum[i])
print("输出学生人数：",s)
'''