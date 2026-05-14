"""
CP1404 Final 2026 TR1S
"""

# 第六章 函数进阶

# 第1节 函数的多返回值
"""
def test_return():
    return 1, 2
    
x, y = test_return()
print(x)
print(y)

按照返回值的顺序，写对应顺序的多个变量接收即可
变量之间用逗号隔开
支持不同类型的数据return
"""

# 第2节 函数的多种传参方式
"""
 - 位置参数:
    调用函数时根据函数定义的参数位置来传递参数
    
    def user_info(name, age, gender):
        print(f"Your name is {name}, your age is {age}, your gender is {gender}")
    
    user_info("Tom", 22, "male")
    
    注意：传递的参数和定义的参数的顺序以及个数必须一致

 - 关键字参数：
    函数调用时通过“键=值”的形式传递参数
    可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求
    
    def user_info(name, age, gender):
        print(f"Your name is {name}, your age is {age}, your gender is {gender}")
    
    user_info(name = "Tom", age = 22, gender = "male")
    user_info("Tom", age = 22, gender = "male")
    
    可以与位置参数混用，但位置参数必须在前且顺序及个数正确，但关键字参数之间不存在先后顺序
    
 - 缺省参数（默认参数）：
    用于为参数提供默认值；调用函数时可以不传该默认参数的值
    所有位置参数必须出现在默认参数前，包括函数的定义和调用
    当调用函数时没有传递参数，就会默认使用缺省参数对应的值
    
    def user_info(name, age, gender = '男'):
        print(f"Your name is {name}, your age is {age}, your gender is {gender}")
    
    user_info("Tom", 22)
    user_info("Rose", 18, gender = "female")
    
    函数调用时，如果为缺省参数传值则修改默认参数值，否则使用这个默认值
    
 - 不定长参数（可变参数）：
    用于不确定调用函数的时候会传递多少个参数（或者不传参数）的情景
    
    类型1：位置传递
    
    def user_info(*args): # 使用单星号
        print(args)
    
    user_info('Tom')
    user_info('Rose', 18)
    
    传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组，args是元组类型
    
    类型2：关键字传递
    适用于参数是“键=值”的情况
    
    def user_info(**kwargs): # 使用双星号
        print(kwargs)
    
    user_info('name': 'Tom', 'age': 18, 'gender': 'male')):

    所有的“键=值”都会被kwargs接收，同时会根据键值组成字典
"""


# 第3节 匿名函数
"""
 - 函数作为参数传递

    def test_func(compute):
        result = compute(1, 2)
        print(result)
    
    def compute(x, y):
        return x + y
    
    test_func(compute)

 - lambda 匿名函数
    def关键字可以定义带有名称的函数，可以基于名称重复使用
    lambda关键字可以定义匿名函数（无名称），只可临时使用一次
    
    语法：
    lambda 传入参数：函数体
    注意：仅能写一行代码，无法写多行
"""
