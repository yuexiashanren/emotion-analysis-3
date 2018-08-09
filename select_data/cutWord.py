import jieba
#jieba.add_word("计算机导论")

stop = [line.strip()  for line in open('./input.txt', 'r', encoding='utf-8').readlines() ]
print("type(stop)",type(stop))
print(stop)
for a in stop:
	print("aa",a)
f_0 = open("./cutWord.txt","w",encoding="utf-8")
#保存符合知识点的评论数据
f_1 = open("./need.txt","w",encoding="utf-8")

text = open("./cutWord","r",encoding="utf-8")

for line in text.readlines():
	#分词
	line_str = jieba.lcut(line.replace('\n',''))
	text_str = ' '.join(line_str)
	f_0.write(text_str)
	f_0.write('\n')
	#匹配知识点，匹配成功数据写入need.txt
	j = 0
	for i in line_str:
		if(i in stop):
			j += 1
	if(j > 0):
		f_1.write(text_str)
		f_1.write('\n')
	
f_0.close()
f_1.close()


