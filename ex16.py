# -*- coding: utf-8 -*-

# 读写文件
'''
与文件相关的命令（方法/函数）
• close：关闭文件。跟你的编辑中的“文件”-“保存”是一个意思。
• read：读取文件的内容。你可以把结果赋给一个变量
• readline：只读取文本文件中的一行。
• truncate：清空文件，请小心使用该命令。
• write('stuff')：将“stuff”写入文件。
• seek(0)：将读写位置移动到文件开头。
'''

from sys import argv
script, filename = argv
print(f"我们准备清空文件 {filename}")
print("如果你现在反悔了，请按Ctrl + C")
print("如果你想继续，请按 回车")

input("?")

print("正在打开文件...")
target = open(filename, 'w', encoding="utf-8")  # 加入mdoe='w'参数表示允许对文件进行写入操作。
print("正在清空文件。再见！")
target.truncate()  # 清空文件

print("现在请你输入3行内容：")

line1 = input("第一行：")
line2 = input("第二行：")
line3 = input("第三行：")

print("现在开始将这三行内容写入文件。")

target.write(line1)
target.write("\n")  # 写入一个换行
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("写入完毕，我们现在关闭文件。")
target.close()
