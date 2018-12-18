#词典返回list
def loadUnit1Words():     
    info = [line.strip()  for line in open('./units/unit1.txt', 'r', encoding='utf-8').readlines() ]   
    return info
def loadUnit2Words():     
    info = [line.strip()  for line in open('./units/unit2.txt', 'r', encoding='utf-8').readlines() ]   
    return info
def loadUnit3Words():     
    info = [line.strip()  for line in open('./units/unit3.txt', 'r', encoding='utf-8').readlines() ]   
    return info
def loadUnit4Words():     
    info = [line.strip()  for line in open('./units/unit4.txt', 'r', encoding='utf-8').readlines() ]   
    return info
def loadUnit5Words():     
    info = [line.strip()  for line in open('./units/unit5.txt', 'r', encoding='utf-8').readlines() ]   
    return info
def loadUnit6Words():     
    info = [line.strip()  for line in open('./units/unit6.txt', 'r', encoding='utf-8').readlines() ]   
    return info
def loadUnit7Words():     
    info = [line.strip()  for line in open('./units/unit7.txt', 'r', encoding='utf-8').readlines() ]   
    return info
	
if __name__=='__main__':
	need_1 = loadUnit1Words()
	need_2 = loadUnit2Words()
	need_3 = loadUnit3Words()
	need_4 = loadUnit4Words()
	need_5 = loadUnit5Words()
	need_6 = loadUnit6Words()
	need_7 = loadUnit7Words()

	f_1 = open('./units/unit1_.txt','w',encoding='utf-8')
	f_2 = open('./units/unit2_.txt','w',encoding='utf-8')
	f_3 = open('./units/unit3_.txt','w',encoding='utf-8')
	f_4 = open('./units/unit4_.txt','w',encoding='utf-8')
	f_5 = open('./units/unit5_.txt','w',encoding='utf-8')
	f_6 = open('./units/unit6_.txt','w',encoding='utf-8')
	f_7 = open('./units/unit7_.txt','w',encoding='utf-8')
	#set()去重，并按原顺序打印
	re_1 = sorted(set(need_1),key=need_1.index)
	re_2 = sorted(set(need_2),key=need_2.index)
	re_3 = sorted(set(need_3),key=need_3.index)
	re_4 = sorted(set(need_4),key=need_4.index)
	re_5 = sorted(set(need_5),key=need_5.index)
	re_6 = sorted(set(need_6),key=need_6.index)
	re_7 = sorted(set(need_7),key=need_7.index)
	for i in range(0,len(re_1)):
		f_1.write(str(re_1[i]))
		f_1.write('\n')
	for i in range(0,len(re_2)):
		f_2.write(str(re_2[i]))
		f_2.write('\n')
	for i in range(0,len(re_3)):
		f_3.write(str(re_3[i]))
		f_3.write('\n')
	for i in range(0,len(re_4)):
		f_4.write(str(re_4[i]))
		f_4.write('\n')
	for i in range(0,len(re_5)):
		f_5.write(str(re_5[i]))
		f_5.write('\n')
	for i in range(0,len(re_6)):
		f_6.write(str(re_6[i]))
		f_6.write('\n')
	for i in range(0,len(re_7)):
		f_7.write(str(re_7[i]))
		f_7.write('\n')
	f_1.close()
	f_2.close()
	f_3.close()
	f_4.close()
	f_5.close()
	f_6.close()
	f_7.close()