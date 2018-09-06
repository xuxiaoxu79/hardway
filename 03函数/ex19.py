# -*- coding: utf-8 -*-

# 函数和变量


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("我们直接给函数传递数字：")
cheese_and_crackers(20, 30)

print("也可以给它变量：")
amout_of_cheese = 10
amout_of_crackers = 50
cheese_and_crackers(amout_of_cheese, amout_of_crackers)

print("还可以给它数学表达式：")
cheese_and_crackers(10 + 20, 5 + 6)

print("甚至还可以将数学表达式和变量组合起来用：")
cheese_and_crackers(amout_of_cheese + 100, amout_of_crackers + 1000)
