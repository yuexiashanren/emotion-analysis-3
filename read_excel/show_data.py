import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.gridspec as gridspec

neg = ['3.86%', '3.12%', '3.53%', '4.13%', '2.49%', '3.39%', '4.03%', '7.63%', '3.18%', '4.77%', '8.24%', '3.53%', '4.07%']
neu = ['0.00%', '0.28%', '0.15%', '0.00%', '0.00%', '0.85%', '1.06%', '1.17%', '0.00%', '0.00%', '0.00%', '0.21%', '0.31%']
pos = ['96.14%', '96.59%', '96.32%', '95.87%', '97.51%', '95.76%', '94.92%', '91.19%', '96.82%', '95.23%', '91.76%', '96.27%', '95.62%']

#设置x,y轴
x = [x for x in range(1,14)]
#定义figure
plt.figure()
#分隔figure,3行3列
gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, :])
ax3 = plt.subplot(gs[2, :])
#绘制图像
ax1.plot(x, neg, color='red')
ax1.set_title('negative')
ax2.plot(x, neu, color='skyblue')
ax2.set_title('neural')
ax3.plot(x, pos, color='green')
ax3.set_title('positive')
plt.show()


plt.title('Result Analysis')
plt.plot(x, pos, color='green', label='positive')
plt.plot(x, neg, color='red', label='negative')
plt.plot(x, neu,  color='skyblue', label='neural')
plt.legend() # 显示图例
#plt.plot(x,y)
plt.xlabel("week(w)")#X轴标签
plt.ylabel("percent(%)")#Y轴标签 
plt.show()
#plt.savefig("result.png")
