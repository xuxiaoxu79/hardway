# -*- coding: utf-8 -*-

# 命名、变量、代码和函数


# 这个函数就像在脚本中接收argv一样
def print_two(*args):  # 在参数前面加了一个*号表示是可变参数，传入的参数个数是可变的。
    arg1, arg2 = args  # 将参数解包
    print(f"arg1: {arg1}, arg2: {arg2}")


# 好吧，* args实际上毫无意义，我们可以这样做
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# 这个函数只有一个参数
def print_one(arg1):
    print(f"arg1: {arg1}")


# 这个函数没有参数
def print_none():
    print("我什么都没得到。")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
