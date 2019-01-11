#! /bin/env python
# -*- coding: utf-8 -*-
"""
课后作业13周内的情感分析
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
    for i in range(1,14):
        if(i<10):
            route = './weeks/0'+str(i)+'.txt'
        else:
            route = './weeks/'+str(i)+'.txt'
        result = lstm_predict(route,i)
        neg[i-1] = result[0]
        neu[i-1] = result[1]
        pos[i-1] = result[2]
    
    print("negative",neg)
    print("neural",neu)
    print("positive",pos)  

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
    ax2.plot(x, neu, color='blue')
    ax2.set_title('neural')
    ax3.plot(x, pos, color='green')
    ax3.set_title('positive')
    plt.xlabel("week")#X轴标签
    plt.ylabel("percent")#Y轴标签 
    plt.show()

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
    