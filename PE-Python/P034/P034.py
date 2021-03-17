# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 20 Feb 2021, 21:58
# Project Euler # 034 Digit factorials

#================================Solution
from math import *

maxn = 2177280
all_sum = 0
for i in range(10, maxn):
    sum = 0
    for j in str(i):
        sum += factorial(int(j))
    if sum == i:
        all_sum += i
print(all_sum)