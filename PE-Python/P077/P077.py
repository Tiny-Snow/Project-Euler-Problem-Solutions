# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 10 Mar 2021, 23:19
# Project Euler # 077 Prime summations

#=================================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P077')[0] + 'Utility Class')

from prime_utility import *

limit = 100
prime_class = Prime(limit)
prime_class._traverse()
prime_list = prime_class._get_prime_list()
prime_num = len(prime_list)

partition_list = [{}.fromkeys(prime_list, 0) for i in range(limit + 1)]
partition_list[0] = {}.fromkeys(prime_list, 1)
partition_list[2] = {}.fromkeys(prime_list, 1)
for n in range(3, limit + 1):
    if n % 2 == 0:
        partition_list[n][2] = 1
    else:
        partition_list[n][2] = 0
    for k in range(1, len(prime_list)):
        partition_list[n][prime_list[k]] = partition_list[n - prime_list[k]][prime_list[k]] + partition_list[n][prime_list[k - 1]]

for n in range(1, limit + 1):
    if partition_list[n][prime_list[len(prime_list) - 1]] > 5000:
        print(n)
        break