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


# 字典元素操作
print('dic1判断1：','Jim' in dic1)
del dic1['Mongoose']            # 删除字典指定元素
print('dic1结果3：',dic1)
dic1['Tim']=79                  # 增加字典元素
print('dic1的结果4：',dic1)
dic1['Mongoose']=83
print('dic1的结果5：',dic1)      # 修改字典元素，位置变到末尾

keys1=dic1.keys()                      # 获取列表所有键
print('keys1的结果1：',list(keys1))     # 将字典的所有键排列为列表显示
values1=dic1.values()                  # 获取列表所有值
print('values1的结果1：',list(values1))  # 将字典内所有值排列为列表显示

items1=dic1.items()                     # 获取列表内所有键值对
print('items1的结果1：',list(items1))   # 将键值对作为列表显示


# 字典元素遍历
for i in dic1:              # 变量被赋的值为键，而不是值
    print(i,dic1.get(i))
