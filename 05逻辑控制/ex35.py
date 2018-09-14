# -*- coding: utf-8 -*-

# 分支和函数

from sys import exit


def gold_room():
    print("新的房间里面放满了黄金，你想要拿多少？")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("伙计，去学习一下如何输入数字再来吧。")

    if how_much < 50:
        print("很好，你不贪心，你赢了！")
        exit(0)
    else:
        dead("你这个贪婪的小人。")


def bear_room():
    print("这里有一只熊。")
    print("拿着一罐蜂蜜。")
    print("胖熊挡在另一扇门前面。")
    print("你要怎么做才能让熊走开？")
    bear_moved = False

    while True:
        choice = input("1:拿走蜂蜜 2:刺激胖熊 3:打开门 > ")
        if choice == "1":
            dead("熊扑向你然后扇了你一记熊掌。")
        elif choice == "2" and not bear_moved:
            print("熊离开了那扇门。")
            print("你现在可以进去了。")
            bear_moved = True
        elif choice == "2" and bear_moved:
            dead("熊生气了，嚼断了你的腿。")
        elif choice == "3" and bear_moved:
            gold_room()
        else:
            print("我不知道你想干什么。")


def cthulhu_romm():
    print("在这里，你看到了邪恶的克苏鲁。")
    print("他那恐怖的眼睛盯着你，你快要疯了。")
    print("你想要逃命还是让他吃了你的脑子？")
    choice = input("1:逃命 2:献上脑子 > ")
    if "1" in choice:
        start()  # 游戏重新开始
    elif "2" in choice:
        dead("脑子真好吃。")
    else:
        cthulhu_romm()  # 再次执行该函数


def dead(why):
    print(why, "游戏结束！")
    exit(0)


def start():
    print("你来到了一间漆黑的房间。")
    print("在你的左边和右边分别有一扇门。")
    print("你想打开哪扇门？")
    choice = input("1:左边 2:右边 > ")
    if choice == "1":
        bear_room()
    elif choice == "2":
        cthulhu_romm()
    else:
        dead("你在房间里到处乱蹿，直到饿死为止。")


start()
