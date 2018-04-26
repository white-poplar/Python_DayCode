#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-21 10:16:20
# @Author  : poplar. (BYH5566@gmail.com)
# @Link    : https://white-poplar.github.io
# @Version : $Id$

import os


# 加载文件
def load_file(dirpath, filename):
    file = os.path.join(dirpath, filename)
    if not os.path.exists(file):
        print('%s 文件未找到！' % (file))
        return None

    return read_file_line(file)


# 读取文件
def read_file(file):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()
        print(file)
        print(data)
    return data


# 读取文件
def read_file_line(file):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.readlines()
        # print(file)
        # print(data)
    return data


# 获取单词
def get_word_list(readlines):
    word = []
    for line in readlines:
        line = line.strip()  # 把末尾的'\n'删掉
        line = line.replace('“', '').replace(
            '”', '').replace(',', '').replace('.', '')
        _temp = line.split(' ')
        # print(_temp)
        word.extend(_temp)
    return word


# 清理重复
def get_clean_word(words):
    # print(words)
    wokey = {}
    wokey = wokey.fromkeys(words)  # 键值去重
    word_list = list(wokey.keys())  # 键
    # print(word_list)

    # 出现次数
    for i in word_list:
        wokey[i] = words.count(i)
    return wokey


# 排序
def sort_word(wokey):
    if ' ' in wokey.keys():
        del wokey[' ']
    if '' in wokey.keys():
        del wokey['']

    result_wokey = {}
    result_wokey = sorted(wokey.items(), key=lambda x: x[1], reverse=True)
    return result_wokey


# 读取文章 - 返回单词字典
def get_word_count(dirpath, filename):
    _content = load_file('.', 'post.txt')
    _wokey = sort_word(get_clean_word(get_word_list(_content)))
    # print(_wokey)
    _wokey = dict(_wokey)
    return _wokey


# mian
def main():
    _wokey = get_word_count('.', 'post.txt')
    print(_wokey)

    i = 0
    for x, y in _wokey.items():
        if i < 10:
            print('word => ', '{}'.format(x), ' && ',
                  'count => ', '{}'.format(y))

            print('word => {} && count => {} '.format((x, y)))
            i = i + 1
            continue
        else:
            break


if __name__ == '__main__':
    main()
