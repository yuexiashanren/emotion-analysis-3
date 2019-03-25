#! /bin/env python
# -*- coding: utf-8 -*-
"""
多位学生在13周内的情感变化
"""

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.gridspec as gridspec

if __name__=='__main__':

    emo1 = [-0.3, 0.1, 0.56, 0.0, -0.17, -0.21, -0.12, 0.0, 0.0, 0.0, 0.0, 0.3, 0.17]
    emo2 = [0.0, -0.1, 0.0, 0.46, 0.0, -0.03, -0.2, -0.5, 0.3, 0.0, -0.09, 0.0, 0.0]
    emo3 = [-0.07, -0.1, 0.0, 0.0, 0.3, -0.3, -0.3, -0.17, 0.21, 0.3, 0.15, 0.25, 0.17]
    emo4 = [-0.46, -0.1, -0.25, -0.56, -0.07, 0.3, -0.5, -0.17, -0.09, 0.0, -0.09, -0.25, 0.0]
    emo5 = [-0.46, -0.3, -0.25, -0.4, 0.0, -0.39, -0.5, -0.33, -0.12, -0.56, -0.15, -0.58, -0.13]
    emo6 = [0.0, 0.0, 0.0, -0.4, 0.0, 0.0, 0.0, 0.0, -0.03, 0.0, 0.0, 0.0, 0.0]
    emo7 = [-0.07, -0.1, 0.0, 0.17, -0.39, -0.09, 0.46, -0.5, -0.12, -0.56, -0.09, 0.3, -0.56]
    emo8 = [0.07, 0.0, -0.25, -0.27, -0.09, 0.21, 0.17, 0.13, 0.33, 0.13, -0.15, -0.25, 0.03]
    
    emo11 = [-0.33,-0.33,0,0,-0.33,0,0,0,0,0,0,0.33,-0.33]
    emo22 = [0,-0.33,0,-0.66,0,-0.33,-0.66,-1,-0.33,0,-0.33,0,0]
    emo33 = [0.33,-0.33,0,0,0.33,-0.33,-0.33,-0.33,0,-0.33,0.66,0.33,0.33]

    def aveEmo(emo):
        return float('{:.4f}'.format(np.mean(emo)))
    def varEmo(emo):
        return float('{:.4f}'.format(np.var(emo)))

    stuA = emo11
    stuB = emo22
    stuC = emo33
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
    plt.plot(x, stuA, 'ko-.', label='A')
    #plt.plot(x, emo3, color='red')
    plt.plot(x, stuB, 'k*:', label='B')
    #plt.plot(x, emo4,  color='blue')
    plt.plot(x, stuC, 'kd--', label='C')
    plt.legend() # 显示图例
    #plt.plot(x,y)
    plt.xlabel("week")#X轴标签
    plt.ylabel("emoValue")#Y轴标签 
    plt.show()  
    