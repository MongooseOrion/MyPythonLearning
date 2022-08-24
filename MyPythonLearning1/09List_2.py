#
# 列表的排序操作
#
lst1=[9,3,2,6,1,7,8,4,5,3]
lst1.sort()             # 按升序排列列表元素
print('lst1的结果1为：',lst1)
lst1.sort(reverse=True) # 按降序排列列表元素
print('lst1的结果2为：',lst1)
lst2=sorted(lst1)       # 按升序排列的列表另存为新列表
print('lst2的结果1为：',lst2)
lst2=sorted(lst1,reverse=True)  # 按降序排列的列表另存为新列表
print('lst2的结果2为：',lst2)
print('<-------------------------------------------->')


# 列表生成
lst3=[i*i for i in range(10)]       # i*i位置表示元素表达式，i表示自定义变量
print('lst3的结果1为：',lst3)
lst4=[i*2 for i in range(1:6)]      # 表示2，4，6，8，10
print('lst4的结果1为：',lst4)
