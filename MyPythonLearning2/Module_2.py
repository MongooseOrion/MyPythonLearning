#
# 导入 Python 内置模块
#
import sys
print(dir(sys))                                 # 查看 sys 内的所有函数
print('True的字节数：',sys.getsizeof(True))      # 获取指定字符的数据占用量

import time
print(dir(time))
print('<----------------------------------------------->')
print(time.time())                          # 总时间
print(time.localtime(time.time()))          # 转换为当前时间

import urllib.request as a
print(a.urlopen('https://cn.bing.com').read())      # 读取该网页所有内容并返回


#
# 从其他文件导入类
#