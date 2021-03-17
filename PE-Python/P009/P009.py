# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Thu, 28 Jan 2021, 23:32
# Project Euler # 009 Special Pythagorean triplet

#==================================================Solution
for c in range(int(250 * (5 ** 0.5 - 1)), 500):
    for a in range(1, 1000 - c):
        b = 1000 - a - c
        if a ** 2 + b ** 2 == c ** 2:
            print(a * b * c)
            break