# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sun, 21 Feb 2021, 17:44
# Project Euler # 040 Champernowne's constant

#=======================================================Solution
fractional_part = ''
product = 1
i = 1
while len(fractional_part) <= 1000000:
    fractional_part += str(i)
    if i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        product *= int(fractional_part[i - 1])
    i += 1
print(product)