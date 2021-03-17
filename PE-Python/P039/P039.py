# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sun, 21 Feb 2021, 17:21
# Project Euler # 039 Integer right triangles

#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P039')[0] + 'Utility Class')

from prime_utility import *

limit = 1000
prime_class = Prime(limit // 2)
prime_class._traverse()
prime_class._find_factor()
factor_list = prime_class._get_factor_list()

def get_setnum(origin_list):
    if origin_list == []:                # 注意空列表情况
        return 0
    num = 1
    for l in range(len(origin_list) - 1):
        flag = True
        for i in range(l + 1, len(origin_list)):
            if origin_list[l] == origin_list[i]:
                flag = False
        if flag == True:
            num += 1
    return num

max_solution = 0
p_ans = 0
for p in range(12, limit, 2):
    solution = 0
    solution_list = []
    for k in factor_list[p // 2]:
        for a in factor_list[p // (2 * k)]:
            if a > (p // (2 * k)) ** 0.5:
                break
            b = p // (2 * k * a) - a
            if a > b and b > 0:
                solution_list.append(list(sorted([k * (a ** 2 - b ** 2), 2 * k * a * b, k * (a ** 2 + b ** 2)])))
    solution = get_setnum(solution_list)
    if solution >= max_solution:
        p_ans = p
        max_solution = solution
print(p_ans)