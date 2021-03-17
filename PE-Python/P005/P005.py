# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Thu, 28 Jan 2021, 02:59
# Project Euler # 005 Smallest multiple

#==========================================Solution
from math import *

n_lcm = 1
for i in range(1, 21):
    n_lcm = int((n_lcm * i)/gcd(n_lcm, i))
print(n_lcm)