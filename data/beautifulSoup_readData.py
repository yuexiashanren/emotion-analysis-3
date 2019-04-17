from bs4 import BeautifulSoup 
from urllib.request import urlopen 
import re
#专业领域词
url_data = "http://mt.wtulip.com/teacher/#/task-report"
#url_data = "https://blog.csdn.net/qq_41853758/article/details/82924765"

#获取网址
html = urlopen(url_data).read().decode('utf-8') 
#解析网址
soup = BeautifulSoup(html,"html.parser") 
#选择CSS
#titles = soup.select('.ant-table-content .ant-table-body') 
titles = soup.select('body') 
#根据已知属性值获取指定属性
#f_1 = open('./0321.txt','w',encoding='utf-8')
i = 0
print(type(titles))
print("title", titles)
'''
for word in titles: 
	i = i + 1
	print(i)
	print(word)
	print("word.get_text()", word.get_text())
	#f_1.write(str(word.get_text().strip()))
	#f_1.write('\n')
