1.加载数据
loadfile_combined.txt--数据集文本（numpy.ndarray (21088,)）
loadfile_y.txt--数据集标签文本（numpy.ndarray (21088,)）

2.分词（去除停用词）
cutWords_combined.txt--分词后的数据集文本（list 21088）

3.训练word2vec模型
word2vec_train_index_dict.txt--词语的索引字典文本{词语：索引数字}（dict 8304）
word2vec_train_word_vectors.txt--词向量的索引字典文本{词向量：索引数字}（dict 8304）
word2vec_train_combined.txt--21088个句子对应的句子向量，每个句子向量100维（numpy.ndarray (21088,100)）

create_dictionaries_w2indx.txt--词语的索引字典文本{词语：索引数字}（dict 8304）
create_dictionaries_w2vec.txt--词向量的索引字典文本{词向量：索引数字}（dict 8304）
create_dictionaries_combined.txt--21088个句子对应的句子向量，每个句子向量100维（numpy.ndarray (21088,100)）

4.获取网络参数
get_data_n_symbols.txt--字典长度8305（int）
get_data_embedding_weights.txt--8305个词的权重，每个词的权重向量100维（numpy.ndarray (8305,100)）
get_data_x_train.txt--16870个训练样本向量，每个样本向量100（numpy.ndarray,(16870,100)）
get_data_y_train.txt--16870个训练样本标签向量，每个样本标签向量3（numpy.ndarray,(16870,3)）
get_data_x_test.txt--4218个测试样本向量，每个样本向量100（numpy.ndarray,(4218,100)）
get_data_y_test.txt--4218个测试样本标签向量，每个样本标签向量3（numpy.ndarray,(4218,3)）

5.模型训练