from bs4 import BeautifulSoup 
from urllib.request import urlopen 
import re

url_1 = "https://blog.csdn.net/zhiyinyouni_pi/article/details/78837022"
url_2 = "https://blog.csdn.net/linaux_mctc/article/details/78970441"
url_3 = "https://blog.csdn.net/qq_26954773/article/details/53730064"
url_4 = "https://blog.csdn.net/peng_shakalaka/article/details/53165059"
url_5 = "https://blog.csdn.net/a1809032425/article/details/81268589"
#获取网址
html = urlopen(url_5).read().decode('utf-8') 
#解析网址
soup = BeautifulSoup(html,"html.parser") 
#选择CSS
titles=soup.select("#content_views h3") # CSS 选择器 
#根据已知属性值获取指定属性
#print(soup.find('a', attrs={'class',"follow-nickName"}).get_text())
f_1 = open('./0321.txt','w',encoding='utf-8')
i = 0
for title in titles: 
	#获取 li>h2的文本信息
	
	#获取文本信息，去掉左换行
	#print(title.get_text().lstrip())
	#f_1.write(title.get_text().lstrip())
	#f_1.write('\n')

	#.contents将子节点以列表的形式输出
	#tit = title.contents
	#print(tit[3].get_text())
	#f_1.write(tit[3].get_text())
	#f_1.write('\n')

	text = title.get_text().split()
	#print(text[-1])
	if len(text) > 0:
		print(text)
		
		for i in range(len(text)):
			if text[i] >= u'\u4e00' and text[i] <= u'\u9fa5':
				print(text[i])
				f_1.write(text[i])
				f_1.write(' ')
		f_1.write('\n')
		print('\n')
		
