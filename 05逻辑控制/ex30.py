# -*- coding: utf-8 -*-

# else 和 if
'''
* 如果多个elif块都是True, Python会如何处理？
  Python只会运行它遇到的是True的第一个块，所有只有第一个为True的块会运行。
'''

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
