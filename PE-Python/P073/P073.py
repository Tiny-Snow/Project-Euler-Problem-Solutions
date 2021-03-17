# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sun, 7 Mar 2021, 14:12
# Project Euler # 073 Counting fractions in a range

#===================================================Solution
from math import gcd

num = 0
for d in range(4, 12000 + 1):
    for n in range(int(d / 3) + 1, int(d / 2) + 1):
        if gcd(n, d) == 1:
            num += 1
print(num)