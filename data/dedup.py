#词典返回list
def loadStopWords():     
    stop = [line.strip()  for line in open('./emotions_init.txt', 'r', encoding='utf-8').readlines() ]   
    return stop
	
if __name__=='__main__':
	need = loadStopWords()
	f1 = open('./emotions.txt','w',encoding='utf-8')
	#set()去重，并按原顺序打印
	re = sorted(set(need),key=need.index)
	for i in range(0,len(re)):
		f1.write(str(re[i]))
		f1.write('\n')
	f1.close()