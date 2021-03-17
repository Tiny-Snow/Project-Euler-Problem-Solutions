# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 20 Feb 2021, 22:45
# Project Euler # 035 Circular primes

#==================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P035')[0] + 'Utility Class')

from prime_utility import *

limit = 1000000
circular_primes = 0
prime_class = Prime(limit)
prime_class._traverse()
for p in prime_class._get_prime_list():
    flag = True
    l = len(str(p))
    for i in range(1, l):
        if prime_class._is_prime(int(str(p)[i: l] + str(p)[0: i])) == False:
            flag = False
    if flag == True:
        circular_primes += 1
print(circular_primes)