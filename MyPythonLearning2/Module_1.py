
import math                 # 导入数学常数模块（预置）
print(id(math))
print(type(math))
print(math)
print(math.e)
print(dir(math))            # 查看math的所有属性
print(math.pow(2,3))        # 指的是2^3
print(math.ceil(9.001))     # 向上取整
print(math.floor(9.999))    # 向下取整
print('<-------------------------------------------------->')

from math import pi         # 选择导入某模块中的参数
print(pi)


#
# 选择导入自定义模块，平级的模块到模块
#
import main                 # 全部导入
print(main.add(10,20))

from main import div        # 部分导入
print(main.div(90,3))


#
# 选择导入自定义包中的模块
#
import package1.Module_subP1_1 as a
print('a的调用结果为：',a.func1(1,2))

# 使用 from...import... 语句
from package1 import Module_subP1_1 as b
print('b的调用结果为：',b.func1(3,4))

# 使用该语句可以导入包、包内模块，并指定函数，而 import 只能导入模块
from package1.Module_subP1_1 import func1 as c
print('c的调用结果为：',c(3,4))
print('<----------------------------------------------->')


#
# 使用在线 Python 模块，须在“搜索路径”中添加扩展所在的路径
#
import schedule                             # 在线下载的模块
import time
def job():
    print('渐进式打印，每隔3秒打印')
schedule.every(3).seconds.do(job)           # 单位为秒,每隔3秒执行一次
while True:
    schedule.run_pending()
    time.sleep(1)                           # 延迟1秒