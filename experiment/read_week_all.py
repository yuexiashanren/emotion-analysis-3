'''
读取课前预习/课后作业/每周总结/实验练习.xls中的数据，
存储到weeks/下的01-13/del.txt中
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

sum = 0
f1 = open('./weeks/01.txt', 'w', encoding='utf-8')
f2 = open('./weeks/02.txt', 'w', encoding='utf-8')
f3 = open('./weeks/03.txt', 'w', encoding='utf-8')
f4 = open('./weeks/04.txt', 'w', encoding='utf-8')
f5 = open('./weeks/05.txt', 'w', encoding='utf-8')
f6 = open('./weeks/06.txt', 'w', encoding='utf-8')
f7 = open('./weeks/07.txt', 'w', encoding='utf-8')
f8 = open('./weeks/08.txt', 'w', encoding='utf-8')
f9 = open('./weeks/09.txt', 'w', encoding='utf-8')
f10 = open('./weeks/10.txt', 'w', encoding='utf-8')
f11 = open('./weeks/11.txt', 'w', encoding='utf-8')
f12 = open('./weeks/12.txt', 'w', encoding='utf-8')
f13 = open('./weeks/13.txt', 'w', encoding='utf-8')
f14 = open('./weeks/del.txt', 'w', encoding='utf-8')


#课前预习筛选
for i in range(nrows1):
    #获取情感倾向列的标签值(行列序号从0开始)
	choose1 = sheet1.cell_value(i,4)
	text_str = sheet1.cell_value(i,6)
	if(choose1 == 1):
		sum += 1
		f1.write(str(text_str))
		f1.write('\n')
	elif(choose1 == 2):
		sum += 1
		f2.write(str(text_str))
		f2.write('\n')
	elif(choose1 == 3):
		sum += 1
		f3.write(str(text_str))
		f3.write('\n')
	elif(choose1 == 4):
		sum += 1
		f4.write(str(text_str))
		f4.write('\n')
	elif(choose1 == 5):
		sum += 1
		f5.write(str(text_str))
		f5.write('\n')
	elif(choose1 == 6):
		sum += 1
		f6.write(str(text_str))
		f6.write('\n')
	elif(choose1 == 7):
		sum += 1
		f7.write(str(text_str))
		f7.write('\n')
	elif(choose1 == 8):
		sum += 1
		f8.write(str(text_str))
		f8.write('\n')
	elif(choose1 == 9):
		sum += 1
		f9.write(str(text_str))
		f9.write('\n')
	elif(choose1 == 10):
		sum += 1
		f10.write(str(text_str))
		f10.write('\n')
	elif(choose1 == 11):
		sum += 1
		f11.write(str(text_str))
		f11.write('\n')
	elif(choose1 == 12):
		sum += 1
		f12.write(str(text_str))
		f12.write('\n')
	elif(choose1 == 13):
		sum += 1
		f13.write(str(text_str))
		f13.write('\n')
	else:
		#None
		
		sum += 1
		f14.write(str(text_str))
		f14.write('\n')

#课后作业筛选
for i in range(nrows2):
    #获取情感倾向列的标签值(行列序号从1开始)
	choose2 = sheet2.cell_value(i,4)
	text_str = sheet2.cell_value(i,6)
	if(choose2 == 1):
		sum += 1
		f1.write(str(text_str))
		f1.write('\n')
	elif(choose2 == 2):
		sum += 1
		f2.write(str(text_str))
		f2.write('\n')
	elif(choose2 == 3):
		sum += 1
		f3.write(str(text_str))
		f3.write('\n')
	elif(choose2 == 4):
		sum += 1
		f4.write(str(text_str))
		f4.write('\n')
	elif(choose2 == 5):
		sum += 1
		f5.write(str(text_str))
		f5.write('\n')
	elif(choose2 == 6):
		sum += 1
		f6.write(str(text_str))
		f6.write('\n')
	elif(choose2 == 7):
		sum += 1
		f7.write(str(text_str))
		f7.write('\n')
	elif(choose2 == 8):
		sum += 1
		f8.write(str(text_str))
		f8.write('\n')
	elif(choose2 == 9):
		sum += 1
		f9.write(str(text_str))
		f9.write('\n')
	elif(choose2 == 10):
		sum += 1
		f10.write(str(text_str))
		f10.write('\n')
	elif(choose2 == 11):
		sum += 1
		f11.write(str(text_str))
		f11.write('\n')
	elif(choose2 == 12):
		sum += 1
		f12.write(str(text_str))
		f12.write('\n')
	elif(choose2 == 13):
		sum += 1
		f13.write(str(text_str))
		f13.write('\n')
	else:
		#None
		
		sum += 1
		f14.write(str(text_str))
		f14.write('\n')
		
#每周总结筛选
for i in range(nrows3):
    #获取情感倾向列的标签值(行列序号从1开始)
	choose3 = sheet3.cell_value(i,4)
	text_str = sheet3.cell_value(i,5)
	if(choose3 == 1):
		sum += 1
		f1.write(str(text_str))
		f1.write('\n')
	elif(choose3 == 2):
		sum += 1
		f2.write(str(text_str))
		f2.write('\n')
	elif(choose3 == 3):
		sum += 1
		f3.write(str(text_str))
		f3.write('\n')
	elif(choose3 == 4):
		sum += 1
		f4.write(str(text_str))
		f4.write('\n')
	elif(choose3 == 5):
		sum += 1
		f5.write(str(text_str))
		f5.write('\n')
	elif(choose3 == 6):
		sum += 1
		f6.write(str(text_str))
		f6.write('\n')
	elif(choose3 == 7):
		sum += 1
		f7.write(str(text_str))
		f7.write('\n')
	elif(choose3 == 8):
		sum += 1
		f8.write(str(text_str))
		f8.write('\n')
	elif(choose3 == 9):
		sum += 1
		f9.write(str(text_str))
		f9.write('\n')
	elif(choose3 == 10):
		sum += 1
		f10.write(str(text_str))
		f10.write('\n')
	elif(choose3 == 11):
		sum += 1
		f11.write(str(text_str))
		f11.write('\n')
	elif(choose3 == 12):
		sum += 1
		f12.write(str(text_str))
		f12.write('\n')
	elif(choose3 == 13):
		sum += 1
		f13.write(str(text_str))
		f13.write('\n')
	else:
		#None
		
		sum += 1
		f14.write(str(text_str))
		f14.write('\n')

#实验练习筛选
for i in range(nrows4):
    #获取情感倾向列的标签值(行列序号从1开始)
	choose4 = sheet4.cell_value(i,4)
	text_str = sheet4.cell_value(i,6)
	if(choose4 == 1):
		sum += 1
		f1.write(str(text_str))
		f1.write('\n')
	elif(choose4 == 2):
		sum += 1
		f2.write(str(text_str))
		f2.write('\n')
	elif(choose4 == 3):
		sum += 1
		f3.write(str(text_str))
		f3.write('\n')
	elif(choose4 == 4):
		sum += 1
		f4.write(str(text_str))
		f4.write('\n')
	elif(choose4 == 5):
		sum += 1
		f5.write(str(text_str))
		f5.write('\n')
	elif(choose4 == 6):
		sum += 1
		f6.write(str(text_str))
		f6.write('\n')
	elif(choose4 == 7):
		sum += 1
		f7.write(str(text_str))
		f7.write('\n')
	elif(choose4 == 8):
		sum += 1
		f8.write(str(text_str))
		f8.write('\n')
	elif(choose4 == 9):
		sum += 1
		f9.write(str(text_str))
		f9.write('\n')
	elif(choose4 == 10):
		sum += 1
		f10.write(str(text_str))
		f10.write('\n')
	elif(choose4 == 11):
		sum += 1
		f11.write(str(text_str))
		f11.write('\n')
	elif(choose4 == 12):
		sum += 1
		f12.write(str(text_str))
		f12.write('\n')
	elif(choose4 == 13):
		sum += 1
		f13.write(str(text_str))
		f13.write('\n')
	else:
		#None
		
		sum += 1
		f14.write(str(text_str))
		f14.write('\n')

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f10.close()
f11.close()
f12.close()
f13.close()
f14.close()

print("累计语料",sum)#6947

