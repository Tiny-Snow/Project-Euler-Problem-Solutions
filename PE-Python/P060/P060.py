# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Fri, 26 Feb 2021, 00:55
# Project Euler # 060 Prime pair sets

#==================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P060')[0] + 'Utility Class')

from prime_utility import *
limit = 10000
prime_class = Prime(limit)
prime_class._traverse()
prime_list = prime_class._get_prime_list()

def is_prime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

def is_prime_pair(p1, p2):
    if is_prime(int(str(p1) + str(p2))) == True and is_prime(int(str(p2) + str(p1))) == True:
        return True
    return False

def is_prime_pair_set(prime_set):
    for p1 in range(len(prime_set) - 1):
        for p2 in range(p1 + 1, len(prime_set)):
            if is_prime_pair(prime_set[p1], prime_set[p2]) != True:
                return False
    return True

def find_ans():
    for i1 in range(len(prime_list) - 4):
        for i2 in range(i1 + 1, len(prime_list) - 3):
            if is_prime_pair_set([prime_list[i1], prime_list[i2]]) == True:
                for i3 in range(i2 + 1, len(prime_list) - 2):
                    if is_prime_pair_set([prime_list[i1], prime_list[i2], prime_list[i3]]) == True:
                        for i4 in range(i3 + 1, len(prime_list) - 1):
                            if is_prime_pair_set([prime_list[i1], prime_list[i2], prime_list[i3], prime_list[i4]]) == True:
                                for i5 in range(i4 + 1, len(prime_list)):
                                    if is_prime_pair_set([prime_list[i1], prime_list[i2], prime_list[i3], prime_list[i4], prime_list[i5]]) == True:
                                        return sum([prime_list[i1], prime_list[i2], prime_list[i3], prime_list[i4], prime_list[i5]])
print(find_ans())