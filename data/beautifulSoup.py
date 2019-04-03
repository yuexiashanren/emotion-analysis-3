from bs4 import BeautifulSoup 
from urllib.request import urlopen 
import re

url_1 = "https://blog.csdn.net/zhiyinyouni_pi/article/details/78837022"
url_2 = "https://blog.csdn.net/linaux_mctc/article/details/78970441"
url_3 = "https://blog.csdn.net/qq_26954773/article/details/53730064"
url_4 = "https://blog.csdn.net/peng_shakalaka/article/details/53165059"
url_5 = "https://blog.csdn.net/a1809032425/article/details/81268589"
#停用词
url_6 = "https://blog.csdn.net/shijiebei2009/article/details/39696571"
url_7 = "https://blog.csdn.net/unikran2018/article/details/79441188"
url_8 = "https://blog.csdn.net/icurious/article/details/78670504"
url_9 = "https://blog.csdn.net/akalius/article/details/83237167"
url_10 = "https://blog.csdn.net/u010533386/article/details/51458591"
url_11 = "https://blog.csdn.net/u012661010/article/details/70880847"
#获取网址
html = urlopen(url_11).read().decode('utf-8') 
#解析网址
soup = BeautifulSoup(html,"html.parser") 
#选择CSS
#titles=soup.select('.htmledit_views pre .language-python') # CSS 选择器 
#titles=soup.select('.htmledit_views') 
titles=soup.select('#content_views p') 
#根据已知属性值获取指定属性
#print(soup.find('a', attrs={'class',"follow-nickName"}).get_text())
f_1 = open('./0321.txt','w',encoding='utf-8')
i = 0
words = str(titles).split("<br/>")
print("words:",words)
print(type(words))
#print(titles.get_text())
for word in words: 
	#获取 li>h2的文本信息
	
	#获取文本信息，去掉左换行
	print(word.lstrip())
	if word.lstrip() >= u'\u4e00' and word.lstrip() <= u'\u9fa5':
		f_1.write(word)
	#f_1.write('\n')

	#.contents将子节点以列表的形式输出
	#tit = title.contents
	#print(tit[3].get_text())
	#f_1.write(tit[3].get_text())
	#f_1.write('\n')
	
	#text = title.get_text().split()
	#print(text[-1])
	#if len(text) > 0:
	#	print(text)
		
	#	for i in range(len(text)):
	#		if text[i] >= u'\u4e00' and text[i] <= u'\u9fa5':
	#			print(text[i])
	#			f_1.write(text[i])
	#			f_1.write(' ')
	#	f_1.write('\n')
	#	print('\n')
	
