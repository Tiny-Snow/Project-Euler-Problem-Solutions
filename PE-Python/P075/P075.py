# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 9 Mar 2021, 20:37
# Project Euler # 075 Singular integer right triangles

#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P075')[0] + 'Utility Class')

from prime_utility import *

limit = 1500000
prime_class = Prime(limit // 2)
prime_class._traverse()
prime_class._find_factor()
factor_list = prime_class._get_factor_list()

def set_list(origin_list):              # 列表去重
    if origin_list == []:
        return []
    new_list = []
    for i in range(len(origin_list)):
        if origin_list[i] not in new_list:
            new_list.append(origin_list[i])
    return new_list


num = 0
for p in range(12, limit, 2):
    solutions = []
    for k in factor_list[p // 2]:
        for a in factor_list[p // (2 * k)]:
            if a > (p // (2 * k)) ** 0.5:
                break
            b = p // (2 * k * a) - a
            if a > b and b > 0:
                solutions.append(list(sorted([k * (a ** 2 - b ** 2), 2 * k * a * b, k * (a ** 2 + b ** 2)])))
    solutions = set_list(solutions)
    if len(solutions) == 1:
        num += 1
print(num)