# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 22 Feb 2021, 14:59
# Project Euler # 047 Distinct primes factors

#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P047')[0] + 'Utility Class')

from prime_utility import *
limit = 200000
prime_class = Prime(limit)
prime_class._traverse()
prime_class._find_factor()
prime_factor_list = prime_class._get_prime_factor_list()

for n in range(647, limit):
    flag = True
    for i in range(4):
        if len(prime_factor_list[n + i]) != 4:
            flag = False
            break
    if flag == True:
        print(n)
        break