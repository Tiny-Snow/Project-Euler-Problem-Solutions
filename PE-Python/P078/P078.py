# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Thu, 11 Mar 2021, 14:31
# Project Euler # 078 Coin partitions

#=================================================================================Solution
partition_dict = {0: 1, 1: 1}
n = 2
while True:
    sum_p = 0
    for k in range(-int(((24 * n + 1) ** 0.5 - 1) / 6), int(((24 * n + 1) ** 0.5 + 1) / 6) + 1):
        if k == 0:
            continue
        sum_p += int(((-1) ** (k + 1))) * partition_dict[int(n - k * (3 * k - 1) // 2)]
    partition_dict[n] = sum_p
    if str(sum_p)[-6:] == '000000':
        print(n)
        break
    n += 1