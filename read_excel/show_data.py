import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.gridspec as gridspec

neg = [3.86, 13.12, 23.53, 14.13, 42.49]
neu = [0.00, 14.28, 70.15, 80.00, 50.00]
pos = [66.14, 76.59, 36.32, 25.87, 10.00]

#设置x,y轴
x = [x for x in range(1,6)]
'''
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

'''
#fig = plt.figure(num=1, figsize=(15, 8),dpi=80)
plt.title('Result Analysis')

plt.plot(x, neg)
#plt.plot(neg, 'o', color='red')
plt.plot(x, neu)
#plt.plot(neu, 'o', color='skyblue')
plt.plot(x, pos)
#plt.plot(pos, 'o', color='green')
plt.legend() # 显示图例
#plt.plot(x,y)
#plt.ylim(0, 100)
#plt.yticks(np.linspace(0,100,28,endpoint=True)) 

plt.xlabel("week(w)")#X轴标签
plt.ylabel("percent(%)")#Y轴标签 
plt.show()
#plt.savefig("result.png")
