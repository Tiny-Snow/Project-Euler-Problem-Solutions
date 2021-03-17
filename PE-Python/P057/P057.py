# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Thu, 25 Feb 2021, 14:43
# Project Euler # 057 Square root convergents

#=================================================Solution
from fractions import Fraction

numerator_more_digits = 0
denominator = Fraction(2, 1)
for i in range(1000):
    num = Fraction(1, 1) + Fraction(1, denominator)
    denominator = Fraction(2, 1) + Fraction(1, denominator)
    if len(str(num.numerator)) > len(str(num.denominator)):
        numerator_more_digits += 1
print(numerator_more_digits)