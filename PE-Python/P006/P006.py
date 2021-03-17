# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Thu, 28 Jan 2021, 03:16
# Project Euler # 006 Sum square difference

#==========================================Solution
n = 100
sum_square = n * (n + 1) *(2 *n + 1) // 6
square_sum = (n * (n + 1) // 2) ** 2
print(square_sum - sum_square)