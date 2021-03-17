# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 17 Feb 2021, 03:16
# Project Euler # 023 Non-abundant sums

#==================================================================================================================================Solution
maxn = 28123
p_list = []
sumd_list = [0 for i in range(maxn + 1)]
sumd_list[1] = 1
prime_list = [1 for i in range(maxn + 1)]
prime_list[1] = 0
for p in range(1, maxn + 1):
    if prime_list[p] == 1:
        p_list.append(p)
        sumd_list[p] = 1 + p            # 质数的因子只有两个
    for j in range(len(p_list)):
        if p * p_list[j] > maxn:
            break
        prime_list[p * p_list[j]] = 0
        if p % p_list[j] == 0:          # 遍历至最小质因数
            p_divided_by_pj = p
            alpha_j = 1
            while p_divided_by_pj % p_list[j] == 0:
                p_divided_by_pj /= p_list[j]
                alpha_j += 1
            sumd_list[p * p_list[j]] = sumd_list[int(p_divided_by_pj)] * int(((p_list[j] ** (alpha_j + 1) - 1) // (p_list[j] - 1)))
            break 
        else:                           # 没有遍历到质因数
            sumd_list[p * p_list[j]] = sumd_list[p] * sumd_list[p_list[j]]

abundant_numlist = []
for i in range(1, maxn + 1):
    sumd_list[i] -= i
    if sumd_list[i] > i:
        abundant_numlist.append(i)

abundant_sums = []
for i in range(len(abundant_numlist) - 1):
    for j in range(i, len(abundant_numlist)):
        abundant_sum = abundant_numlist[i] + abundant_numlist[j]
        if abundant_sum > maxn:
            break
        if abundant_sum not in abundant_sums:
            abundant_sums.append(abundant_sum)
            print(len(abundant_sums))
print(maxn * (maxn + 1) // 2 - abundant_numsum)