#! /bin/env python
# -*- coding: utf-8 -*-
"""
多位学生在13周内的情感变化
"""

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.gridspec as gridspec

if __name__=='__main__':

    emo1 = [2.0, 0.0, 0.0, 0.0, 0.75, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0]
    emo2 = [0.0, 2.0, 0.0, -0.5, 0.0, 0.75, 0.0, 0.0, -2.0, 0.0, 0.0, 0.0, -1.5]
    emo3 = [1.0, -2.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.75, 0.0, -0.75, 2.25, 1.5]
    emo4 = [3.5, 0.0, 0.0, 0.0, 0.0, 2.5, 2.0, -1.5, 0.0, 0.0, -0.75, 0.0, 0.0]
    def aveEmo(emo):
        return np.mean(emo)
    def varEmo(emo):
        return np.var(emo)

    print("学生A情感值数组：",emo2)
    print("学生A情感均值：",aveEmo(emo2))
    print("学生A情感方差：",varEmo(emo2))
    print("学生B情感值数组：",emo3)
    print("学生B情感均值：",aveEmo(emo3))
    print("学生B情感方差：",varEmo(emo3))
    print("学生C情感值数组：",emo4)
    print("学生C情感均值：",aveEmo(emo4))
    print("学生C情感方差：",varEmo(emo4))
    #设置x,y轴
    x = [x for x in range(1,14)]
    #定义figure
    plt.figure()
    plt.title('Result Analysis')
    plt.plot(x, emo2, color='green', label='stu_A')
    plt.plot(x, emo2, 'gs')
    plt.plot(x, emo3, color='red', label='stu_B')
    plt.plot(x, emo3, 'r*')
    plt.plot(x, emo4,  color='blue', label='stu_C')
    plt.plot(x, emo4, 'bd')
    plt.legend() # 显示图例
    #plt.plot(x,y)
    plt.xlabel("week")#X轴标签
    plt.ylabel("emoValue")#Y轴标签 
    plt.show()  
    