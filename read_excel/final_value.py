#! /bin/env python
# -*- coding: utf-8 -*-
"""
oneStudent/oneStu_allWeek.txt中文本的最终情感值
即输出某个同学整个学习过程的最终情感值
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

jieba.load_userdict('../data/introductions.txt')
jieba.load_userdict('../data/emotions.txt')
jieba.load_userdict('../experiment/knowledge_content/units/unit1.txt')
jieba.load_userdict('../experiment/knowledge_content/units/unit2.txt')
jieba.load_userdict('../experiment/knowledge_content/units/unit3.txt')
jieba.load_userdict('../experiment/knowledge_content/units/unit4.txt')
jieba.load_userdict('../experiment/knowledge_content/units/unit5.txt')
jieba.load_userdict('../experiment/knowledge_content/units/unit6.txt')
jieba.load_userdict('../experiment/knowledge_content/units/unit7.txt')

# 定义参数
maxlen = 100

def create_dictionaries(model=None, combined=None):
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
    stop = [line.strip()  for line in open('../data/stopWords.txt', 'r', encoding='utf-8').readlines() ]   
    return stop  

def input_transform(string):
    words=jieba.lcut(string)
    
    stopWords = loadStopWords()
    leftWords = []
    for i in words:
        if(i not in stopWords):
            leftWords.append(i)
    text_str = leftWords

    words=np.array(text_str).reshape(1,-1)
    #载入模型
    model=Word2Vec.load('../lstm_test/model/Word2vec_model.pkl')
    _,_,combined=create_dictionaries(model,words)
    return combined

#weekValue = [ 0 for i in range(40)]
weekValue = [ [0]*3 for i in range(13)]
def lstm_predict(string):
    with open('../lstm_test/model/lstm.yml', 'r') as f:
        yaml_string = yaml.load(f)
    model = model_from_yaml(yaml_string)
    model.load_weights('../lstm_test/model/lstm.h5')
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',metrics=['accuracy'])

    neg = 0
    neu = 0
    pos = 0
    now = 0
    with open(string ,'r', encoding='utf-8') as ff:
        for line in ff.readlines():
            a = now//3#取整
            b = now%3#取余
            data=input_transform(line)
            data.reshape(1,-1)
            #print data
            result=model.predict_classes(data)
            choose = result[0]
            print(now+1,choose)
            if choose==1:
                pos += 1
                weekValue[a][b] = 1
                now += 1
            elif choose==0:
                neu += 1
                weekValue[a][b] = 0
                now += 1
            else:
                neg += 1
                weekValue[a][b] = -1
                now += 1
    print("now",now)
    print("negative:",neg)
    print("neural",neu)
    print("positive",pos)
    #print("weekValue",weekValue)
    return weekValue

if __name__=='__main__':
    string = './oneStudent/oneStu_allWeek.txt'
    #获取周情感值
    weekValue = lstm_predict(string)
    #课前、课后、每周总结权重赋值
    weight = [0.2,0.5,0.3]
    #难度标记
    dif = [[2,2],[3,2],[3,3],[3,2],[2,1],[1,1],
            [1,2],[1,2],[1,1],[3,2],[2,1],[1,3],[3,2]]
    #定义难度权值
    difWeight = [0.17,0.33,0.5]
    def changeDif(dif,difWeight):
        for i in range(len(dif)):
            for j in range(len(dif[0])):
                if dif[i][j] == 1:
                    dif[i][j] = difWeight[0]
                elif dif[i][j] == 2:
                    dif[i][j] = difWeight[1]
                else:
                    dif[i][j] = difWeight[2]
    #难度标记数组=》难度权重数组
    changeDif(dif,difWeight)
    print("weekValue:",weekValue)
    #最终情感值=课前*权重*难度+课后*权重*难度+每周*权重
    def returnValue(weekValue,weight,dif):
        emoValue = [ 0 for i in range(13)]
        for i in range(13):
            emoValue[i] = float('{:.2f}'.format(weekValue[i][0]*weight[0]*dif[i][0]+weekValue[i][1]*weight[1]*dif[i][1]+weekValue[i][2]*weight[2]))
        return emoValue
    emoValue = returnValue(weekValue,weight,dif)
    finValue = [ 0 for i in range(13)]
    for i in range(len(emoValue)):
        if i == 0:
            finValue[i] = float('{:.4f}'.format(emoValue[i]))
        else:
            finValue[i] = float('{:.4f}'.format(0.2*emoValue[i-1] + 0.8*emoValue[i]))
    print("emoValue:",emoValue)
    print("finValue:",finValue)
