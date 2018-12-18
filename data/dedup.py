#词典返回list
def loadEmotWords():     
    emot = [line.strip()  for line in open('./emotions.txt', 'r', encoding='utf-8').readlines() ]   
    return emot
def loadIntroWords():     
    intro = [line.strip()  for line in open('./introductions.txt', 'r', encoding='utf-8').readlines() ]   
    return intro
if __name__=='__main__':
	#情感词典去重
	need_1 = loadEmotWords()
	f_1 = open('./emotions_.txt','w',encoding='utf-8')
	#set()去重，并按原顺序打印
	re_1 = sorted(set(need_1),key=need_1.index)
	for i in range(0,len(re_1)):
		f_1.write(str(re_1[i]))
		f_1.write('\n')
	f_1.close()
	#专业领域词典去重
	need_2 = loadIntroWords()
	f_2 = open('./introductions_.txt','w',encoding='utf-8')
	re_2 = sorted(set(need_2),key=need_2.index)
	for i in range(0,len(re_2)):
		f_2.write(str(re_2[i]))
		f_2.write('\n')
	f_2.close()