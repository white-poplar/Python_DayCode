#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-21 10:16:20
# @Author  : poplar. (BYH5566@gmail.com)
# @Link    : https://white-poplar.github.io
# @Version : $Id$

import os
import glob
import random
import string
import redis



# 26 个大写字母
def create_uppercase():
    return string.ascii_uppercase


# 26 个小写字母
def create_lowercase():
    return string.ascii_lowercase


# 小写 + 大写
def create_case():
    return string.ascii_letters


# 10 数字
def create_number():
    return string.digits


# 字母 + 数字
def get_case_num():
    return create_lowercase() + create_number() + create_uppercase()


# 获取优惠码
def get_code():
    code = ''
    base_code = get_case_num()
    for x in range(16):
        code = code + random.choice(base_code)

    return code


resultList = []
COUNT = 10


# 不重复优惠码列表
def get_code_list(counter=1):
    if counter > COUNT:
        return None
    temp_code = get_code()
    if temp_code not in resultList:
        resultList.append(temp_code)
        counter += 1
    get_code_list(counter)


# redis
def save_redis(code_list=None):
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)

    # r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    
    r.set('code',code_list)
    # print(r['code'])
    print('redis_data', r.get('code'))
    print(type(r.get('code')))


if __name__ == '__main__':
    get_code_list()
    print('code_list', resultList)

    # pip install redis --驱动

    save_redis(resultList)
