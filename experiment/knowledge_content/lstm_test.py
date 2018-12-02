#! /bin/env python
# -*- coding: utf-8 -*-
"""
知识点内容情感分析
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

def introductionWords():   
    introduction = [line.strip()  for line in open('../../data/introductions.txt', 'r', encoding='utf-8').readlines() ]   
    #print("type(loadStopWords_stop)",type(stop))
    return introduction  
f1 = open('./need_test.txt','w',encoding='utf-8')
f2 = open('./text_str.txt','w',encoding='utf-8')
f3 = open('./result_test.txt','w',encoding='utf-8')
def input_transform(string):
    words=jieba.lcut(string)
    #去除停用词
    stopWords = loadStopWords()
    leftWords = []
    for i in words:
        if(i not in stopWords):
            leftWords.append(i)
    text_str = leftWords
    #print("text_str",text_str)
    
    f2.write(str(text_str))
    f2.write('\n')

    #筛选符合知识点的数据
    flag = "false"
    introductions = introductionWords()
    for i in text_str:
        if i in introductions:
            flag = "true"
            f3.write(str(text_str))
            f3.write('\n')
            break
    if flag == "true":
        words=np.array(text_str).reshape(1,-1)
        f1.write(str(words))
        f1.write('\n')
        #载入模型
        model=Word2Vec.load('../../lstm_test/model/Word2vec_model.pkl')
        _,_,combined=create_dictionaries(model,words)
        return combined
    else:
        return "none"

def lstm_predict(string):
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
            if(data != "none"):
                data.reshape(1,-1)
                #print data
                result=model.predict_classes(data)
                choose = result[0]
                print(sum+1,choose)
                if choose==1:
                    pos += 1
                    sum += 1
                elif choose==0:
                    neu += 1
                    sum += 1
                else:
                    neg += 1
                    sum += 1
    print("sum",sum)
    print("negative:",neg)
    print("neural",neu)
    print("positive",pos)
    print('negative/sum: {:.2%}'.format(neg/sum))
    print('neural/sum: {:.2%}'.format(neu/sum))
    print('positive/sum: {:.2%}'.format(pos/sum))

if __name__=='__main__':
    
    string = './input_test.txt'
    lstm_predict(string)       
