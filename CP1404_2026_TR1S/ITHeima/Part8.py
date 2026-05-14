"""
CP1404 Final 2026 TR1S
"""

# 第八章 异常、模块、包和json文件

# 第1节 异常简介及捕获异常
"""
 - 异常：BUG
 - 捕获异常：预期可能出现异常时，提前对其进行处理，避免程序直接崩溃

 - 捕获全部异常
    try:
        预期可能出现异常的代码
    expect:
        如果出现异常则执行的代码
    else： （可选）
        如果未出现异常则执行的代码
    finally： （可选）
        无论是否出现异常均要执行的代码

 - 捕获指定异常
    try:
        预期可能出现异常的代码
    expect 异常类型名 as 异常对象名:
        如果出现异常则执行的代码

 - 捕获多个异常
    try:
        预期可能出现异常的代码
    expect （异常类型名1，异常类型名2，...） as 异常对象名:
        如果出现异常则执行的代码

 - 捕获全部异常（顶级）
    try:
        预期可能出现异常的代码
    expect Exception as 异常对象名:
        如果出现异常则执行的代码
"""


# 第2节 异常的传递性
"""
通过回溯异常的传递链，可以直接在异常的最顶级（最终）位置捕获异常，从而避免重复多次的捕获
"""

def fuc1():
    print("fuc1 start")
    i = 1 / 0
    print("fuc1 end")

def fuc2():
    print("fuc2 start")
    fuc1()
    print("fuc2 end")

def main():
    try:
        fuc2()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()


# 第3节 模块
"""
 - 模块：
    模块的本质是python代码文件，包含类、函数、变量等，可以通过导入直接被使用

 - 语法：
 
        [from 模块名] import [模块名|类名|变量名|函数名|*] [as 别名]
        
        from可以省略，直接import模块即可
        as别名可以省略
        通过“.”来确定层级关系
        模块的导入一般写在代码文件的开头位置
        
 - 自定义模块
 
    新建 自定义新python文件名（模块名）
    编写自定义功能
    from 自定义模块名 import 自定义功能名
    
    如果调用了不同模块文件中的同名功能，则只调用最后一个，前面的不会被执行
    
    if __name__ == "__main__":
    main()
    只有程序是直接执行的才会进入if内部，被导入时则无法进入
    
    __all__ = ["可被导入的功能名"]
    只作用于 import *
    手动导入指定功能仍有效
"""


# 第4节 包
"""
 - 包：
    用于包含多个模块文件的“文件夹”
    “_init_.py”文件控制着包的导入行为、
        在该文件内编写__all__变量控制可被导入的模块

 - 使用方法：
    新建包（自动创建“_init_.py”文件）
    新建包内模块python文件
    
 - 导入包：（导入层级）
 
    import 包名.模块名
    包名.模块名.目标
    
    from 包名 import 模块名
    模块名.目标
    
    from 包名.模块名 import 功能
    目标
    
 - 安装第三方包
    除python内置包外的第三方开发包，用于丰富编程功能和生态
"""


# 第5节 json文件
"""
 - json文件：
    一种通用数据文件（特殊类型的字符串），用于不同编程语言之间的数据传递
    通过json模块实现
    
 - 语法
    json与python数据类型的相互转化
    json本质上相当于python中一个单独的字典或者一个内部元素都是字典的列表
    python的字典和列表可以与json字符串进行无缝转换
"""

import json

# 准备列表，列表内每一个元素都是字典，将其转换为json
data_a = [
            {"AAA":"aaa"},
            {"BBB":"bbb"},
            {"CCC":"ccc"},
]
json_str = json.dumps(data_a, ensure_ascii=False) # ensure_ascii=False确保中文正常显示
print(json_str)

# 准备字典，将其转换为json
data_b = {"AAA":"aaa", "BBB":"bbb"}
json_str = json.dumps(data_b, ensure_ascii=False)
print(json_str)

# 将json字符串转换为python数据类型[{k: v,k: v},{k: v,k: v}]
s_a = '[{"AAA": "aaa"}, {"BBB": "bbb"}, {"CCC": "ccc"}]'
list_a = json.loads(s_a)
print(list_a)

# 将json字符串转换为python数据类型{k: v,k: v}
s_b = '{"AAA": "aaa", "BBB": "bbb"}'
dict_a = json.loads(s_b)
