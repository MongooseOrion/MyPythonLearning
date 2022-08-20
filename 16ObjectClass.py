#
# 封装
#
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('The Car has been started...')
car=Car('Audi')
car.start()
print(car.brand)
print('<----------------------------------------------------------->')

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age              # 加两个下划线则在类外部不可被直接引用
    def exp1(self):
        print(self.name,self.__age)
stu1=Student('Michael',22)
stu1.exp1()
print(stu1.name)
# 如果想要引用 age 属性
print(dir(stu1),'\n')           # 首先获取stu1对象所包含的所有属性
print(stu1._Student__age)       # 找到对应的名字，引用即可
print('<------------------------------------------------->')


#
# 继承
#
class Person(object):                           # 父级
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):                          # 子集1
    def __init__(self,name,age,stu_num):
        super().__init__(name,age)
        self.stu_num=stu_num 
    def info(self):
        super().info()                          # 重写父类中的 info() 方法，通过super().func()
                                                # 即可重写方法
        print(self.stu_num)

class Teacher(Person):                          # 子集2
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()                          # 重用
        print(self.teachofyear)

stu1=Student('Micheal',22,1659473)
teach1=Teacher('Miss Tab',34,10)
stu1.info()                                     # 子集1继承
teach1.info()                                   # 子集2继承
print('<------------------------------------------------------->')


#
# object类
#
class Defau:
    def __init__(self,name,age):
        self.name=name 
        self.age=age 
    def __str__(self):          # __str__()方法用于返回对象描述，如果重写则用于查看对象信息
        return 'My name is {0}, and I am {1} years old.'.format(self.name,self.age)
defau1=Defau('Sam',23)
print(dir(defau1),'\n')
print(defau1)


#
# 多态
#
