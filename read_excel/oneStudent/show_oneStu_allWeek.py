#! /bin/env python
# -*- coding: utf-8 -*-
"""
多位学生在13周内的情感变化
"""

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.gridspec as gridspec

if __name__=='__main__':

    emo1 = [-3.7, -3.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    emo2 = [0.0, 3.7, 0.0, -6.5, 0.0, 0.0, 0.0, 0.0, -3.7, 0.0, -1.4, 0.0, 1.5]
    emo3 = [1.0, -3.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.4, -3.7, -1.4, 4.2, 2.8]
    emo4 = [0.9, 0.0, -4.2, 2.4, 0.0, 4.2, 0.0, -2.8, -1.4, 0.0, -1.4, -4.2, 0.0]
    emo5 = [0.0, 0.0, 0.0, -2.2, 0.0, 0.0, -3.7, 0.0, 4.2, 3.7, -2.4, 3.2, 3.7]
    emo6 = [0.0, 0.0, 0.0, -1.5, 0.0, 0.0, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 0.0]
    emo7 = [-1.0, 0.0, 0.0, 0.0, -2.3, 0.0, -6.5, -4.2, -3.7, -6.5, 0.4, 0.0, -3.7]
    meo8 = [3.7, 0.0, 0.0, 0.0, 0.0, 5.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.5]
    def aveEmo(emo):
        return float('{:.4f}'.format(np.mean(emo)))
    def varEmo(emo):
        return float('{:.4f}'.format(np.var(emo)))

    stuA = emo3
    stuB = emo4
    stuC = emo7
    print("学生A情感值数组：",stuA)
    print("学生A情感均值：",aveEmo(stuA))
    print("学生A情感方差：",varEmo(stuA))
    print("学生B情感值数组：",stuB)
    print("学生B情感均值：",aveEmo(stuB))
    print("学生B情感方差：",varEmo(stuB))
    print("学生C情感值数组：",stuC)
    print("学生C情感均值：",aveEmo(stuC))
    print("学生C情感方差：",varEmo(stuC))
    #设置x,y轴
    x = [x for x in range(1,14)]
    #定义figure
    plt.figure()
    plt.title('Result Analysis')
    #plt.plot(x, emo2, color='green')
    plt.plot(x, stuA, 'ko-.', label='stu_A')
    #plt.plot(x, emo3, color='red')
    plt.plot(x, stuB, 'k*:', label='stu_B')
    #plt.plot(x, emo4,  color='blue')
    plt.plot(x, stuC, 'kd--', label='stu_C')
    plt.legend() # 显示图例
    #plt.plot(x,y)
    plt.xlabel("week")#X轴标签
    plt.ylabel("emoValue")#Y轴标签 
    plt.show()  
    