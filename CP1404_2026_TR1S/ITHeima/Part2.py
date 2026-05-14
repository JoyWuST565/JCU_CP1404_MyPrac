"""
CP1404 Final 2026 TR1S
"""

# 第二章 判断

# 第1节 布尔类型和比较运算符
"""
布尔类型bool：
True
False
"""
"""
比较运算符：
==   判断是否相等
!=   判断是否不相等
>    判断运算符左侧是否大于右侧
<    判断运算符左侧是否小于右侧
>=   判断运算符左侧是否大于等于右侧
<=   判断运算符左侧是否小于等于右侧
"""

# 第2节 if elif else 综合判断语句
"""
if 条件1：
    满足条件1应该做的事情
elif 条件2：
    满足条件2应该做的事情
...
elif 条件n：
    满足条件n应该做的事情
else:
    以上条件都不满足应该做的事情
"""
player_age = int(input("Enter your age: "))
if player_age > 18: # 冒号不要忘记
    print("You are an adult.") # 缩进不要忘记
elif player_age == 18:
    print("You will be an adult this year.")
else:  # 与if同级，不缩进
    print("You are a child.") # 缩进不要忘记

# 第3节 判断语句的综合使用
import random
num = random.randint(1,10)

user_guess_num = int(input("Enter your guess (from 1 to 10): "))

if user_guess_num == num:
    print("You guessed right!")
else:
    if user_guess_num > num:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")

    user_guess_num = int(input("Enter your guess (from 1 to 10): "))

    if user_guess_num == num:
        print("You guessed right!")
    else:
        if user_guess_num > num:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

        user_guess_num = int(input("Enter your guess (from 1 to 10): "))

        if user_guess_num == num:
            print("You guessed right!")
        else:
            print("Game Over")
