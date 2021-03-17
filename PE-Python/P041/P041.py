# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 22 Feb 2021, 02:19
# Project Euler # 041 Pandigital prime

#=============================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P041')[0] + 'Utility Class')

from prime_utility import *
limit = 10 ** 7             # n = 1, 4, 7
prime_class = Prime(limit)
prime_class._traverse()

import itertools

def find_prime(n):
    max_prime = 0
    for p_tuple in list(itertools.permutations([i for i in range(1, n + 1)], n)):
        p = ''
        for i in p_tuple:
            p += str(i)
        if prime_class._is_prime(int(p)) == True:
            max_prime = max(max_prime, int(p))
    return max_prime

ans = max(find_prime(1), find_prime(4), find_prime(7))
print(ans)