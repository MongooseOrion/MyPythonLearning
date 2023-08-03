#
# 列表类型注解
#
# 语法：变量名:类型=值
my_list: list = [1,2,34]
my_list2: list[int, str] = [1,'galaxy']
print('my_list2 is: ',my_list2)


# 创建列表
lst1=['hello','world',100,1.2]                # 列表用法1
lst2=list(['hello','world',98,'hello'])       # 列表用法2
print('指定元素显示为：',lst1[0],lst1[-4])      # 表示元素相同
print('<------------------------------------------------->')

print('hello的索引标识数字为：',lst2.index('hello'))
# print(lst2.index('python'))                  # 不在list中 
# print(lst1.index('hello',1,3))               # 在列表内第二个到第三个元素中查找（索引1-2）


# 获取列表多个元素（切片）
print(lst2[0:3:1])              # 获取列表内0-2的每个元素
print(lst2[::-1])               # 元素逆序输出
print(lst2[-4:-2:1])            # 倒数第四个元素至倒数第3个元素，正向步长1
print(lst2[1::-1])              # 逆序输出上式
print('<------------------------------------------------->')


print('列表布尔运算：',('world' in lst2) and (1.2 in lst1))
# 使用for ...in...循环遍历列表
for r in range(4):
    print('输出',r+1,'为',lst2[r])
    r+=1
print('<------------------------------------------------->')


# 列表增加操作
lst2.append('Galaxy')
print('lst2的结果1：',lst2)
lst1.append(lst2)       # 将lst2作为一个元素扩展入lst1尾部
print('lst1的结果1：',lst1)
lst1.extend(lst2)       # 将lst2中的元素逐个扩展入lst1尾部
print('lst1的结果2：',lst1)
lst2.insert(2,3.14)     # 在lst2索引2（第三个元素）位置插入元素3.14
print('lst2的结果2：',lst2)
lst1[2:4:]=lst2         # 从lst1索引2元素开始替换为lst2中的所有元素，直到索引4元素不替换
print('lst1的结果3：',lst1)
# 上述的列表数据写入实际上是对地址进行操作，在lst1结果1中插入了lst2结果1并作为一个元素，
# 而后列表lst2元素发生了一些改变。在lst1结果3中显示的元素lst2实际是被更改过的lst2结果2，
# 而非lst2结果1，这就说明列表内的每个元素都有各自的地址空间，如果单个元素被操作，则在
# 之后调用整个列表时，会显示更改后的元素值。
print('<-------------------------->')

# 列表删除操作
lst3=[1,2,1,3.14,7,-9,0.2]
lst3.remove(1)          # 将列表内第一个匹配的元素移除
print('lst3的结果1为：',lst3)
lst3.pop(2)             # 删除列表内索引2元素（第三个元素）
print('lst3的结果2为：',lst3)
lst4= lst3[1:4]         # 列表内索引1-3组成新列表
print('lst4的结果1为：',lst4)
lst3[1:4]=[]            # 将列表内索引1-3删除
print('lst3的结果3为：',lst3)
print('<--------------------------------------->')


# 列表修改操作
lst5=[1,3,4.1,3.14,10.2]
lst5[2]=0.7             # 将列表索引2元素修改
print('lst5的结果1为：',lst5)
lst5[1:3]=['Galaxy','CQUPT','testbench',890,990]
print('lst5的结果2为：',lst5)
