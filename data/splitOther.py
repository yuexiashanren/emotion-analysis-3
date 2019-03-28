import re

#获取需要切割的文本
def loadWords():   
    words = [line.strip()  for line in open('./0321.txt', 'r', encoding='utf-8').readlines() ]   
    #print("type(loadStopWords_stop)",type(stop))
    return words
f_1  = open('./0326.txt','w',encoding='utf-8')
if __name__ == '__main__':
	word = loadWords()
	word_1 = re.split('[、|,|，|\'|\"|\[|\]|\s]',str(word))
	#word_1 = re.split(r'[、,，\'\"\[\]\s]',str(word))
	#word_1 = re.split(r'(?:、|,|，|\'|\"|\[|\]|\s)',str(word))
	#print(word_1)
	for i in word_1:
		if i.strip() != '':
			f_1.write(i)
			f_1.write('\n')
	#print(str(word.split(',')))
'''
line = 'asdf fjdk; afed, fjek,asdf, foo'
#value = re.split(r'(?:,|;|\s)\s*', line)
#正则匹配，\s表示空格
print(re.split(r'[;,\s]\s*', line))
print(re.split(r'(;|,|\s)\s*', line))
print(re.split(r'(?:,|;|\s)\s*', line))
#print('.'.join(value))
'''