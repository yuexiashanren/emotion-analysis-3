import jieba
jieba.add_word("对..感兴趣")
str = "非常对计算机导论感兴趣的，还不错！"
print(jieba.lcut(str))