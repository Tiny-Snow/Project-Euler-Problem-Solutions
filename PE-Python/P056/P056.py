# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Thu, 25 Feb 2021, 14:21
# Project Euler # 056 Powerful digit sum

#=================================================Solution
max_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        num = a ** b
        num_sum = 0
        for char in str(num):
            num_sum += int(char)
            max_sum = max(max_sum, num_sum)
print(max_sum)