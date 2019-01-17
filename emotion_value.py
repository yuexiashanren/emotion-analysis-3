'''
课前/课后/每周总结情感值*权重
'''
# -*- coding: utf-8 -*-

#情感数组赋值
def changeArr(a,b):
	l = 0
	arr = [ [0]*a for i in range(b) ]
	#情感值取-1/0/1
	for i in range(-1,2):
		for j in range(-1,2):
			for k in range(-1,2):
				arr[l][0] = i
				arr[l][1] = j
				arr[l][2] = k
				l += 1
	return arr
#print(changeArr(3,27))
#添加权重
def addWeight(weight,arr):
	arrLength = len(arr)
	emoValue = [ 0 for i in range(arrLength)]
	for i in range(arrLength):
		emoValue[i] = arr[i][0]*weight[0]+arr[i][1]*weight[1]+arr[i][2]*weight[2]
	return emoValue
#定义权重
weight = [1,1.5,2]
#定义情感数组
arr = changeArr(3,27)
print("emoValue",addWeight(weight,arr))