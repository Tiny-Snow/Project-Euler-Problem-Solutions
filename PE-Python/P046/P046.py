# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 22 Feb 2021, 14:44
# Project Euler # 046 Goldbach's other conjecture

#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P046')[0] + 'Utility Class')

from prime_utility import *
limit = 10000
prime_class = Prime(limit)
prime_class._traverse()

for n in range(9, limit, 2):
    if prime_class._is_prime(n) == True:
        continue
    flag = False
    for k in range(1, int((n / 2) ** 0.5) + 1):
        if prime_class._is_prime(n - 2 * (k ** 2)) == True:
            flag = True
            break
    if flag == False:
        print(n)
        break