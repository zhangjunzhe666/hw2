# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 19:22:03 2019

@author: Administrator
"""

#密码本：5位
#导入迭代器工具
import itertools as it
numbers = "1234567890"
#生成5数随机的排列，类型为元组
r = it.product(numbers,repeat = 5)
#用文件打开这些数据
for i in r:
    data = open("password.txt","a")#以追加的模式添加数据到一个txt文件中
    #元组不能写入到文件中去，需要用到方法join()
    data.write("".join(i))
    #换行
    data.write("".join('\n'))
data.close()