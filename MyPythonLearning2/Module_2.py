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
# 导入 pyecharts 绘制图表
#
import pyecharts
from pyecharts.charts import Line       # 构建折线图
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line=Line()
line.add_xaxis(['China','USA','UK'])    # 构建 X 轴
line.add_yaxis('GDP',[30,10,20])        # 构建 Y 轴
line.add_yaxis('Public',[14,5,6])

line.set_global_opts(                   # 配置参数
    # 配置标题
    title_opts=TitleOpts(title='测试曲线',pos_left='center',pos_bottom='1%'),
    # 图例
    legend_opts=LegendOpts(is_show=True),
    # 工具箱
    toolbox_opts=ToolboxOpts(is_show=True),
    # 视觉映射
    visualmap_opts=VisualMapOpts(is_show=True)
)
line.render()                           # 绘制图像，生成 HTML 文件

