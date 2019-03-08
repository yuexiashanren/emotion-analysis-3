import matplotlib.pyplot as plt  
import matplotlib.gridspec as gridspec
import numpy as np 

stuA = [1, -1, 0, 0, 0, 0, 0, 1, 1, -1, -1, 1, 1]
stuA_w = [1.0, -3.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.4, -3.7, -1.4, 4.2, 2.8]
stuB = [0, 0, -1, 1, 0, 2, 0, -1, -1, 0, -1, -1, 0]
stuB_w = [0.9, 0.0, -4.2, 2.4, 0.0, 4.2, 0.0, -2.8, -1.4, 0.0, -1.4, -4.2, 0.0]
stuC = [-1, 0, 0, 0, 0, 0, -2, -2, -1, -2, 0, 0, -1]
stuC_w = [-1.0, 0.0, 0.0, 0.0, -2.3, 0.0, -6.5, -4.2, -3.7, -6.5, 0.4, 0.0, -3.7]

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
ax1.plot(x, stuA, 'ko-.', label='no')
ax1.plot(x, stuA_w, 'k*:', label='yes')
ax1.set_title('stuA')
ax2.plot(x, stuB, 'ko-.')
ax2.plot(x, stuB_w, 'k*:')
ax2.set_title('stuB')
ax3.plot(x, stuC, 'ko-.')
ax3.plot(x, stuC_w, 'k*:')
ax3.set_title('stuC')
plt.xlabel("week")#X轴标签
plt.ylabel("emoValue")#Y轴标签 
plt.show()
'''
plt.title('Result Analysis')
plt.plot(x, pos, color='green', label='positive')
plt.plot(x, pos, 'go')
plt.plot(x, neg, color='red', label='negative')
plt.plot(x, neg, 'ro')
plt.plot(x, neu,  color='blue', label='neural')
plt.plot(x, neu, 'bo')
plt.legend() # 显示图例
#plt.plot(x,y)
plt.xlabel("week")#X轴标签
plt.ylabel("percent")#Y轴标签 
plt.show()  
'''
def aveEmo(emo):
        return float('{:.4f}'.format(np.mean(emo)))
def varEmo(emo):
    return float('{:.4f}'.format(np.var(emo)))

print("学生A情感均值：",aveEmo(stuA))
print("添加权重学生A情感均值：",aveEmo(stuA_w))
print("学生A情感方差：",varEmo(stuA))
print("添加权重学生A情感方差：",varEmo(stuA_w))

print("学生B情感均值：",aveEmo(stuB))
print("添加权重学生B情感均值：",aveEmo(stuB_w))
print("学生B情感方差：",varEmo(stuB))
print("添加权重学生B情感方差：",varEmo(stuB_w))

print("学生C情感均值：",aveEmo(stuC))
print("添加权重学生C情感均值：",aveEmo(stuC_w))
print("学生C情感方差：",varEmo(stuC))
print("添加权重学生C情感方差：",varEmo(stuC_w))