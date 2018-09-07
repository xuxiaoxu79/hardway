# -*- coding: utf-8 -*-

# 将ex25.py作为模块导入，然后调用它提供的一些函数

import ex25

print('** sentence = "All good things come to those who wait."')
sentence = "All good things come to those who wait."

print("** ex25.break_words(sentence)")
words = ex25.break_words(sentence)
print(words)

print("** ex25.sort_words(words)")
sorted_words = ex25.sort_words(words)
print(sorted_words)

print("** ex25.print_first_word(words)")
ex25.print_first_word(words)
print("** ex25.print_last_word(words)")
ex25.print_last_word(words)
print("** 删除了两个元素后的words")
print(words)

print("** ex25.print_first_word(sorted_words)")
ex25.print_first_word(sorted_words)
print("** ex25.print_last_word(sorted_words)")
ex25.print_last_word(sorted_words)
print("** 删除了两个元素后的sorted_words")
print(sorted_words)

print("** ex25.sort_sentence(sentence)")
sorted_words = ex25.sort_sentence(sentence)  # 变量重新赋值
print(sorted_words)

print("** ex25.print_first_and_last(sentence)")
ex25.print_first_and_last(sentence)
print("** ex25.print_first_and_last_sorted(sentence)")
ex25.print_first_and_last_sorted(sentence)
