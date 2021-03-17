# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 20 Feb 2021, 23:56
# Project Euler # 037 Truncatable primes

#================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P037')[0] + 'Utility Class')

from prime_utility import *

limit = 1000000
prime_sum = 0
prime_num = 0
prime_class = Prime(limit)
prime_class._traverse()
prime_list = prime_class._get_prime_list()[4: ]

for p in prime_list:
    if prime_num == 11:
        break
    flag = True
    l = len(str(p))
    for i in range(1, l):
        if prime_class._is_prime(int(str(p)[i: l])) == False:
            flag = False
            break
        if prime_class._is_prime(int(str(p)[: -i])) == False:
            flag = False
            break
    if flag == True:
        prime_sum += p
        prime_num += 1

print(prime_sum)