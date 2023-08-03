from file_define import *
from data_define import *
from pyecharts.charts import *
from pyecharts.options import *
from pyecharts.globals import ThemeType


text_file_reader = TextFileReader('C:/Users/YiMon/Source/Repos/MyPythonLearning/MyPythonLearning2/package2/2011年1月销售数据.txt')
json_file_reader = JsonFileReader('C:/Users/YiMon/Source/Repos/MyPythonLearning/MyPythonLearning2/package2/2011年2月销售数据JSON.txt')

jan_data:list[Record] = text_file_reader.read_data()
feb_data:list[Record] = json_file_reader.read_data()

# 合并两个列表
all_data:list[Record] = jan_data + feb_data 

# 将内容转变为 {'2011.01.01': 1111, '2011.01.02':2222} 的形式
data_dic = {}
for record in all_data:
    if record.date in data_dic.keys():
        # 如果键存在，则将该日期下的所有值累加
        data_dic[record.date] += record.money
    else:
        # 第一个值
        data_dic[record.date] = record.money

#print(data_dic)


# 绘图
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dic.keys()))
bar.add_yaxis('销售额', list(data_dic.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts('每日销售额')

    )

bar.render('销售额情况.html')