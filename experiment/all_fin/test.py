import matplotlib.pyplot as plt

x = [x for x in range(1,14)]
xx = [x for x in range(0,13)]

neg = [0.23, 0.24, 0.27, 0.25, 0.19, 0.26, 0.23, 0.16, 0.18, 0.24, 0.28, 0.24, 0.22]
neu = [0.72, 0.71, 0.66, 0.69, 0.76, 0.67, 0.72, 0.78, 0.76, 0.7, 0.67, 0.66, 0.69]
pos = [0.06, 0.05, 0.08, 0.06, 0.05, 0.07, 0.05, 0.06, 0.06, 0.07, 0.04, 0.1, 0.08]

acc = [0.8, 0.68, 0.71, 0.69, 0.84, 0.86, 0.79, 0.88, 0.9, 0.76, 0.87, 0.71, 0.76]
#绘制整体柱状图
addPG = [addPG for addPG in range(len(pos))]
for i in range(len(pos)):
	addPG[i] = float('{:.2f}'.format(pos[i]+neu[i]))

plt.title('Result Analysis')
plt.bar(range(len(pos)), pos, label='positive',fc = 'Chartreuse')
plt.bar(range(len(pos)), neu, bottom=pos, label='neural',fc = 'OrangeRed')
plt.bar(range(len(pos)), neg, bottom=addPG, label='negative',tick_label = x, fc = 'DodgerBlue')
plt.plot(xx, acc, color='yellow', label='accuracy')
plt.plot(xx, acc, 'go')
plt.legend()
#plt.plot(x,y)
plt.xlabel("week")#X轴标签
plt.ylabel("percent")#Y轴标签 
plt.show()