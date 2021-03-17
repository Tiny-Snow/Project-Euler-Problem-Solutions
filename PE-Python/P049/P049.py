# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 22 Feb 2021, 18:27
# Project Euler # 049 Prime permutations

#===================================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P049')[0] + 'Utility Class')

from prime_utility import *
limit = 10000
prime_class = Prime(limit)
prime_class._traverse()

import itertools

ans_list = []
for num in range(1000, 10000):
    permutations = list(itertools.permutations(list(str(num)), 4))
    for num1, num2, num3 in list(itertools.combinations(permutations, 3)):
        num1 = int(num1[0] + num1[1] + num1[2] + num1[3])
        num2 = int(num2[0] + num2[1] + num2[2] + num2[3])
        num3 = int(num3[0] + num3[1] + num3[2] + num3[3])
        num1, num2, num3 = tuple(sorted((num1, num2, num3)))
        if len(str(num1)) == len(str(num2)) == len(str(num3)) == 4:
            if num1 == num2 or num1 in ans_list:        # 去除三数相同结果和重复结果
                continue
            if num2 - num1 == num3 - num2 and prime_class._is_prime(num1) == True and\
                    prime_class._is_prime(num2) == True and prime_class._is_prime(num3) == True:
                print(num1, num2, num3)
                ans_list.append(num1)