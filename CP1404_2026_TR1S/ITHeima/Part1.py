"""
CP1404 Final 2026 TR1S
"""

# 第一章 数据与运算基础

# 第1节 字面量
"""
写在代码中的固定的值
整数 int	10、-10
浮点数 float	13.14、-13.14
字符串 string	“任意数量的字符 ”
"""

# 第2节 注释
# 单行注释：# 开头
"""
多行注释：三引号
"""

# 第3节 变量
# 变量名 = 变量值
money = 50
print("钱包现有：",money,"元")
# 花了10元
money = money - 10
print("还剩余：",money,"元")

# 第4节 数据类型
# 查看数据类型
abc = 123
type(abc)
print(type(abc))

# 第5节 数据类型转换
"""
int(x) - 将x转化为一个整数
float(x) - ……
string(x) - ……
遵循数据类型规则
"""

# 第6节 标识符
"""
变量、类、方法等的名字
英文、中文（不推荐）、数字、下划线
数字不可以用在开头
区分大小写
不可使用关键字
"""
"""
变量的命名规范：
见名知意
下划线命名 first_number
英文全小写
"""

#第7节 运算符
"""
算术运算符：
+	加
-	减
*	乘
/	除
//	取整数
%	取余数
**	指数
"""
"""
赋值运算符：
=	赋值
+=	a = a + 1 等同于 a += 1
-=	…
*=	…
/=	…
%=	…
**=	…
//=	…
"""

# 第8节 字符串定义的三种方式
# 单引号定义：name = 'abcd'
# 双引号定义：name = "abcd"
# 三引号定义：name = """abcd""" - 同多行注释，可多行

# 第9节 字符串的拼接
name = "abc"
tel = 123456
print("My name is " + name)
print("My tel number is " + str(tel))

# 第10节 字符串格式化
"""
%s：先占一个位，后面有一个数据会以字符串的形式放进来
%d：…整数…
%f：…浮点数…
"""
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，毕业平均工资：%s" %(class_num, avg_salary)
#多个变量占位，要用括号括起来，并按照占位的顺序填入

# 第11节 字符串格式化的精度控制
"""
%m.n
m，控制宽度，不小于数字自身
.n：控制小数位数
%5d %5.2f %.2f
"""
num1 = 11
num2 = 11.345
print("数字11.345，宽度限制7，小数精度2，结果是：%7.2f" % num1)

# 第11节 字符串格式化的精度控制2
# 快速格式化:不限数据类型、不做精度控制,使用大括号{}
name_a = "abc"
year = 2004
print(f"My name is {name_a},my birth year is {year}")

# 第12节 表达式（一条具有明确结果的代码语句）格式化
print(f"1+1的结果是：{1+1}")
print("1+1的结果是:%d"%(1+1))

# 练习题
company_name = "传智播客"
stock_code = "003032" # 003032不符合数字规则，所以使用字符串定义
stock_price = 19.99
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司{company_name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数是：%f,经过%d天的增长后，股价达到了%.2f" %(stock_price_daily_growth_factor, growth_days ,(19.99 * stock_price_daily_growth_factor ** growth_days)))

# 第13节 数据输入
"""
数据输出：print
数据输入：input 输入数据均默认当作字符串，其余类型需要单独定义
"""
user_password = int(input("Your Password:"))
print(f"Your Password is {user_password}")
