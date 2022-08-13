#
# Tuple 元组
# 
# 创建方法
tup1=('python','Galaxy',3.14,4)                 # method1,可省略小括号
tup2=tuple(('save','double',2.7,[7,9]))         # method2
tup3=('best',)                                  # 元组仅含有1个元素时需要加逗号以表示元组类型
print('tup1结果1:',tup1)
print('tup2结果1：',tup2)

print('tup1索引1为：',tup1[1])          # 元组内单个元素查找方法


# 元组不允许修改，但元组内如果包含列表或字典，则列表内元素可被修改
tup2[3][1]=2                    # 对元组中的列表值进行修改
tup2[3].append(tup1)            # 对元组中的列表增加元素，如果添加的元素是列表，则列表
                                # 类型变为元组
# tup2[3][2][1]=89  # 报错
print('tup2结果2：',tup2)


# 元组遍历
for i in range(4):
    print('元组tup1的元素',i,'为:',tup1[i])
print('<-------------------------------------------->')

#
# 集合 Set
# 
# 集合创建
set1=