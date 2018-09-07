# -*- coding: utf-8 -*-

'''更多更多的练习'''  # 这是文档注释


def break_words(stuff):
    '''这个函数会为我们拆分单词'''  # 这是函数注释
    words = stuff.split(' ')
    return words


def sort_words(words):
    '''对单词列表进行排序'''
    return sorted(words)


def print_first_word(words):
    '''删除并打印列表中的第一个单词'''
    word = words.pop(0)
    print(word)


def print_last_word(words):
    '''删除并打印列表中的最后一个单词'''
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    '''输入一个完整的句子，返回拆分并进行排序后的列表'''
    words = break_words(sentence)  # 调用拆分单词的函数
    return sort_words(words)  # 调用排序的函数


def print_first_and_last(sentence):
    '''打印列表中的第一个单词和最后一个单词'''
    words = break_words(sentence)  # 调用拆分单词的函数
    print_first_word(words)  # 调用删除并打印列表中第一个单词的函数
    print_last_word(words)  # 调用删除并打印列表中最后一个单词的函数


def print_first_and_last_sorted(sentence):
    '''打印拆分并排序后的第一个单词和最后一个单词'''
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
