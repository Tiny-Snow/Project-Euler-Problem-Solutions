# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Thu, 4 Mar 2021, 15:06
# Project Euler # 069 Totient maximum

#===================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P069')[0] + 'Utility Class')

from prime_utility import *
limit = 1000000
prime_class = Prime(limit)
prime_class._traverse()
prime_class._find_factor()

max_euler = 0
for n in range(2, limit + 1):
    euler = prime_class._euler_func(n)
    if n / euler > max_euler:
        max_euler = n / euler
        ans_n = n
print(ans_n)