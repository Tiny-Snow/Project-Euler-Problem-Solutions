# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sun, 21 Feb 2021, 14:58
# Project Euler # 038 Pandigital multiples

#================================================================Solution
product_max = 0
for n in range(1, 10000):
    k = 2
    product = str(n)
    while len(product) < 9:
        product += str(k * n)
        k += 1
    if ''.join(sorted(product)) == '123456789':
        product_max = max(product_max, int(product))
print(product_max)