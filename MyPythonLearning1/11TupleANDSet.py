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
set1={'Galaxy','Python','Tablet'}       # 集合元素排列不一定按顺序
set2=set(range(6))
set3=set([9,2,5,3,8,6,1,1,10])          # 将列表内元素逐个转为集合元素，忽略重复元素
set4=set((98,4,3,7,7,4,1,2,7))          # 将元组内元素逐个转为集合元素
set5=set('Galaxy')                      # 此写法将把字符串字母依次转为集合元素,同时忽略重复元素
set6=set()                              # 定义空集合
print('set1的结果1:',set1)
print('set2的结果1：',set2)
print(set3)
print(set4)
print(set5)


# 集合数据操作
print('10 in set3?',10 in set3)

set1.add(7.9)                       # 添加一个元素
print('set1结果2：',set1)
set4.update(['Galaxy'],['fold'])    # 添加多个元素，注意字符串整个添加须作为列表对象，
                                    # 否则只依次添加字母
set4.update(['SA','NSA'])           # 两组写法都添加的是元素，而不是整个列表
print('set4结果1：',set4)
print('<------------------------------------------->')

# 集合删除
set4.remove('Galaxy')               # 删除一个元素
print('set4结果2：',set4)
set4.discard('500')                 # 不存在该元素，但编译器不报错
set4.pop()                          # 随机删除一个元素
set3.clear()                        # 清空集合
print('set4结果3：',set4)
print('set3结果1：',set3)
print('<------------------------------->')

# 集合间的运算
set7={9,2,5,4}
set8={2,4,5,9}
print('set7 is equal to set8? ',set7==set8)         # 两集合是否相等
set7.update([89,100,34])
print('set8 is sub to set7? ',set8.issubset(set7))  # 判断一集合是否是另一个集合的子集
# 判断一集合是否是另一个集合的超集
print('set7 is superset to set8?',set7.issuperset(set8))
print('set7与set8是否有交集？',set7.isdisjoint(set8))  # 判断两集合是否有交集，false为有交集
print('<------------------------------------------------>')

print('set7与set8交集：',set7.intersection(set8))       # 两集合交集运算
print('set7与set8交集：',set7 & set8)                   # 两集合交集运算

print('set7与set8并集：',set7.union(set8))              # 两集合并集运算
print('set7与set8并集：',set7 | set8)

print(set7.difference(set8))                            # 两集合差集运算,求在set7中同时
print(set7-set8)                                        # 不在set8中的元素集合

set8.update([2.1,65,3.8])
print(set7.symmetric_difference(set8))                  # 两集合对称差集运算,求两者的并
                                                        # 集减去交集

# 集合生成
set9={i*i for i in range(10)}           # 其中i*i表示生成的元素表达式
print('set9的结果1：',set9)              # 无序