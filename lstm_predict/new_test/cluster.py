import pandas
import matplotlib.pyplot as plt

import numpy
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
'''
dataset = pandas.read_csv('international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3)
plt.plot(dataset)
plt.show()
'''
# load the dataset
#取第一列
dataframe = pandas.read_csv('periodData.csv', usecols=[0], engine='python', skipfooter=1)
#通过.values得到dataframe的值，返回shape是(144, 1)的数组形式
dataset = dataframe.values 
#把dataset里的所有数据从整型变为浮点型
dataset = dataset.astype('float32') 

print("dataframe:", dataframe)
#print("dataset:", dataset)
setValue = dataset
#dataset数据归一化，[0, 1]
scaler = MinMaxScaler(feature_range=(-1, 1))
dataset = scaler.fit_transform(dataset)
print("new dataset:")
classes = ""
for i in range(len(dataset)):
	if dataset[i] <= -0.5:
		classes = "负面"
	elif dataset[i] < 0.5:
		classes = "一般"
	else:
		classes = "正面"
	#print("dataset["+str(i)+"]=", dataset[i], classes)
	print(setValue[i], dataset[i], classes)
