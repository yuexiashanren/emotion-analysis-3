"""
综合所有数据在13周内的情感分析
1）每周独立进行分析，即每周的情感分析仅包括本周的数据
2）周次累计进行分析，即每周的情感分析数据包含了本周包括之前周次的数据
"""
import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.gridspec as gridspec

neg = [107, 85, 168, 213, 83, 181, 107, 79, 92, 119, 95, 117, 141]
neu = [357, 249, 430, 587, 336, 475, 342, 399, 381, 351, 230, 319, 444]
pos = [28, 18, 54, 47, 23, 52, 23, 33, 30, 33, 15, 46, 54]
sum1 = [492, 352, 652, 847, 442, 708, 472, 511, 503, 503, 340, 482, 639]

pos_rate = [ 0 for i in range(13)]
neg_rate = [ 0 for i in range(13)]
pos_rate1 = [ 0 for i in range(13)]
neg_rate1 = [ 0 for i in range(13)]
for i in range(13):
	pos_rate[i] = float('{:.4f}'.format(sum(pos[:i+1])/sum(sum1[:i+1])))
	neg_rate[i] = float('{:.4f}'.format(sum(neg[:i+1])/sum(sum1[:i+1])))
	pos_rate1[i] = float('{:.4f}'.format(pos[i]/sum1[i]))
	neg_rate1[i] = float('{:.4f}'.format(neg[i]/sum1[i]))


#设置x,y轴
x = [x for x in range(1,14)]
#定义figure
plt.figure()
#分隔figure,3行3列
gs = gridspec.GridSpec(2, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, :])
#绘制图像
ax1.plot(x, neg_rate, color='red')
ax1.plot(x, neg_rate1, color='blue')
ax1.set_title('negative')
ax2.plot(x, pos_rate, color='red')
ax2.plot(x, pos_rate1, color='blue')
ax2.set_title('positive')
plt.xlabel("week")#X轴标签
plt.ylabel("percent")#Y轴标签
plt.show()
