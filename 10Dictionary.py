#
# How to build dictionary
#
dic1 = {'Mongoose':100,'Li hua':97,'Jim':69}        # 第一种
dic2 = dict(name='Jack',score=76)                   # 第二种
print('dic1结果1：',dic1)
print('dic2结果1：',dic2)

# 查找字典内元素
print(dic1['Mongoose'])         # 不存在则报错
print(dic1.get('Jim'))          # 不存在则返回none，推荐此种方法
print(dic1.get('Michel',97))    # 不存在则返回设置默认值97

