#词典返回list
def loadEmotWords():     
    emot = [line.strip()  for line in open('./newEmo.txt', 'r', encoding='utf-8').readlines() ]   
    return emot

if __name__=='__main__':
	
	#专业领域词典去重
	newEmo = loadEmotWords()
	f_1 = open('./0321.txt','w',encoding='utf-8')
	re_2 = sorted(set(newEmo),key=newEmo.index)
	print("newEmo:",newEmo[0])
	#for i in len(newEmo):
	print(len(newEmo))
	for i in range(len(newEmo)):
		word  =newEmo[i]
		#通过索引切割
		num = word.index(' ')
		#print(word[:num])
		newWord = word[:num]
		print(newWord[0])
		if newWord[0] != '5':
			f_1.write(newWord)
			f_1.write('\n')
		'''
		#通过空格切割
		newWord = word.split()
		print(newWord[0])
		f_1.write(newWord[0])
		f_1.write('\n')
		'''
	
