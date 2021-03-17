# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 6 Mar 2021, 19:42
# Project Euler # 070 Totient permutation

#===================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P070')[0] + 'Utility Class')

from prime_utility import *
limit = 10 ** 7
prime_class = Prime(limit)
prime_class._traverse()
prime_class._find_factor()

min_ratio = limit
ans_n = 0
for n in range(2, limit):
    euler = prime_class._euler_func(n)
    if len(str(euler)) != len(str(n)):
        continue
    if sorted(str(euler)) == sorted(str(n)):
        if min_ratio > n / euler:
            min_ratio = n / euler
            ans_n = n
print(ans_n)