# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 23 Feb 2021, 19:04
# Project Euler # 051 Prime digit replacements

#===================================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P051')[0] + 'Utility Class')

from prime_utility import *
limit = 1000000
prime_class = Prime(limit)
prime_class._traverse()

import itertools

def transfer(n: str, index_list: list):
    prime_num = 0
    min_p = limit
    for i in range(0, 10):
        p = n
        for index in index_list:
            p = p[:index] + str(i) + p[index + 1:]
        if len(str(int(p))) != len(str(int(n))):              # 排除位数改变的情况
            continue
        if prime_class._is_prime(int(p)) == True:
            prime_num += 1
            min_p = min(min_p, int(p))
    if prime_num >= 8:
        return min_p
    return False

def find_ans():
    for n in range(56003, limit):
        n_len = len(str(n))
        for index_num in range(1, n_len):
            for index_list in itertools.combinations([i for i in range(0, n_len - 1)], index_num):
                ans = transfer(str(n), list(index_list))
                if ans != False:
                    return ans

print(find_ans())