import json

# 字典或元素为字典的列表可以转换为 json 格式
data=[{'name':'Li Hua','age':16},{'name':'Michael','age':19}]

# 将 Python 数据转换为 json 数据
json_str=json.dumps(data,ensure_ascii=False)        # 不转换为ASCII，以确保中文正确显示
print(json_str)
print(type(json_str),end='\n')                      # 说明 json 格式是字符串类型

# 将 json 数据转换为 Python 数据
py_str=json.loads(json_str)
print(py_str)
print(type(py_str))
print('<-------------------------------------------------------->\n')



#
# 可视化图表
#
# https://gallery.pyecharts.org/#/README
# 在 Module_2 中查看