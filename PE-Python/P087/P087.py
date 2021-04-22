# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 30 Mar 2021, 22:14
# Project Euler # 087 1097343

#=================================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P087')[0] + 'Utility Class')

from prime_utility import *

limit = int(50000000 ** 0.5)
prime_class = Prime(limit)
prime_class._traverse()
prime_list = prime_class._get_prime_list()

sum_list = []
for i in range(len(prime_list)):
    if prime_list[i] ** 2 >= 50000000:
        break
    for j in range(len(prime_list)):
        if prime_list[i] ** 2 + prime_list[j] ** 3>= 50000000:
            break
        for k in range(len(prime_list)):
            if prime_list[i] ** 2 + prime_list[j] ** 3 + prime_list[k] ** 4 >= 50000000:
                break
            sum_list.append(prime_list[i] ** 2 + prime_list[j] ** 3 + prime_list[k] ** 4)
sum_list = list(set(sum_list))
print(len(sum_list))