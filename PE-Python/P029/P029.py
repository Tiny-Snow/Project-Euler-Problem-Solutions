# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Fri, 19 Feb 2021, 17:21
# Project Euler # 029 Distinct powers

#================================Solution
maxn = 100
numlist = []
for a in range(2, maxn + 1):
    for b in range(2, maxn + 1):
        numlist.append(a ** b)
numlist = list(set(numlist))
print(len(numlist))