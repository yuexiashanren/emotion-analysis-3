import os
#筛选某一学生所有评论数据
os.system("python ./read_oneStu_allWeek.py")
#得出该学生最终的学习过程情感值
os.system("python ./final_value.py")
