#! /bin/env python
# -*- coding: utf-8 -*-
"""
训练网络，并保存模型，其中LSTM的实现采用Python中的keras库
"""
import pandas as pd 
import numpy as np 
import jieba
import multiprocessing
import keras

from gensim.models.word2vec import Word2Vec
from gensim.corpora.dictionary import Dictionary
from keras.preprocessing import sequence

from sklearn.cross_validation import train_test_split
from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM, GRU
from keras.layers.core import Dense, Dropout,Activation
from keras.models import model_from_yaml

from keras.layers import SimpleRNN

np.random.seed(1337)  # For Reproducibility
import sys
sys.setrecursionlimit(1000000)
import yaml
#jieba中添加专业词典
jieba.load_userdict('introduction.txt') 
# 设置参数
cpu_count = multiprocessing.cpu_count() # 4
vocab_dim = 100 #向量维度
n_iterations = 5  # 理想情况更多..
n_exposures = 5 # 所有频数超过10的词语
window_size = 7
n_epoch = 6
input_length = 100
maxlen = 100 #文本保留的最大长度

batch_size = 32


def loadfile():
    neg=pd.read_csv('../data/neg.csv',header=None,index_col=None,error_bad_lines=False)
    pos=pd.read_csv('../data/pos.csv',header=None,index_col=None,error_bad_lines=False)
    neu=pd.read_csv('../data/neu.csv', header=None, index_col=None,error_bad_lines=False)

    #数组拼接
    combined = np.concatenate((pos[0], neu[0], neg[0]))
    #标签拼接
    y = np.concatenate((np.ones(len(pos), dtype=int), np.zeros(len(neu), dtype=int), 
                        -1*np.ones(len(neg),dtype=int)))
    #返回所有数据及对应标签
    return combined,y

#获取停用词
def loadStopWords():   
    
    stop = [line.strip()  for line in open('../data/stopWords.txt', 'r', encoding='utf-8').readlines() ]   
    #print("type(loadStopWords_stop)",type(stop))
    return stop  

#对句子经行分词，并去掉换行符
def cutWords(text):
    
    #分词
    text = [jieba.lcut(document.replace('\n', '')) for document in text]
    #读取分词后的数据，去除停用词后写入文本
    f_o = open('../data/cutWords.txt', 'w', encoding='utf-8')
    stopWords = loadStopWords()
    for line in text: 
        leftWords = []   
        for i in line:  
            if (i not in stopWords):  
                leftWords.append(i)
        text_str = ' '.join(leftWords)
        f_o.write(text_str)
        f_o.write('\n')
    f_o.close()
    return text
    '''
    with open('../data/cutWords.txt','r',encoding='utf-8') as text_list:
        return list(text_list)
    '''
#创建词语字典，并返回每个词语的索引，词向量，以及每个句子所对应的词语索引
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
            ''' 单词变集合
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
        #返回每个词语的索引（从1开始编号）、词向量、每个句子所对应的词语索引
        '''
        f_3 = open('./data/create_dictionaries_w2indx.txt', 'w', encoding='utf-8')
        for word,index in w2indx.items():   
            f_3.write(str(word))
            f_3.write(' : ')
            f_3.write(str(index))
            f_3.write('\n')
        f_3.close()
        f_4 = open('./data/create_dictionaries_w2vec.txt', 'w', encoding='utf-8')
        for word,index in w2vec.items():   
            f_4.write(str(word))
            f_4.write(' : ')
            f_4.write(str(index))
            f_4.write('\n')
        f_4.close()
        f_5 = open('./data/create_dictionaries_combined.txt', 'w', encoding='utf-8')
        for line in combined:   
            f_5.write(str(line))
            f_5.write('\n')
        f_5.close()
        '''
        return w2indx, w2vec,combined
    else:
        print ('没有提供数据...')


#词向量训练
def word2vec_train(combined):

    model = Word2Vec(size=vocab_dim, #特征向量的维度，默认100，大的size需要更多数据
                     min_count=n_exposures, #最小词频，小于该次数的单词被丢弃，默认5
                     window=window_size, #当前词与预测词在一个句子中的最大距离
                     workers=cpu_count, #参数训练的并行数
                     iter=n_iterations) #迭代次数，默认5
    #录入列表
    model.build_vocab(combined) # input: list
    #模型训练
    model.train(combined,total_examples=model.corpus_count,epochs=model.iter)
    #模型保存（语料的索引及词向量）
    model.save('../model/Word2vec_model.pkl')
    #每个词语的索引字典{单词：索引数字}##21088##、
    #词向量字典{单词：词向量（100维长的数组）}##21088##、
    #每个句子所对应的向量100维##总数据=21088*100##
    index_dict, word_vectors,combined = create_dictionaries(model=model,combined=combined)

    return   index_dict, word_vectors,combined


def get_data(index_dict,word_vectors,combined,y):
    #获取句子向量
    n_symbols = len(index_dict) + 1  # 所有单词的索引数，频数小于10的词语索引为0，所以加1=8305
    embedding_weights = np.zeros((n_symbols, vocab_dim)) # n_symbols*100的0矩阵
    for word, index in index_dict.items(): # 从索引为1的词语开始，用词向量填充矩阵
        embedding_weights[index, :] = word_vectors[word] #词向量矩阵，第一行是0向量
    #随机抽取20%的测试集，x_test=20%，combined-样本特征集，y-样本标签，test_size-样本占比，都是列表
    x_train, x_test, y_train, y_test = train_test_split(combined, y, test_size=0.2)
    #多分类标签生成
    y_train = keras.utils.to_categorical(y_train,num_classes=3) 
    y_test = keras.utils.to_categorical(y_test,num_classes=3)

    #字典长度##8305##、权重##字典中每个词1*100##、
    #训练样本##16870*100##、训练样本标签##16870*3##、测试样本##4218*100##、测试样本标签##4218*3##
    
    return n_symbols,embedding_weights,x_train,y_train,x_test,y_test


##定义网络结构,参数为get_data返回值
def train_lstm(n_symbols,embedding_weights,x_train,y_train,x_test,y_test):
    print ('定义一个简单的keras模型...')
    #定义基本网络结构（输入维度100，输出维度3）
    model = Sequential()  # or Graph or whatever
#    #添加嵌入层，只能作为第一层，将输入转化为向量
    model.add(Embedding(output_dim=vocab_dim, #大于0的整数，代表全连接嵌入的维度
                        input_dim=n_symbols, #大或等于0的整数，字典长度，即输入数据最大下标+1 
                        mask_zero=True, #布尔值，确定是否将输入中的‘0’看作是应该被忽略的‘填充’（padding）值，该参数在使用递归层处理变长输入时有用。
                        weights=[embedding_weights], #初始化权值的numpy arrays组成的list
                        input_length=input_length))  # 输入序列的长度
    #添加LSTM层,内部投影的维数和最终输出的维数为50，激活函数tanh
    model.add(LSTM(units=50, activation='tanh')) 
    #添加GRU层
    '''
    model.add(GRU(units=50,
                  activation='tanh',
                  unroll=True,
                  ))
    '''
    #添加RNN层
#    model.add(SimpleRNN(units=50,
#                  activation='tanh',
#                  unroll=True,
#                  ))

    #采用50%的dropout,模型训练时随机让网络某些隐含层节点50%的权重不工作，避免过拟合（训练和测试数据的结果差别大）
    model.add(Dropout(0.5))
    #Dense=>全连接层,输出维度=3（三分类，输出维度为3，sigmoid）
    model.add(Dense(3)) 
    #最后一层用激活函数softmax
    model.add(Activation('softmax'))
    #二分类与多分类在前面的结构上都没有问题，就是需要改一下最后的全连接层，
    #因为此时有3分类，所以需要Dense(3)，同时激活函数是softmax，如果是二分类就是dense(2)+sigmoid(激活函数)

    print ('编译模型...')
    #loss-目标函数（categorical_crossentropy-多分类，binary_crossentropy-二分类）
    #optimizer-指定模型训练的优化器
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',metrics=['accuracy'])

    print ("训练...") # batch_size=32
    #用于训练一个固定迭代次数的模型
    #x_train-训练数据，y_train-标签，batch_size-每次训练和梯度更新块的大小,epochs-迭代次数
    #verbose-进度表示方式，0=不显示，1=显示进度条，2=只显示一个数据
    model.fit(x_train, y_train, batch_size=batch_size, epochs=n_epoch,verbose=1)

    print ("评估...")
    #展示模型在验证数据上的效果
    #x_test-训练数据,y_test-标签,batch_size-更新块大小
    score, acc = model.evaluate(x_test, y_test,
                                batch_size=batch_size)
    #以YAML字符串的形式返回模型，不包括权重，只包括结构
    yaml_string = model.to_yaml()
    with open('../model/lstm.yml', 'w') as outfile:
        outfile.write( yaml.dump(yaml_string, default_flow_style=True) )
    #将所有层的权值保存为HDF5文件
    model.save_weights('../model/lstm.h5')
    print ('Test score:', score)
    print ('Test accuracy:', acc)


#训练模型，并保存
print ('加载数据...')
combined,y=loadfile()
'''
print("type(loadfile_combined)",type(combined))
print("len(loadfile_combined)",combined.shape)
print("type(loadfile_y)",type(y))
print("len(loadfile_y)",y.shape)
f_0 = open('./data/loadfile_combined.txt', 'w', encoding='utf-8')
for line in combined:   
    f_0.write(str(line))
    f_0.write('\n')
f_0.close()
f_1 = open('./data/loadfile_y.txt', 'w', encoding='utf-8')
for line in y:   
    f_1.write(str(line))
    f_1.write('\n')
f_1.close()
'''
print ("数据集：",len(combined),"，数据集标签：",len(y))

print ('分词...')
combined = cutWords(combined)
'''
print("type(cutWord_combined)",type(combined))
print("len(cutWord_combined)",len(combined))
f_15 = open('./data/cutWords_combined.txt', 'w', encoding='utf-8')
for line in combined:   
    f_15.write(str(line))
    f_15.write('\n')
f_15.close()
'''
print ('训练Word2vec模型...')
index_dict, word_vectors,combined=word2vec_train(combined)
'''
print("type(word2vec_train_index_dict)",type(index_dict))
print("len(word2vec_train_index_dict)",len(index_dict))
print("type(word2vec_train_word_vectors)",type(word_vectors))
print("len(word2vec_train_word_vectors)",len(word_vectors))
print("type(word2vec_train_combined)",type(combined))
print("len(word2vec_train_combined)",combined.shape)
f_6 = open('./data/word2vec_train_index_dict.txt', 'w', encoding='utf-8')
for word,index in index_dict.items():   
    f_6.write(str(word))
    f_6.write(' : ')
    f_6.write(str(index))
    f_6.write('\n')
f_6.close()
f_7 = open('./data/word2vec_train_word_vectors.txt', 'w', encoding='utf-8')
for word,index in word_vectors.items():   
    f_7.write(str(word))
    f_7.write(' : ')
    f_7.write(str(index))
    f_7.write('\n')
f_7.close()
f_8 = open('./data/word2vec_train_combined.txt', 'w', encoding='utf-8')
for line in combined:   
    f_8.write(str(line))
    f_8.write('\n')
f_8.close()
'''
print ('获取网络参数...')
n_symbols,embedding_weights,x_train,y_train,x_test,y_test=get_data(index_dict, word_vectors,combined,y)
'''
print("type(get_data_n_symbols)",type(n_symbols))

print("type(get_data_embedding_weights)",type(embedding_weights))
print("len(get_data_embedding_weights)",embedding_weights.shape)
print("type(get_data_x_train)",type(x_train))
print("len(get_data_x_train)",x_train.shape)
print("type(get_data_y_train)",type(y_train))
print("len(get_data_y_train)",y_train.shape)
f_9 = open('./data/get_data_n_symbols.txt', 'w', encoding='utf-8') 
f_9.write(str(n_symbols))
f_9.write('\n')
f_9.close()
f_10 = open('./data/get_data_embedding_weights.txt', 'w', encoding='utf-8')
for line in embedding_weights:   
    f_10.write(str(line))
    f_10.write('\n')
f_10.close()
f_11 = open('./data/get_data_x_train.txt', 'w', encoding='utf-8')
for line in x_train:   
    f_11.write(str(line))
    f_11.write('\n')
f_11.close()
f_12 = open('./data/get_data_y_train.txt', 'w', encoding='utf-8')
for line in y_train:   
    f_12.write(str(line))
    f_12.write('\n')
f_12.close()
f_13 = open('./data/get_data_x_test.txt', 'w', encoding='utf-8')
for line in x_test:   
    f_13.write(str(line))
    f_13.write('\n')
f_13.close()
f_14 = open('./data/get_data_y_test.txt', 'w', encoding='utf-8')
for line in y_test:   
    f_14.write(str(line))
    f_14.write('\n')
f_14.close()
'''
print ("训练集：",x_train.shape,"，训练集标签：",y_train.shape)
print ("测试集：",x_test.shape,"，测试集标签：",y_test.shape)
train_lstm(n_symbols,embedding_weights,x_train,y_train,x_test,y_test)