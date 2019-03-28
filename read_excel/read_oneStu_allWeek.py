'''
读取某同学n的课前、课后和每周总结数据
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

nrows1 = sheet1.nrows    # 获取行总数
ncols1 = sheet1.ncols    #获取列总数
nrows2 = sheet2.nrows
ncols2 = sheet2.ncols
nrows3 = sheet3.nrows
ncols3 = sheet3.ncols
print ("课前预习总行/列数",nrows1,ncols1)
print ("课后作业总行/列数",nrows2,ncols2)
print ("每周总结总行/列数",nrows3,ncols3)
f0 = open('./oneStudent/oneStu_allWeek.txt', 'w', encoding='utf-8')
#筛选同学X在n周内的所有课前、课后和每周总结评论，空的补“null”
def choiceAllText(name,week):
	print("学生姓名：",name)
	for k in range(1,week+1):
		flag1 = "false"
		flag2 = "false"
		flag3 = "false"
		#课前预习筛选
		for i in range(nrows1):
			a = sheet1.cell_value(i,2)#获取姓名
			b = sheet1.cell_value(i,4)#获取周次
			c = sheet1.cell_value(i,6)#获取评论文本
			text = "null"
			if(a == name and b == k):
				flag1 = "true"
				print(k,"周课前：",c)
				f0.write(c)
				f0.write('\n')
				break
		if flag1 == "false":
			print(k,"周课前：null")
			f0.write("null")
			f0.write('\n')
		#课后作业筛选
		for i in range(nrows2):
			a = sheet2.cell_value(i,2)#获取姓名
			b = sheet2.cell_value(i,4)#获取周次
			c = sheet2.cell_value(i,6)#获取评论文本
			if(a == name and b == k):
				flag2 = "true"
				print(k,"周课后：",c)
				f0.write(c)
				f0.write('\n')
				break
		if flag2 == "false":
			print(k,"周课后：null")
			f0.write("null")
			f0.write('\n')
		#每周总结筛选
		for i in range(nrows3):
			a = sheet3.cell_value(i,2)#获取姓名
			b = sheet3.cell_value(i,4)#获取周次
			c = sheet3.cell_value(i,5)#获取评论文本
			if(a == name and b == k):
				flag3 = "true"
				print(k,"周每周：",c)
				f0.write(c)
				f0.write('\n')
				break
		if flag3 == "false":
			print(k,"周每周：null")
			f0.write("null")
			f0.write('\n')

name1 = "文习尚"#m1701
name2 = "林雨钦"#m1702
name3 = "赵华源"#m1703
name4 = "徐海标"#m1704
name5 = "李宵"
name6 = "朱智"
name7 = "刘晓稳"
name8 = "朱浩杰"
week = 13
choiceAllText(name4,week)