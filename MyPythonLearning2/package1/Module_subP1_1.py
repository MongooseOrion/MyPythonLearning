
a=10
b=20

def func1(num1,num2):
    result=num1+num2/num1+a*b
    return result

# 在 Module_1 中被引用
#########################


#
# 使用类定义计算圆参数功能
#
import math
class Circle(object):
    def __init__(self,r):
        self.r=r

    def square(self):
        return math.pi*(self.r**2)

    def perimeter(self):
        return 2*math.pi*self.r 
'''
num1=int(input('请输入圆的半径：'))
c=Circle(num1)
print('圆的面积为：{:.2f} cm^2'.format(c.square()))
print('圆的周长为：{:.2f} cm'.format(c.perimeter()))
print('<---------------------------------------------->')
'''

#
# 定义一个学生类
#
class Stu_info():
    def __init__(self,stu_name,stu_age,stu_gender,stu_score):
        self.stu_name=stu_name
        self.stu_age=stu_age
        self.stu_gender=stu_gender 
        self.stu_score=stu_score 

    def show(self):
        print(self.stu_name,self.stu_age,self.stu_gender,self.stu_score)
'''
print('请输入 5 位学生的信息（以 姓名#年龄#性别#分数 为格式：）\n')
lst=[]
for i in range(5):
    str=input(f'请输入第 {i+1} 名学生的信息：\n')
    s_lst=str.split('#')
    stu=Stu_info(s_lst[0],int(s_lst[1]),s_lst[2],int(s_lst[3]))
    lst.append(stu)
for item in lst:
    item.show()
'''


#
# 模拟高铁售票系统
#
import prettytable as excel
def show_tic(row_num):
    table=excel.PrettyTable()
    table.field_names=['行号','座位1','座位2','座位3','座位4','座位5','座位6']
    for i in range(row_num):
        lst=[f'第{i+1}行','有票','有票','有票','有票','有票','有票']
        table.add_row(lst)
    print(table)

def order_tic(row_num,row,column):
    table=excel.PrettyTable()
    table.field_names=['行号','座位1','座位2','座位3','座位4','座位5','座位6']
    for i in range(row_num):
        if int(row)==i+1:
            lst=[f'第{i+1}行','有票','有票','有票','有票','有票','有票']
            lst[int(column)]='已售'
            table.add_row(lst)
        else:
            lst=[f'第{i+1}行','有票','有票','有票','有票','有票','有票']
            table.add_row(lst)
    print(table)
'''
row_num=13
show_tic(row_num)
choose_num=input('请输入选择的座位：（行,列）')
row,column=choose_num.split(',')
order_tic(row_num,row,column)
'''


#
# 时间
#
import datetime
def date_cal():
    

