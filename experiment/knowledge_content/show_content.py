#! /bin/env python
# -*- coding: utf-8 -*-
"""
符合每个章节知识点的情感分析
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
jieba.load_userdict('./units/unit1.txt')
jieba.load_userdict('./units/unit2.txt')
jieba.load_userdict('./units/unit3.txt')
jieba.load_userdict('./units/unit4.txt')
jieba.load_userdict('./units/unit5.txt')
jieba.load_userdict('./units/unit6.txt')
jieba.load_userdict('./units/unit7.txt')

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

def unit1Datas():   
    unit_data = [line.strip()  for line in open('./units/unit1.txt', 'r', encoding='utf-8').readlines() ]   
    #print("type(loadStopWords_stop)",type(stop))
    return unit_data

def unit2Datas():   
    unit_data = [line.strip()  for line in open('./units/unit2.txt', 'r', encoding='utf-8').readlines() ]   
    #print("type(loadStopWords_stop)",type(stop))
    return unit_data

def unit3Datas():   
    unit_data = [line.strip()  for line in open('./units/unit3.txt', 'r', encoding='utf-8').readlines() ]   
    #print("type(loadStopWords_stop)",type(stop))
    return unit_data

def unit4Datas():   
    unit_data = [line.strip()  for line in open('./units/unit4.txt', 'r', encoding='utf-8').readlines() ]   
    #print("type(loadStopWords_stop)",type(stop))
    return unit_data

def unit5Datas():   
    unit_data = [line.strip()  for line in open('./units/unit5.txt', 'r', encoding='utf-8').readlines() ]   
    #print("type(loadStopWords_stop)",type(stop))
    return unit_data

def unit6Datas():   
    unit_data = [line.strip()  for line in open('./units/unit6.txt', 'r', encoding='utf-8').readlines() ]   
    #print("type(loadStopWords_stop)",type(stop))
    return unit_data

def unit7Datas():   
    unit_data = [line.strip()  for line in open('./units/unit7.txt', 'r', encoding='utf-8').readlines() ]   
    #print("type(loadStopWords_stop)",type(stop))
    return unit_data
f3 = open('./need_test.txt','w',encoding='utf-8')
#string表示初始的单个文本数据，unitDatas表示需要引入的第几单元的词典
def input_transform(string,unitDatas):
    words=jieba.lcut(string)
    stopWords = loadStopWords()
    leftWords = []
    for i in words:
        if(i not in stopWords):
            leftWords.append(i)
    text_str = leftWords
    #print("text_str",text_str)
    
    #筛选符合章节信息的数据
    flag = "false"
    #引入单元词典，匹配符合该单元词典的数据
    unit1s = unitDatas
    for i in words:
        if i in unit1s:
            flag = "true"
            f3.write(str(words))
            f3.write('\n')
            break

    if flag == "true":
        words=np.array(text_str).reshape(1,-1)
        #载入模型
        model=Word2Vec.load('../../lstm_test/model/Word2vec_model.pkl')
        _,_,combined=create_dictionaries(model,words)
        return combined
    else:
        return "none"

f1 = open('./text_str.txt','w',encoding='utf-8')
f2 = open('./result_test.txt','w',encoding='utf-8')
def lstm_predict(string,unit,unitDatas):
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
            #line表示输入的单个文本数据，unitDatas表示需要引入的单元词典
            data = input_transform(line,unitDatas)
            if data != "none":
                f1.write(str(line))
                f2.write(str(data))
                f2.write('\n')
                data.reshape(1,-1)
                #print data
                result = model.predict_classes(data)
                choose = result[0]
                #print(sum+1,choose)
                if choose == 1:
                    pos += 1
                    sum += 1
                elif choose == 0:
                    neu += 1
                    sum += 1
                else:
                    neg += 1
                    sum += 1

    print("单元",unit)
    print("sum",sum)
    print("negative:",neg)
    print("neural",neu)
    print("positive",pos)
    if sum == 0:
        print('negative/sum: {:.2%}'.format(0))
        print('neural/sum: {:.2%}'.format(0))
        print('positive/sum: {:.2%}'.format(0))
    else:
        print('negative/sum: {:.2%}'.format(neg/sum))
        print('neural/sum: {:.2%}'.format(neu/sum))
        print('positive/sum: {:.2%}'.format(pos/sum))
    '''
    #区域标签
    labels = 'neg','neu','pos'
    #区域大小
    sizes = neg/sum, neu/sum, pos/sum
    #区域颜色
    colors = 'red', 'blue', 'green'
    #区域缝隙
    explode=0.1,0.08,0.12
    #autopct，圆里面的文本格式，%1.2f%%表示小数有2位
    #startangle，起始角度，表示从0开始逆时针转
    #shadow，True表示有一定的阴影,False表示没有阴影
    plt.pie(sizes,explode=explode,labels=labels,
            colors=colors,autopct='%1.2f%%',shadow=True,startangle=90)
    #保证饼状图是正圆，否则会有一点角度偏斜
    plt.axis('equal')
    plt.show()
    '''

if __name__=='__main__':
    #输入的数据源
    route = './input_test.txt'
    for i in range(1,8):
        unit = [unit1Datas(), unit2Datas(), unit3Datas(), unit4Datas(), unit5Datas(), unit6Datas(), unit7Datas()]
        #route表示输入文本路径，i表示第几章节，unit[]表示需要的第几章节的词典
        result = lstm_predict(route,i,unit[i-1])
    