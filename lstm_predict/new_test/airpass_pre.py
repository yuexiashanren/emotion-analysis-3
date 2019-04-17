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
dataframe = pandas.read_csv('international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3)#原有两列，一列是时间，一列是乘客数量，这里利用usecols=[1],只取了乘客数量一列
dataset = dataframe.values #通过.values得到dataframe的值，返回shape是(144, 1)的数组形式
dataset = dataset.astype('float32') #把dataset里的所有数据从整型变为浮点型

print("dataframe:", dataframe)
print("dataset:", dataset)

#dataset数据归一化，[0, 1]
scaler = MinMaxScaler(feature_range=(0, 1))
dataset = scaler.fit_transform(dataset)
print("new dataset:", dataset)