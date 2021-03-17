# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 22 Feb 2021, 11:18
# Project Euler # 043 Sub-string divisibility

#==========================================================================Solution
import itertools

prime_list = [2, 3, 5, 7, 11, 13, 17]
def is_right(num, prime_list):
    for i in range(len(prime_list)):
        if int(num[i + 1: i + 4]) % prime_list[i] != 0:
            return False
    return True

all_sum = 0
for num_tuple in list(itertools.permutations([i for i in range(0, 10)], 10)):
    if num_tuple[0] == 0:       # 首位为0的情况
        continue
    num = ''
    for i in num_tuple:
        num += str(i)
    if is_right(num, prime_list) == True:
        all_sum += int(num)
print(all_sum)