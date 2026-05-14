"""
CP1404 Final 2026 TR1S
"""

# 第五章 数据容器

# 第1节 列表 list
"""
特点：
可容纳多个元素、可容纳不同的元素类型、元素是有序存储的（下标序号）、允许重复数据存在、可以修改、列表内可以嵌套列表

定义列表字面量：
[元素0，元素1，元素2，...]

定义列表变量：
变量名 = [元素0，元素1，元素2，...]

定义空列表：
变量名 = []
变量名 = list（）

列表的下标索引（定位、取用列表内的某个元素）：
语法：列表名[下标]

顺序：从左至右，由0开始编号；从右至左，由-1开始编号
[元素0，元素1，元素2，...]
[...，元素-3，元素-2，元素-1]

嵌套列表顺序示例：
[[元素0，元素1],[元素0，元素1]]
取出外层列表第二个元素内的元素0：
外层列表名[1][0]

"""

my_list_a = ["aaa","bbb","ccc","ddd","eee"]

print(my_list_a[0])
print(my_list_a[1])
print(my_list_a[2])
print(my_list_a[3])
print(my_list_a[4])

print(my_list_a[-1])
print(my_list_a[-2])
print(my_list_a[-3])
print(my_list_a[-4])
print(my_list_a[-5])

my_list_b = [[1,2,3],[4,5,6],[7,8,9]]

print(my_list_b[0][0])
print(my_list_b[1][1])
print(my_list_b[2][2])

"""
列表的方法：
 - 查找指定元素在列表的下标索引值：
    列表名.index（元素）
    如果找不到会报错
 - 修改特定位置（索引）的元素值：
    列表名[下标] = 值
    正向反向均可
 - 在特定位置插入元素：
    列表名.insert（下标，元素）
    插入下标为新元素插入后的下标
 - 追加单个元素至列表尾部：
    列表名.append（元素）
 - 追加批量元素（其它数据容器中的元素）至列表尾部：
    列表.extend（其它数据容器）
 - 删除元素：
    del 列表名[下标] - 仅删除
    列表名.pop（下标） - 删除后将被删除元素作为返回值得到：变量名 = 列表名.pop（下标）
 - 删除某元素（内容）在列表中从前至后的第一个匹配项：
    列表名.remove（元素）
 - 清空列表
    列表名.clear（）
 - 统计某元素在列表内的数量：
    列表名.count（元素）
 - 统计类表中所有元素的数量：
    len（列表名）
"""

my_list_c = [21, 25, 21, 23, 22, 20]

my_list_c.append(31)
my_list_c.extend([29,33,30])
print(my_list_c)
data_a = my_list_c[0]
print(data_a)
data_b = my_list_c[-1]
print(data_b)
index_a = my_list_c.index(31)
print(index_a)

"""
列表的循环遍历（从列表中依次取出元素进行操作）

while循环

index = 0
while index < len（列表名）
    元素 = 列表[index]
    对元素进行处理
    index += 1

for循环

for 临时变量 in 数据容器：
    对临时变量进行处理
"""

my_list_d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_e = []
my_list_f = []

index_b = 0
while index_b < len(my_list_d):
    element_a =  my_list_d[index_b]
    if element_a % 2 == 0:
        my_list_e.append(element_a)
    index_b += 1
print(my_list_e)

for element_b in my_list_e:
    if element_b % 2 == 0:
        my_list_f.append(element_b)
print(my_list_f)


# 第2节 元组 tuple
"""
元组同列表一样，都可以封装多个、有序存储的、允许重复的、不同类型的元素在内；元组也支持嵌套。
但元组一旦定义完成，就不可修改。
但如果元组内嵌套了列表，该列表内的元素是可以被修改的。

定义元组字面量：
（元素，元素，元素，...）

定义元组变量：
变量名 = （元素，元素，元素，...）

定义空元组：
变量名 = （）
变量名 = tuple（）

如果定义仅有一个元素的元组，该数据后要添加逗号
（元素，）
"""

"""
元组的相关操作：
元组的以下操作、元素下标均与列表相同；元组没有修改操作
 - 查找元组中某个元素的对应下标：index（）
 - 统计某个元素在当前元组出现的次数：count（）
 - 统计元组内元素的个数：len（元组名）
"""

"""
元组的遍历：
while for
"""

my_tuple_a = ('Jay Zhou', 11, ['football', 'music'])

age_a = my_tuple_a.index(11)
print(age_a)

name_a = my_tuple_a[0] # 访问元组内的元素的下标时仍需要用[] / 任何下标的访问都是[]
print(name_a)

del my_tuple_a[2][0]
# 实际是修改元组内嵌套的列表：my_tuple_a[2]为一个整体，表示元组内嵌套的列表；[0]表示列表中元素的对应下标
print(my_tuple_a)

my_tuple_a[2].append('coding') # 同上，修改元组内嵌套的列表
print(my_tuple_a)

# 第3节 字符串 string
"""
字符串可以存放任意数量、长度任意、允许重复的字符，如“itheima”
字符串同样是无法修改的数据容器。

字符串的相关操作：
 - 字符串同样支持下正反向下标索引：字符串名[下标]
 - 查找字符串中元素的下标：字符串名.index（元素）
 - 字符串的替换（不是修改，而是得到一个新的字符串，需要定义新字符串进行接收）：字符串名.replace（待替换字符串，新字符串）
 - 字符串的分割（按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中，需要定义新列表进行接收）：字符串名.split（分隔符字符串）
 - 字符串的规整操作1（去除前后空格）：字符串名.strip（）
 - 字符串的规整操作2（去除前后指定字符串）：字符串名.strip（待去除字符串）
 - 统计字符串中某字符串的出现次数：字符串名.count（字符串）
 - 统计字符串的长度：len（字符串名）

字符串也可使用while和for循环进行遍历
"""

my_str_a = "itheima itcast boxuegu"

count_it = my_str_a.count("it")
print(count_it)

new_my_str_a = my_str_a.replace(" ", "|") # 实际是得到新的字符串，需要定义新的字符串名称去接收
print(new_my_str_a)

new_list = new_my_str_a.split("|")
print(new_list)


# 第4节 序列
"""
序列是指：内容连续、有序、可使用下标索引的一类数据容器；
列表、元组、字符串，均可以被视为序列

序列的常用操作 - 切片：
从序列中，从指定位置开始，依次取出元素，到指定位置结束，得到一个新序列

语法：序列名[起始下标：结束下标：步长]
 - 起始下标表示从何处开始；如果留空，视作从头开始
 - 结束下标（不含）表示至何处结束；如果留空，视作截取至结尾
 - 步长表示依次截取元素的间隔
    步长1表示，一个个截取元素
    步长2表示，每次跳过1个元素截取
    步长N表示，每次跳过N-1个元素截取
    步长为负数表示，反向截取；此时起始下标与结束下标也需要使用反向标记
    
对序列进行的任何操作都不会影响原序列，而是会得到一个新的序列（需要定义新序列进行接收）
"""

my_str_b = "9876543210"

new_my_str_b = my_str_b[-1::-1]
new2_my_str_b = new_my_str_b[1:6:1]

print(new2_my_str_b)


# 第5节 集合 set
"""
集合：
 - 可容纳多个、不同类型的数据
 - 不支持元素的重复
 - 内容无序、不支持下标索引（不能使用while遍历）；集合自带去重功能
 - 可以修改

定义集合字面量：
{元素，元素，元素，...}
定义集合变量：
变量名 = {元素，元素，元素，...}
定义空集合：
变量名 = set（） 仅此一个！

集合的常用操作：
 - 添加元素：集合名.add（元素）
 - 移除元素：集合名.remove（元素）
 - 随机取出元素（有返回值，需定义新变量接收）：集合名.pop（元素）
 - 清空集合：集合名.clear()
 - 取两个集合的差集（集合1有而集合2没有的）：集合1.different（集合2）
    得到一个新集合（需定义新集合接收），原集合1、2不变
 - 消除两个集合的差集：集合1.difference.update（集合2）
    对比集合1和集合2，在集合1内，删除和集合2相同的元素
    集合1被修改，集合2不变
 - 两个集合合并为一个：集合1.union（集合2）
    得到新集合，原集合1和集合2不变
 - 统计集合元素数量：len（集合名）
 
集合的遍历：
由于集合不支持下标索引，所以不能使用while循环进行遍历
可以使用for循环进行遍历
"""

my_list_g = ['a', 'b', 'a', 'b', 'c', 'd', 'c', 'd', 'e']
my_set_a = set()

for item in my_list_g:
    my_set_a.add(item)
print(my_set_a)


# 第6节 字典 dict
"""
通过字典，实现用Key取出对应的Value的操作
字典不可使用下标索引，唯一的索引是key值
字典存储的元素是一个个键值对
不允许Key重复

定义字典字面量：
{key:value,key:value,key:value,...}
定义字典变量：
字典名 = {key:value,key:value,key:value,...}
定义空字典：
字典名 = dict（）
字典名 = {}

字典的相关操作：
 - 从字典中基于key获取value：字典名[key]

字典的嵌套：
字典名 = {key1：{key1-1，value1-1：key1-2，value1-2}，key2：{key2-1，value2-1：key2-2，value2-2}，...}

从嵌套字典内获取数据：
字典名[key1][key1-1]

字典的常用操作：
 - 新增元素/更新元素：字典名[key] = value （如果key不存在，则为新增）
 - 删除元素：字典名.pop（key）
 - 清空元素：字典名.clear（）
 - 获取全部key：字典名.keys（）
    用于for循环遍历字典
 - 统计字典内元素数量：len（字典名）
"""

employee_dict = {
    "王力宏":{"部门":"科技部","工资":3000,"级别":1},
    "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
    "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
    "张学友":{"部门":"科技部","工资":4000,"级别":1},
    "刘德华":{"部门":"市场部","工资":6000,"级别":2},
}

print(f"全体员工当前信息如下：{employee_dict}")

for employee_name in employee_dict:
    if employee_dict[employee_name]["级别"] == 1:
        employee_info_dict = employee_dict[employee_name]
        employee_info_dict["级别"] = 2
        employee_info_dict["工资"] += 1000
        employee_dict[employee_name] = employee_info_dict

print(f"全体级别为1的员工完成升级加薪操作，操作后：{employee_dict}")


# 第7节 数据容器的通用操作以及拓展

"""
 - 遍历
    五类数据容器均支持for循环遍历
    列表、元组、字符串支持下标索引，所以可以使用while循环遍历
    集合、字典不支持下标索引，不能使用while循环遍历

 - 通用统计功能
    统计容器中元素的个数：len（容器）
    统计容器中的最大元素：max（容器）
    统计容器中的最小元素：min（容器）
    
 - 通用类型转换
    将给定容器转换为列表：list（容器）
    将给定容器转换为字符串：str（容器）
    将给定容器转换为元组：tuple（容器）
    
 - 进行容器的排序
    sorted（序列，[reverse = True]）
    [reverse = True]表示降序排序，如果不加则表示升序排序
    
 - 字符串的大小比较
    基于ASCII码表的字符码值进行比较
    从头至尾，一位位进行比较；只要其中一位大，后面就无需比较了
"""
