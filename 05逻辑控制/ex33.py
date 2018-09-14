# -*- coding: utf-8 -*-

# while循环

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1  # 没有这行代码的话，while循环条件将永远为True，就会变成死循环
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
