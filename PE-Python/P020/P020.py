# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 6 Feb 2021, 00:29
# Project Euler # 020 Factorial digit sum

#============================Solution
from math import *
num_str = str(factorial(100))
num_sum = 0
for i in num_str:
    num_sum += int(i)
print(num_sum)