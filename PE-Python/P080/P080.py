# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sun, 14 Mar 2021, 18:55
# Project Euler # 080 Square root digital expansion

#====================================================Solution
from decimal import *

getcontext().prec = 110         # 设置精度为110
digit_sum = 0
for D in range(1, 100 + 1):
    if D ** 0.5 == int(D ** 0.5):
        continue
    digit = str(Decimal(D).sqrt())[:101]
    for i in digit:
        if i != '.':
            digit_sum += int(i)
print(digit_sum)