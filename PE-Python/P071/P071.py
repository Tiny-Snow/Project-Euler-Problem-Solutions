# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sun, 7 Mar 2021, 13:49
# Project Euler # 071 Ordered fractions

#===================================================Solution
from fractions import Fraction
from math import gcd

diff = 1
ans_frac = Fraction(0, 1)
for d in range(1, 1000000 + 1):
    for n in reversed(range(1, int(3 * d / 7))):
        if (Fraction(2, 5) - Fraction(n, d)) > diff:
            break
        if gcd(n, d) == 1:
            ans_frac = Fraction(n, d)
            diff = Fraction(2, 5) - Fraction(n, d)
            break
print(ans_frac._numerator)