#! /bin/env python
# -*- coding: utf-8 -*-
"""
综合所有维度的情感分析
"""
import jieba
import numpy as np
from gensim.models.word2vec import Word2Vec
from gensim.corpora.dictionary import Dictionary
from keras.preprocessing import sequence

import yaml
from keras.models import model_from_yaml
np.random.seed(1337)  # For Reproducibility
import sys
sys.setrecursionlimit(1000000)

jieba.load_userdict('../../data/introductions.txt')
jieba.load_userdict('../../data/emotions.txt')
jieba.load_userdict('../knowledge_content/units/unit1.txt')
jieba.load_userdict('../knowledge_content/units/unit2.txt')
jieba.load_userdict('../knowledge_content/units/unit3.txt')
jieba.load_userdict('../knowledge_content/units/unit4.txt')
jieba.load_userdict('../knowledge_content/units/unit5.txt')
jieba.load_userdict('../knowledge_content/units/unit6.txt')
jieba.load_userdict('../knowledge_content/units/unit7.txt')

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.gridspec as gridspec

# 定义参数
maxlen = 100

def create_dictionaries(model=None,
                        combined=None):
    ''' Function does are number of Jobs:
        1-创建索引映射的单词
        2-创建一个单词到矢量映射
        3-转换训练和测试词典
    '''
    if (combined is not None) and (model is not None):
        gensim_dict = Dictionary()
        gensim_dict.doc2bow(model.wv.vocab.keys(),
                            allow_update=True)
        #  freqxiao10->0 所以k+1
        w2indx = {v: k+1 for k, v in gensim_dict.items()}#所有频数超过10的词语的索引,(k->v)=>(v->k)
        w2vec = {word: model[word] for word in w2indx.keys()}#所有频数超过10的词语的词向量, (word->model(word))

        def parse_dataset(combined): # 闭包-->临时使用
            ''' Words become integers
            '''
            data=[]
            for sentence in combined:
                new_txt = []
                for word in sentence:
                    try:
                        new_txt.append(w2indx[word])
                    except:
                        new_txt.append(0) # freqxiao10->0
                data.append(new_txt)
            return data # word=>index
        combined=parse_dataset(combined)
        combined= sequence.pad_sequences(combined, maxlen=maxlen)#每个句子所含词语对应的索引，所以句子中含有频数小于10的词语，索引为0
        return w2indx, w2vec,combined
    else:
        print ('没有提供数据...')

def loadStopWords():   
    
    stop = [line.strip()  for line in open('../../data/stopWords.txt', 'r', encoding='utf-8').readlines() ]   
    #print("type(loadStopWords_stop)",type(stop))
    return stop  

def input_transform(string):
    words=jieba.lcut(string)
    stopWords = loadStopWords()
    leftWords = []
    for i in words:
        if(i not in stopWords):
            leftWords.append(i)
    text_str = leftWords
    #print("text_str",text_str)
    
    words=np.array(text_str).reshape(1,-1)
    #载入模型
    model=Word2Vec.load('../../lstm_test/model/Word2vec_model.pkl')
    _,_,combined=create_dictionaries(model,words)
    return combined

def lstm_predict(string,week):
    #print ('loading model...')
    with open('../../lstm_test/model/lstm.yml', 'r') as f:
        yaml_string = yaml.load(f)
    model = model_from_yaml(yaml_string)

    #print ('loading weights...')
    model.load_weights('../../lstm_test/model/lstm.h5')
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',metrics=['accuracy'])

    neg = 0
    neu = 0
    pos = 0
    sum = 0
    with open(string ,'r', encoding='utf-8') as ff:
        for line in ff.readlines():
            data=input_transform(line)
            data.reshape(1,-1)
            #print data
            result=model.predict_classes(data)
            choose = result[0]
            #print(sum+1,choose)
            if choose==1:
                pos += 1
                sum += 1
            elif choose==0:
                neu += 1
                sum += 1
            else:
                neg += 1
                sum += 1
    print("第",week,"周：")
    print("sum",sum)
    print("negative:",neg)
    print("neural",neu)
    print("positive",pos)
    if sum == 0:
        print('negative/sum: {:.2%}'.format(0))
        print('neural/sum: {:.2%}'.format(0))
        print('positive/sum: {:.2%}'.format(0))
        return '{:.2f}'.format(0),'{:.2f}'.format(0),'{:.2f}'.format(0)
    else:
        print('negative/sum: {:.2%}'.format(neg/sum))
        print('neural/sum: {:.2%}'.format(neu/sum))
        print('positive/sum: {:.2%}'.format(pos/sum))
        return '{:.2f}'.format(neg/sum),'{:.2f}'.format(neu/sum),'{:.2f}'.format(pos/sum)

if __name__=='__main__':
    neg = [ 0 for i in range(13)]
    neu = [ 0 for i in range(13)]
    pos = [ 0 for i in range(13)]
    acc = [0.8, 0.68, 0.71, 0.69, 0.84, 0.86, 0.79, 0.88, 0.9, 0.76, 0.87, 0.71, 0.76]
    for i in range(1,14):
        if(i<10):
            route = '../weeks/0'+str(i)+'.txt'
        else:
            route = '../weeks/'+str(i)+'.txt'
        result = lstm_predict(route,i)
        neg[i-1] = float(result[0])
        neu[i-1] = float(result[1])
        pos[i-1] = float(result[2])
    
    print("negative",neg)
    print("neural",neu)
    print("positive",pos)  
    '''
    negative [0.23, 0.24, 0.27, 0.25, 0.19, 0.26, 0.23, 0.16, 0.18, 0.24, 0.28, 0.24, 0.22]
    neural [0.72, 0.71, 0.66, 0.69, 0.76, 0.67, 0.72, 0.78, 0.76, 0.7, 0.67, 0.66, 0.69]
    positive [0.06, 0.05, 0.08, 0.06, 0.05, 0.07, 0.05, 0.06, 0.06, 0.07, 0.04, 0.1, 0.08]
    '''
    #设置x,y轴
    x = [x for x in range(1,14)]
    xx = [xx for xx in range(0,13)]
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
    ax2.plot(x, neu, color='blue')
    ax2.set_title('neural')
    ax3.plot(x, pos, color='green')
    ax3.set_title('positive')
    plt.xlabel("week")#X轴标签
    plt.ylabel("percent")#Y轴标签
    plt.show()
    #绘制整体柱状图
    addPG = [addPG for addPG in range(len(pos))]
    for i in range(len(pos)):
        addPG[i] = float('{:.2f}'.format(pos[i]+neu[i]))

    plt.title('Result Analysis')
    #range()=>x, pos=>y, bottom=>柱形y轴坐标（柱形堆叠时的起始y轴位置）, tick_label=>刻度线
    plt.bar(range(len(pos)), pos, label='positive',fc = 'green')
    plt.bar(range(len(pos)), neu, bottom=pos, label='neural',fc = 'blue')
    plt.bar(range(len(pos)), neg, bottom=addPG, label='negative',tick_label = x, fc = 'red')
    plt.plot(xx, acc, color='yellow', label='accuracy')
    plt.plot(xx, acc, 'go')
    plt.legend()
    plt.xlabel("week")#X轴标签
    plt.ylabel("percent")#Y轴标签 
    plt.show() 
