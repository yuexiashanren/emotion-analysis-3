'''
计算题目正确率，定义知识点难度
'''
# -*- coding: utf-8 -*-
import xlrd
import numpy
import matplotlib.pyplot as plt 

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
que_num = [[5,7,0],[5,0,0],[0,7,5],[5,7,5],[5,7,0],
			[5,7,10],[5,7,0],[5,7,0],[5,7,0],[8,10,0],
			[7,6,0],[5,7,0],[5,7,20]]
#初始化每周的学生人数[课前，课后，实验]*周次
stu_sum = [ [0] * 3 for i in range(13)]
#初始化每周的总成绩[课前，课后，实验]*周次
sco_sum = [ [0] * 3 for i in range(13)]
#初始化每周的平均成绩[课前，课后，实验]*周次
sco_ave = [ [0] * 3 for i in range(13)]
#初始化题目的正确率[课前，课后，实验]*周次
cor_rte = [ [0] * 3 for i in range(13)]
#初始化周次的正确率1-13周
week_rate = [ 0 for i in range(13)]

#课前习题正确率
classBefore = [ 0 for i in range(13)]
#课后习题正确率
classAfter = [ 0 for i in range(13)]

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

#总成绩=所有学生的成绩累计和
print("各阶段总成绩：",sco_sum)
print("各阶段学生总数：",stu_sum)
'''
#str=>float
	sco_ave = list(map(float,sco_ave))
'''
for i in range(0,13):
	for j in range(0,3):
		if stu_sum[i][j] != 0:
			sco_ave[i][j] = float('{:.2f}'.format(sco_sum[i][j]/stu_sum[i][j]))
		else:
			sco_ave[i][j] = float('{:.2f}'.format(0))
#平均成绩=全体学生总成绩/学生总人数
print("各阶段学生平均成绩：",sco_ave)
print("各阶段题目数量：",que_num)
for i in range(0,13):
	for j in range(0,3):
		if que_num[i][j] != 0:
			cor_rte[i][j] = float('{:.4f}'.format(sco_ave[i][j]/que_num[i][j]))			
		else:
			cor_rte[i][j] = float('{:.2f}'.format(0))
#题目正确率 = 课前/课后/实验阶段的平均得分/课前/课后/实验阶段的总分
print("各阶段题目正确率：",cor_rte)
for i in range(0,13):
	if cor_rte[i][0] != 0:
		classBefore[i] = cor_rte[i][0]
	else:
		classBefore[i] = classBefore[i-1]
	if cor_rte[i][1] != 0:
		classAfter[i] = cor_rte[i][1]
	else:
		classAfter[i] = classAfter[i-1]
	week_rate[i] = float('{:.4f}'.format(
						(classBefore[i]*stu_sum[i][0]+classAfter[i]*stu_sum[i][1])/(stu_sum[i][0]+stu_sum[i][1])
						))

#课前预习正确率
print("课前预习正确率:",classBefore)
#课后作业正确率
print("课后作业正确率:",classAfter)
#周次的平均正确率 = 课前/课后/实验阶段正确率*该阶段人数/该周次的总人数
print("学习周题目正确率：",week_rate)

#设置x,y轴
x = [x for x in range(1,14)]
#定义figure
plt.figure()

plt.title('Result Analysis')
#plt.plot(x, classBefore, color='green')
#plt.plot(x, classBefore, color='gray', linestyle=':', marker='^', label='class_before')
plt.plot(x, classBefore, 'k*:', label='Before')
#plt.plot(x, classAfter, color='red')
plt.plot(x, classAfter, 'kd--', label='After')
#plt.plot(x, week_rate, color='red')
#plt.plot(x, week_rate, 'r*', label='average')
plt.legend() # 显示图例
#plt.plot(x,y)
plt.xlabel("week")#X轴标签
plt.ylabel("accuracy")#Y轴标签 
plt.show()  
