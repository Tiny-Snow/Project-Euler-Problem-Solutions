# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 27 Jan 2021, 19:31
# Project Euler # 001 Multiples of 3 and 5

#=====================================Solution
sum = 0
for i in range(1000):
    if i % 3 == 0:
        sum += i
    if i % 5 == 0:
        sum += i
    if i % 15 == 0:
        sum -= i
print(sum)