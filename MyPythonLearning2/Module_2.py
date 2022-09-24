#
# 导入 Python 内置模块
#

from sqlite3 import Time
import sys
from turtle import position
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
line.render('测试折线图.html')                        # 绘制图像，生成 HTML 文件


#
# 构建地图
#

from pyecharts.charts import Map 
from pyecharts.options import VisualMapOpts
map=Map()
data=[
    ('北京',100),
    ('重庆',101),
    ('香港',102),
    ('海南',103),
    ('广东',105)
]

map.add('测试地图', data, 'china')
map.set_global_opts(
    visualmap_opts = VisualMapOpts(
        is_show=True, 
        is_piecewise=True,  # 手动校正图例参数
        pieces=[
            {'min':1,'max':9,'label':'1-9','color':'#CCFFFF'},
            {'min':10,'max':99,'label':'10-99','color':'#FF6666'},
            {'min':100,'max':500,'label':'100-500','color':'#990033'}
        ]
    )
)

map.render('中国地图测试.html')

'''
# 全国疫情数据
import json
from pyecharts.charts import Map
from pyecharts.options import *
f = open('疫情.txt', 'r', encoding = 'utf-8')
data = f.read()
f.close()

data_dic = json.loads(data)                                 # 将数据转为 python 字典
province_list = data_dic['areaTree'][0]['children']         # 从字典中取出省份数据

data_list = []
for province_data in province_list:                         # 分别获取省份、确诊人数
    province_name = province_data['name']
    province_confirm = province_data['total']['confirm']
    data_list.append((province_name, province_confirm))     # 将省份和确诊人数作为元组存入列表
# print(data_list)

map = Map()
map.add('各省份确诊人数', data_list, 'china')
map.set_global_opts(
    title_opts = TitleOpts(title='全国疫情地图'),
    visualmap_opts = VisualMapOpts(
        is_show=True,               # 是否显示视觉映射
        is_piecewise=True,          # 是否分段
        pieces=[                    # 各分段数
            {'min':1,'max':99,'label':'1-9','color':'#CCFFFF'},
            {'min':100,'max':999,'label':'100-999','color':'#990033'},
            {'min':1000,'max':4999,'label':'1000-4999','color':'#107c42'},
            {'min':5000,'max':9999,'label':'5000-9999','color':'#8a02a7'},
            {'min':10000,'max':99999,'label':'10000-99999','color':'#849b91'},
            {'min':100000,'label':'100000 以上','color':'#1285dc'}
        ]
    )
)

map.render('全国疫情地图.html')
'''
'''
# 省级地图绘制
import json
from pyecharts.charts import Map
from pyecharts.options import *
f = open('疫情.txt','r',encoding='utf-8')
data = f.read()
f.close()
data_dic = json.loads(data)
cities_data = data_dic['areaTree'][0]['children'][3]['children']

data_lst = []
for city_data in cities_data:
    city_name = city_data['name']+'市'
    city_cofirm = city_data['total']['confirm']
    data_lst.append((city_name, city_cofirm))
# print(data_lst)
data_lst.append(('济源市', 5))             # 无数据，手动添加

map = Map()
map.add('河南省确诊人数', data_lst, '河南')
map.set_global_opts(
    title_opts = TitleOpts(title='河南疫情地图'),
    visualmap_opts = VisualMapOpts(
        is_show=True,               # 是否显示视觉映射
        is_piecewise=True,          # 是否分段
        pieces=[                    # 各分段数
            {'min':1,'max':99,'label':'1-9','color':'#CCFFFF'},
            {'min':100,'max':999,'label':'100-999','color':'#990033'},
            {'min':1000,'max':4999,'label':'1000-4999','color':'#107c42'},
            {'min':5000,'max':9999,'label':'5000-9999','color':'#8a02a7'},
            {'min':10000,'max':99999,'label':'10000-99999','color':'#849b91'},
            {'min':100000,'label':'100000 以上','color':'#1285dc'}
        ]
    )
)
map.render('河南省疫情地图.html')
'''

#
# 构建柱状图
#
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar = Bar() 
bar.add_xaxis(['中国', '美国', '英国'])
bar.add_yaxis('GDP', [30,20,10], label_opts = LabelOpts(position = 'right'))    # 数字显示在右边
bar.reversal_axis()                         # 翻转 x，y 轴
bar.render('柱状图测试.html')


#
# 按时间线绘制柱状图
#
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar1 = Bar() 
bar1.add_xaxis(['中国', '美国', '英国'])
bar1.add_yaxis('GDP', [30,20,10], label_opts = LabelOpts(position = 'right'))
bar1.reversal_axis()

bar2 = Bar() 
bar2.add_xaxis(['中国', '美国', '英国'])
bar2.add_yaxis('GDP', [40,30,90], label_opts = LabelOpts(position = 'right'))    # 数字显示在右边
bar2.reversal_axis()

bar3 = Bar() 
bar3.add_xaxis(['中国', '美国', '英国'])
bar3.add_yaxis('GDP', [100,80,60], label_opts = LabelOpts(position = 'right'))    # 数字显示在右边
bar3.reversal_axis()

timeline = Timeline(
    {'theme': ThemeType.LIGHT}              # 选择配色主题
)
timeline.add(bar1, 'Point 1')
timeline.add(bar2, 'Point 2')
timeline.add(bar3, 'Point 3')

timeline.add_schema(                        # 自动播放设置（循环）
    play_interval=1000,                     # 单位 ms
    is_timeline_show=True,                  
    is_auto_play=True,
    is_loop_play=True
)
timeline.render('基础时间线柱状图.html')


#
# 动态柱状图
#
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *


file1 = open('1960-2019全球GDP数据.csv','r',encoding='GB2312')
data_lines = file1.readlines()
file1.close()

data_lines.pop(0)
# 将数据转换为字典存储，格式为：
# { 1960:[[美国, 123],[中国, 321]...], 1961:[[美国,123],...],...}
data_dic = {}
for lines in data_lines:
    year = int(lines.split(',')[0])                 # 年份
    country = lines.split(',')[1]                   # 国家
    gdp = float(lines.split(',')[2])                # 科学计数法可用 float 强制类型转换
    # 判断是否要加列表
    try:
        data_dic[year].append([country, gdp]) 
    except KeyError:
        data_dic[year] = []
        data_dic[year].append([country, gdp]) 

timeline = Timeline()
# 由于字典中 key 的位置不是固定的，首先排序确保年份按顺序
sorted_year_list = sorted(data_dic.keys())

for year in sorted_year_list:
    data_dic[year].sort(key=lambda element:element[1], reverse=True)    # 按键值排序
    year_data = data_dic[year][0:8]                                 # 选择出前 8 位数据
    x_data = []                                         # 国家
    y_data = []                                         # GDP 数值
    for country_gdp in year_data:
        x_data.append(country_gdp[0])                   # x 轴数据
        y_data.append(country_gdp[1]/100000000)         # y 轴数据

    # 构建图像
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GDP(亿)', y_data, label_opts = LabelOpts(position='right'))
    bar.reversal_axis()

    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
    )

timeline.render('动态柱状图1960-2019GDP.html')
