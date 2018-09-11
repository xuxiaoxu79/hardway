# -*- coding: utf-8 -*-

# 作出决定

print("""你进入一个有两扇门的黑暗房间。
你想经过1号门还是2号门？""")

door = input("> ")

if door == "1":
    print("这里有一只巨熊在吃芝士蛋糕。")
    print("你该怎么办？")
    print("1. 拿走蛋糕。")
    print("2. 对着巨熊尖叫。")

    bear = input("> ")

    if bear == "1":
        print("熊吃了你的脸。 游戏结束！")
    elif bear == "2":
        print("熊吃了你的腿。 游戏结束！")
    else:
        print(f"好吧，选择 {bear} 可能会更好。")
        print("熊跑了。")
elif door == "2":
    print("你通过邪神的眼睛望向无尽的深渊。")
    print("1. 蓝莓。")
    print("2. 黄色夹克衫。")
    print("3. 了解左轮手枪的旋律。")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("你的身体依靠果冻的力量生存。")
        print("游戏结束！")
    else:
        print("精神错乱使你的眼睛腐烂成一堆泥土。")
        print("游戏结束！")
else:
    print("你四处乱窜，摔倒在地上，死了。游戏结束")
