# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Thu, 28 Jan 2021, 14:09
# Project Euler # 007 10001st prime

#=============================================================Solution 1
maxn = 116672
p_num = 0
# 初始化认为全部为素数，1为素数，0不为素数
prime_dict = {}.fromkeys(range(1, maxn), 1)   
prime_dict[1] = 0
for p in prime_dict:
    if prime_dict[p] == 1:
        for i in range(p ** 2, maxn, p):    # 筛去所有的p的倍数
            prime_dict[i] = 0
        p_num += 1
        if p_num == 10001:
            print(p)
            break

#=============================================================Solution 2
maxn = 116672
p_list = []
prime_dict = {}.fromkeys(range(1, maxn), 1)
prime_dict[1] = 0
for p in list(prime_dict.keys()):
    if prime_dict[p] == 1:
        p_list.append(p)
    for j in range(len(p_list)):
        if p * p_list[j] > maxn:
            break
        prime_dict[p * p_list[j]] = 0
        if p % p_list[j] == 0:
            break
print(p_list[10000])