'''
计算题目正确率，定义知识点难度
'''
# -*- coding: utf-8 -*-
import xlrd
import numpy
import matplotlib.pyplot as plt 

emo = [ [0] * 3 for i in range(27)]
res = [ 0 for i in range(27)]
wgt = [1,1.5,2]
l = 0
for i in range(-1,2):
	for j in range(-1,2):
		for k in range(-1,2):
			emo[l][0] = i
			emo[l][1] = j
			emo[l][2] = k
			l += 1
for i in range(27):
	res[i] = emo[i][0]*wgt[0]+emo[i][1]*wgt[1]+emo[i][2]*wgt[2]
print("res",res)