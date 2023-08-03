#
# 类的创建
#
class Student:                      # class 之后为自定义类名
    native_space='HAK'               # 类属性
    
    def __init__(self,name,age):    # 初始化方法
        self.name=name              # 实例属性
        self.age=age

    def __str__(self):              # 利用 str 方法可以将对象在 print 后覆写
        return f'Student 类对象, name:{self.name}, age:{self.age}' 

    def __lt__(self, other):        # 用于比较对象（数字）的大小（只支持小于和大于）
        return self.age < other.age # 返回 True 或 False

    def __le__(self, other):        # 用于比较对象大小（支持大于等于和小于等于）
        return self.age <= other.age

    def __eq__(self, other):        # 用于检测两对象是否相等，不加该方法则比较内存地址
        return self.age == other.age

    def eat(self):                  # 实例方法，括号内 self 是默认参数
        print('They are eating.')

    @staticmethod                   # 引用 staticmethod 以创建静态方法，无默认参数
    def method():
        print('default output.')

    @classmethod                    # 创建类方法，括号内 cls 是默认参数
    def cm(cls):
        print('default classmethod.')


#
# 对象的创建
#
stu1=Student('LiHua',21)            # 创建一个Student类的对象
stu1.eat()                          # 调用实例方法，对象名.方法名()
print(stu1)                         # 由 str 方法控制该指令，类中没有 str 方法则输出地址
print(str(stu1))                    # 由 str 方法控制该指令
print(stu1.name)                    # 显示属性
print(stu1.age)

Student.eat(stu1)                   # 调用实例方法，类名.方法名(类的对象)-->实际就是方法
                                    # 定义处的 self
print('<------------------------------------------------>')


#
# 类属性
#
print(Student.native_space)
stu2=Student('Jack',20)             # 创建该类的对象，Jack传入初始化方法name形参，并赋值给
stu3=Student('Mike',21)             # self.name，20传入形参age，并赋值self.age

print(stu1.native_space)            # 显示类属性
print(stu2.native_space)

Student.native_space='CKG'          # 更改类属性
print(stu1.native_space)
print(stu2.native_space)
print('<--------------------------------------->')


#
# 类方法
#
Student.cm()                        # 调用类方法


#
# 静态方法
#
Student.method()                    # 调用静态方法


#
# 动态绑定属性和方法
#
stu2.gender='female'                # 为对象stu2添加实例属性
print(stu2.name,stu2.age,stu2.gender)
stu1.eat()
stu2.eat()

def exp():
    print('Default funtion1.')
stu1.func1=exp                      # 为stu1创建一个新的方法，绑定函数exp()
stu1.func1()                        # 调用该方法


