# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 27 Jan 2021, 22:09
# Project Euler # 003 Largest prime factor

#====================================Solution
from math import *

n = 600851475143
p_list = []
for i in range(3, int(sqrt(n)), 2):
    if n % i == 0:
        p_list.append(i)
        while n % i == 0:
            n /= i
print(max(n, max(p_list)))