# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sun, 7 Mar 2021, 14:03
# Project Euler # 072 Counting fractions

#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P072')[0] + 'Utility Class')

from prime_utility import *
limit = 10 ** 6
prime_class = Prime(limit)
prime_class._traverse()
prime_class._find_factor()

num = 0
for d in range(2, limit + 1):
    num += prime_class._euler_func(d)
print(num)