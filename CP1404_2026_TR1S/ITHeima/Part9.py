"""
CP1404 Final 2026 TR1S
"""

# 第九章 面向对象编程

# 第1节 类和对象
"""
类：
用于在程序中组织数据；
不仅可以定义属性用来记录数据，
也可以定义函数用来记录行为。

包含
属性（变量）：成员变量
和
行为（函数）：成员方法
    函数是写在类外的；
    定义在类内部，均称之为方法

 - 步骤
    1. 设计类 Class
        class 类名：
            变量1 = None
            变量2 = None
            ...
            
            def 方法1（self，形参1，形参2，...）
                方法体
            
    2. 创建对象
        对象1 = 类名（）
        
    3. 对对象属性进行赋值
        对象1.变量1 = 变量值
        对象1.变量2 = 变量值
        ...
        
    4. 获取对象中记录的信息
        print（对象1.变量1）
        print（对象1.变量2）
        ...
"""

class Student:
    name = None

    def say_hi(self):
        print(f"Hello. I am {self.name}.")
        # 在成员方法内部，如果要访问其它成员变量，需要使用self关键字，表示类对象本身

    def say_hi2(self, msg):
        # 在实际传入参数时，self关键字可以忽略，不占用参数位置
        print(f"Hello. I am {self.name}, {msg}")

stu1 = Student()
stu1.name = "Joy"
stu1.say_hi()
stu1.say_hi2("JJJ")

stu2 = Student()
stu2.name = "Mike"
stu2.say_hi()
stu2.say_hi2("BBB")

"""
类和对象的关系：类是图纸，对象是基于图纸的具体生产实体
面向对象编程就是：适用对象进行编程
即，设计类，基于类创建对象，并使用对象来完成具体的工作
"""

# 第2节 构造方法与魔术方法
"""
使用构造方法向成员变量赋值

Python类可以使用：__init__（）方法，称之为构造方法

可以实现：
 - 在创建类对象（构造类）的时候，会自动执行
 - 在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用
"""
class Student2:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    """
    内置类方法1（魔术方法）：
        __str__ 字符串方法
            当类对象需要被转换为字符串时，会输出内存地址
            内存地址没有太大作用，此时可以通过__str__ 字符串方法，控制类转换为字符串的行为
    """
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Tel: {self.tel}"

    """
    内置类方法2-1（魔术方法）：
        __lt__ 小于符号比较方法
            直接对两个对象进行比较是不可以的
            但在类中实现__lt__ 方法，即可同时完成 ＜ 和 ＞ 两种比较
    """
    def __lt__(self, other):
        return self.age < other.age

    """
    内置类方法2-2（魔术方法）：
         __le__ 小于等于符号比较方法
        """
    def __le__(self, other):
        return self.age <= other.age

    """
    内置类方法2-3（魔术方法）：
        __eq__ 相等符号比较方法
    """
    def __eq__(self, other):
        return self.age <= other.age

stu3 = Student2("Tom", 35, "123456")
stu4 = Student2("Ben", 19, "567890")

print(stu3.name)
print(stu3.age)
print(stu3.tel)
print(stu3)
print(str(stu3))
print(stu3 >= stu4)
print(stu3 <= stu4)
print(stu3 == stu4)
print(stu3 == stu4)

# 第3节 封装
"""
封装：
    将现实世界事物的属性、行为，
    封装到类中，描述为：成员变量、成员方法
    从而完成程序对现实世界事物的描述
    
私有成员变量 & 私有成员方法
    无法被类对象访问的成员变量 & 成员方法
    仅供类内部其他成员访问
    
    语法：
        __成员变量
        __成员方法
"""

class Phone:

    __current_voltage = 1

    def __keep_single_core(self):
        if self.__current_voltage >= 1:
            print("CPU is running with double core model")
        else:
            print("CPU is running with single core model")

    def call_by_5g(self):
        phone.__keep_single_core()
        if self.__current_voltage >= 1:
            print("5G call is opening.")
        else:
            print("5G call can not be used")

phone = Phone()
phone.call_by_5g()


# 第3节 继承
"""
单继承：
    class 类名（父类名）：
        类内容体

多继承：
    class 类名（父类1，父类2，父类3，...）：
        类内容体
    如果父类有同名方法或属性。先继承的优先级高于后继承
    
pass关键字：
    保证函数（方法）或类定义的完整性，表示无内容、空
    
复写父类成员或方法：
直接重新定义需要复写的父类成员或方法

调用父类成员：
    方式1：
        使用成员变量：父类名.成员变量
        使用成员方法：父类名.成员方法（self）
        
    方式2：
        使用super（）调用父类成员
        使用成员变量：super（）.成员变量
        使用成员方法：super（）.成员方法
注意：只可以在子类内部调用父类的同名成员，
     子类的实体类对象调用默认是调用子类复写的
"""


# 第4节 类型注解
"""
在代码中设计数据交互的地方，提供数据类型的注解；
帮助第三方IDE工具对代码类型进行推断，协助做代码提示
帮助开发者自身对变量进行类型注释

 - 变量的类型注解
    语法：
        变量：类型 （ = 值） # 也可在定义变量值时进行注解，赋值可以省略
        容器可以进行基础注解（定义容器的类型），也可以进行详细注解（定义内部每个元素的类型）
    
    函数（方法）形参列表和返回值的类型注解



"""