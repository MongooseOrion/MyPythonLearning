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
        super().info()                          # 重写父类中的 info() 方法。通过super().func()
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
print('<------------------------------------------------>')


#
# 多态
#
class Animal(object):
    def eat(self):
        print('Animals can eat.')
class Dog(Animal):
    def eat(self):
        print('Dogs can feet.')
class Cat(Animal):
    def eat(self):
        print('Cats can fish.')
class Person2(object):
    def eat(self):
        print('Human eat everything.')

def exp2(obj):
    obj.eat()                               # 定义函数链接类中的方法

exp2(Cat())                                 # 调用该函数
exp2(Person2())
exp2(Animal())


#
# 特殊方法与属性
#
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name 
        self.age=age 
cans=C('Jack',22)                           # 为 C 创建实例对象
print(cans.__dict__)                        # 实例对象的属性字典
print(cans.__class__)                       # 对象所属的类
print(C.__bases__)                          # 该类所属的所有父类
print(C.__base__)                           # 所属的最近的父类，这里显示A
print(C.__mro__)                            # 类的整个父子结构
print(A.__subclasses__())                   # 类的子集列表


class Student4:
    def __init__(self,name):
        self.name=name 
    def __add__(self,other):                # add 可用于拼接两个对象
        return self.name+other.name
    def __len__(self):                      # len 可用于显示指定对象的长度
        return len(self.name)

stu3=Student4('Jame')
stu4=Student4('MMSAD')
s=stu3+stu4
print(s)
print(len(stu4))
print('<-------------------------------------------->')


#
# 初始化方法和创建对象
#
class Person5(object):
    def __new__(cls,*args,**kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))    # 4336
        obj=super().__new__(cls)                                     # cls 传入此处，创建对象obj（2）
        print('创建的对象的id为：{0}'.format(id(obj)))                 # 7536，对象obj的id（3）
        return obj                                                   # obj将返回给下一行的 self 中（4）
    def __init__(self,name,age):
        print('__init__方法被调用了，self的id为：{0}'.format(id(self))) # 7536，承接（3）
        self.name=name 
        self.age=age                                                 # 初始化完成，参数传回主进程变量 p1（5）

print('object这个类对象的id为: {0}'.format(id(object)))                # 0848
print('Person这个类对象的id为：{0}'.format(id(Person5)))               # 4336

p1=Person5('Tom',21)                    # 创建Person5的实例对象,等号右半边的代码被传入cls中，
                                        # 上式的id：4336出现在类中（1）
print('p1这个Person5类的实例对象的id：{0}'.format(id(p1)))              # 7536
print('<-------------------------------------------------------------->')


#
# 类的浅拷贝与深拷贝
#
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk 

cpu1=CPU()
cpu2=cpu1
