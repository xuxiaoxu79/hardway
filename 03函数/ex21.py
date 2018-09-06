# -*- coding: utf-8 -*-

# 函数可以返回某些东西


def add(a, b):
    print(f"加法 {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"减法 {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"乘法 {a} * {b}")
    return a * b


def divide(a, b):
    print(f"除法 {a} / {b}")
    return a / b


print("我们用函数来进行一些数学运算：")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("自定义一个公式：")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("结果变成了：", what)
