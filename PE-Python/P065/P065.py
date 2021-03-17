# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 3 Mar 2021, 16:46
# Project Euler # 065 Convergents of e

#===================================================Solution
from fractions import Fraction

num_list = [2]
for k in range(1, 34):
    num_list.append(1)
    num_list.append(2 * k)
    num_list.append(1)

p = len(num_list) - 1
e = Fraction(1, num_list[p])
p -= 1
while p > 0:
    e += num_list[p]
    e = Fraction(1, e)
    p -= 1
e += num_list[p]

sum = 0
for i in str(e._numerator):
    sum += int(i)
print(sum)