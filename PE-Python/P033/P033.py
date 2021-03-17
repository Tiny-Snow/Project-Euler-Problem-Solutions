# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 20 Feb 2021, 21:32
# Project Euler # 033 Digit cancelling fractions

#====================================================================Solution
from math import *

def is_curious(m, n):
    flag = False
    if str(m)[1] == str(n)[0] and str(n)[1] != '0':
        if int(str(m)[0]) / int(str(n)[1]) == m / n:
            flag = True
    return flag

product_numerator = 1
product_denominator = 1

for m in range(10, 100):
    for n in range(m + 1, 100):
        if m % 10 == 0 and n % 10 == 0:
            continue
        if is_curious(m, n) == True:
            product_numerator *= m
            product_denominator *= n

print(product_denominator // gcd(product_denominator, product_numerator))