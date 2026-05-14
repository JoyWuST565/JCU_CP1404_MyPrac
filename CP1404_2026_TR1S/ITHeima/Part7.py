"""
CP1404 Final 2026 TR1S
"""

# 第七章 文件操作

# 第1节 文件编码概念
"""
文件编码技术：
文件内容与二进制如何相互转化的规定
通用UTF-8
"""

# 第2节 文件的读取操作
"""
 - 打开文件
    文件对象 = open（name，mode，encoding）
        name：要打开的目标文件的文件名的字符串（可以包含文件的具体路径）
        mode：打开文件的模式（只读、写入、追加等）
            “r”：只读；默认模式，文件的指针将会放在开头
            “w”：写入；打开一个文件并从开头开始编辑，原有内容会被删除；如果文件不存在，则创建新文件
            “a”：追加：打开一个文件并在已有内容之后写入新内容；如果文件不存在，则创建新文件
        encoding：编码格式（推荐使用UTF-8）
    f = open（“python.txt”，“r”，encoding = “UTF-8”）
    
 - 只读操作相关方法
    文件对象.read（num）
        num表示要从文件中读取的数据的长度，单位是字节；如果没有传入num，则表示读取文件中的全部数据
        
    文件对象.readlines（）
        可以按照行的方式将文件中的全部内容进行一次性读取，并且返回的是一个列表，其中每一行的数据作为一个元素
        
    文件对象.readline（）
        一次读取文件中一行的内容，并将该行的内容封装进一个列表
        
    for循环读取文件行
        for line in 文件对象：
            print（line）
        
    注意：如果在同一程序中，对同一文件多次调用只读操作相关函数，则读取时会上一次调用的末尾开始读取
    
    关闭文件，解除占用
        文件对象.close（）
        
    with open （name，mode，encoding） as 文件对象：
    可在操作后自动关闭文件并解除占用

"""

count = 0

with open("C:/Users/MSI/Desktop/CP1404 Final/test.txt","r",encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            if word == "itheima":
                count += 1

print(count)


# 第3节 文件的写入操作
"""
 - 首先以写入模式（“w”）打开文件
 - 文件写入：文件对象.write（写入内容）
 - 内容刷新：文件对象.flush（）
    直接调用write时，内容并未真正写入文件，而是会积攒在程序的内存中，称为缓冲区
    当调用flush时，内容才会真正写入文件；目的是避免频繁操作硬盘，导致效率下降
    close（）方法带有flush方法的功能
"""

# 第4节 文件的追加操作
"""
 - 打开文件时，“a”模式表示追加操作
 - 进行追加写入操作
 - 写入会紧接原有内容写入，注意使用\n换行符
 - 更新并关闭文件
"""

# 第5节 文件操作的综合内容

fr = open("C:/Users/MSI/Desktop/CP1404 Final/bill.txt","r",encoding="utf-8")
fw = open("C:/Users/MSI/Desktop/CP1404 Final/bill.txt.bak","w",encoding="utf-8")

for line in fr:
    line = line.strip()
    if line.split("，")[4] == "测试":
        continue
    fw.write(line)
    fw.write("\n")

fr.close()
fw.close()
