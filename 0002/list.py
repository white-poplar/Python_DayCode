#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-08 09:11:30
# @Author  : poplar. (BYH5566@gmail.com)
# @Link    : https://white-poplar.github.io
# @Version : $Id$


_list = [2, 5, 8, 10, 3]

a = [2]
b = [3]
c = [6, 8]
d = [2, 7]

for i in range(0, len(_list), 2):
    print(_list[i:i + 2])

# _result = [l for l in [a, b, c, d] if len(l) > 0]
_result = [l for l in [a, b, c, d] if l]

print(_result)
# print(type(range(1,10)))
# print(list(range(1,10)))

################################################################################

_result = [_list[i:i + 2] for i in range(0, len(_list), 2)]
print(_result)


_result = lambda _list:map(lambda b:_list[b:b+2],range(0,len(_list),2))
print(_result)
