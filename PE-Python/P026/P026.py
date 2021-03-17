# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 17 Feb 2021, 23:55
# Project Euler # 026 Reciprocal cycles

#=========================================================Solution
maxn = 1000
maxk = 1
d = 1
for n in range(2, maxn + 1):
    r_list = [0 for i in range(maxn + 1)]
    dividend = 1
    k = 1
    while True:
        r = dividend * 10 % n
        dividend = r
        if r == 0:                  # 有限小数的情况
            break
        if r_list[r] != 0:          # 余数重复，即循环的情况
            if maxk < k - r_list[r]:
                maxk = k - r_list[r]
                d = n
            break
        r_list[r] = k               # 标记余数r出现的位数
        k += 1
print(d)