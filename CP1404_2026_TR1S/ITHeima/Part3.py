"""
CP1404 Final 2026 TR1S
"""

# 第三章 循环

# 第1节 while循环
"""
while 条件：
    条件满足时，做事情1
    条件满足时，做事情2
    条件满足时，做事情3
    ...
只要条件满足，就会无限循环执行；注意设置循环终止的条件，如i+=1，i<100
"""
num1 = 1
sum1 = 0

while num1 <= 100:
    sum1 += num1
    num1 += 1

print(sum1)

# 第2节 while循环应用
"""
import random
num2 = random.randint(1,100)
count1 = 0

flag = True
while flag:
    guess_number_a = int(input("Enter a number (from 1 to 100): "))
    count1 += 1
    if guess_number_a == num2:
        flag = False
        print("You are right!")
    else:
        if guess_number_a > num2:
            print("You guessed too high!")
        else:
            print("You guessed too low!")

print(f"You guessed a total of {count1} times.")
"""

# 第3节 while循环的嵌套应用 - 输出99乘法表
print("Hello",end='') # 输出后不换行
print("World")

print("Hello\t\tWorld")
print("language\tbest") #制表符，多行字符串对齐;上下字符串不能相差太长，否则需要多个

i = 1
while i <= 9:

    j = 1
    while j <= i:
        print(f"{j} * {i} = {i * j}", end=' ')
        j += 1

    i += 1
    print() # 输出一个换行 或使用\n换行符

# 第4节 for循环
"""
轮询机制
for 临时变量 in 待处理数据集（序列类型：字符串、列表、元组，等）：
    循环满足条件时执行的代码
将待处理数据集内的数据依次取出，赋予临时变量进行处理
不能定义循环条件，只能被动取出数据进行处理
"""

name_b = "itheima is a brand of itcast"
k_a = 0

for i_a in name_b:
    if i_a == "a":
        k_a += 1

print(f"{name_b} 中共有 {k_a} 个字母a.")

# 第5节 for循环中的range语句
range(5) # [0,1,2,3,4] 不含结束数字本身
range(5,10) # [5,6,7,8,9] 不含结束数字本身
range(5,10,2) # [5,7,9] 步长为2（从起始数字开始，每隔2个数字取一个值，不含结束数字本身）

num2 = 100
k_b = 0

for i_b in range(1,num2):
    if i_b % 2 == 0:
        k_b += 1

print(f"从1至{num2}共有{k_b}个偶数")

# 第6节 for循环的变量作用域
"""
规范：
for循环内的临时变量，应当只在循环内部生效，而不应使用到循环外部
"""
k_c = 0 # 如果确需在循环外部访问临时变量，应在循环之前提前定义
for k_c in range(5):
    print(k_c)
print(k_c) # k_c作为循环内部的临时变量，规范上不应在循环外部使用

# 第7节 for循环的应用 - 打印99乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {j * i}", end=' ')

    print()

# 第8节 continue和break
"""
continue：中断本次循环，直接进入下一次
break：直接结束循环
在嵌套循环中，仅作用于所在循环，不作用于上层循环
"""

# 第9节 循环综合应用

account_balance = 10000
salary_per_employee = 1000
num_of_employees = 20

for employee_id in range(1,num_of_employees + 1):

    import random
    perf_score = random.randint(1, 10)

    if perf_score < 5:
        print(f"员工{employee_id}，绩效分{perf_score}，低于5，不发工资，下一位。")
        continue

    if account_balance >= salary_per_employee:
        account_balance -= salary_per_employee
        print(f"向员工{employee_id}发放工资{salary_per_employee}元，账户余额还剩余{account_balance}元。")
    else:
        print(f"余额不足，当前余额{account_balance}元，不足以发工资。")
        break
