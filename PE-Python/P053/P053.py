# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 23 Feb 2021, 20:45
# Project Euler # 053 Combinatoric selections

#==============================================Solution
import itertools
from scipy.special import comb

origin = 1
while comb(origin, origin // 2) <= 1000000:
    origin += 1
left = origin // 2
right = origin // 2 + 1
greater_num = 2
for l in reversed(range(0, left)):
    if comb(origin, l) < 1000000:
        break
    left = l
    greater_num += 1
for r in range(right + 1, origin + 1):
    if comb(origin, r) < 1000000:
        break
    right = r
    greater_num += 1

for n in range(origin + 1, 100 + 1):
    greater_num += (right - left + 1)
    for l in reversed(range(0, left)):
        if comb(n, l) < 1000000:
            break
        left = l
        greater_num += 1
    for r in range(right + 1, n + 1):
        if comb(n, r) < 1000000:
            break
        right = r
        greater_num += 1
print(greater_num)