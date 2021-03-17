# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 16 Feb 2021, 23:07
# Project Euler # 021 Amicable numbers

#==================================================================================================================================Solution
maxn = 10000
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

amicable_num = [0 for i in range(maxn + 1)]         # 0表示不是amicable number，1代表是amicable number
amicable_sum = 0
for i in range(1, maxn):
    sumd_list[i] -= i
for i in range(1, maxn):
    if amicable_num[i] == 1:
        continue
    if sumd_list[i] <= maxn:
        if i == sumd_list[sumd_list[i]] and sumd_list[i] != i:
            amicable_sum += (i + sumd_list[i])
            amicable_num[i] = amicable_num[sumd_list[i]] = 1
print(amicable_sum)