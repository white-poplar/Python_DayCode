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
import mysql.connector


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


# mysql
def save_mysql(list=None):
    conn = mysql.connector.connect(
        host='127.0.0.1', port=3306, user='root', password='', database='daycode')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE `daycode`.`coupon` ( `Id` BIGINT NOT NULL AUTO_INCREMENT COMMENT \'标识\' , `Code` VARCHAR(200) NOT NULL COMMENT \'优惠码\' , PRIMARY KEY (`Id`)) ENGINE = MyISAM COMMENT = \'优惠码表\';')
    cursor.execute('insert into coupon(Code) values (%s)', ['5566'])
    conn.commit()
    cursor.close()


if __name__ == '__main__':
    get_code_list()
    print(resultList)

    # show variables like '%char%'; --mysql 编码

    # pip install mysql-connector-python --allow-external mysql-connector-python --驱动

    # pip install mysql-connector --驱动

    save_mysql()
