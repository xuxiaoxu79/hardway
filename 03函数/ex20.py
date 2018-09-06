# -*- coding: utf-8 -*-

# 函数和文件
# python ex20.py ex20_smaple.txt

from sys import argv
script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)  # 将指针指向文件的开始


def print_a_line(line_count, f):
    # 文件f会记录每次调用readline()后的读取位置，下次再调用时就会读取下一行了
    print(line_count, f.readline(), end="")


current_file = open(input_file, encoding="utf-8")

print("首先打印出整个文件内容：")
print_all(current_file)
print("现在我们将指针指向文件的首位置：")
rewind(current_file)
print("然后分别打印3行内容：")
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
