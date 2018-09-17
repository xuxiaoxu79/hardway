# -*- coding: utf-8 -*-

# 学习面向对象术语
# python ex41.py english 运行脚本，就可以进行反向练习了。

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# 代码片段和语言描述
PHRASES = {
    "class %%%(%%%):":
    "创建一个叫 %%% 的类，它是 %%% 的一种。",
    "class %%%(object):\n\tdef __int__(self, ***)":
    "类 %%% 有一个 __int__，它接收 self 和 *** 作为参数。",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "类 %%% 有一个名为 *** 的函数，它接收 self 和 @@@ 作为参数。",
    "*** = %%%()":
    "将 *** 设为类 %%% 的一个实例。",
    "***.***(@@@)":
    "从 *** 中找到 *** 函数，并使用 self 和 @@@ 参数调用它。",
    "***.*** = '***'":
    "从 *** 中获取 *** 属性，并将其设为 ***。"
}

# 如果第2个参数为english，则先出语言描述，然后再出代码片段
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# 从网站上下载文本并其放入WORDS列表中
for word in urlopen(WORD_URL).readlines():
    # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    '''
    将代码片段和语言描述中的特殊符号替换成随机的单词
        snippet: 代码片段
        phrase: 语言描述
    '''
    # capitalize() 将字符串的第一个字母变成大写,其他字母变小写。
    # random.sample() 从指定序列中随机获取指定长度的片断。
    # count() 方法用于统计字符串里某个字符出现的次数。
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    # 函数参数随机生成1到3个
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)  # random.randint(a,b)：用于生成一个指定范围内的整数。生成的随机数n：a<=n<=b
        # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:  # 在一个for循环中遍历两个变量
        result = sentence[:]  # [:]可以原样复制一个list

        # 替换类名称
        for word in class_names:
            # replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
            result = result.replace("%%%", word, 1)

        # 替换其它名称
        for word in other_names:
            result = result.replace("***", word, 1)

        # 替换参数名称
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


try:
    while True:
        snippets = list(PHRASES.keys())  # 将PHRASES字典中的所有key组成一个新的列表
        # 注意：shuffle()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
        random.shuffle(snippets)  # 将列表的所有元素随机排序。
        # 开始提问
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print(question)
            str_answer = input("请回答，退出请按q > ")
            if str_answer == 'q':
                exit(0)
            else:
                print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
