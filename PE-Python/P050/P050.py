# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 22 Feb 2021, 19:17
# Project Euler # 050 Consecutive prime sum

#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P050')[0] + 'Utility Class')

from prime_utility import *
limit = 1000000
prime_class = Prime(limit)
prime_class._traverse()
prime_list = prime_class._get_prime_list()
prime_num = len(prime_list)

max_len = 0
ans_p = 0
for start in range(prime_num - 1):
    p_sum = prime_list[start]
    for end in range(start + 1, prime_num):
        p_sum += prime_list[end]
        if p_sum > limit:
            break
        if prime_class._is_prime(p_sum) == True and end - start > max_len:
            ans_p = p_sum
            max_len = end - start
print(ans_p)