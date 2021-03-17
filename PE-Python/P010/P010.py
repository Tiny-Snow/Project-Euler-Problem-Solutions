# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Thu, 28 Jan 2021, 23:48
# Project Euler # 010 Summation of primes

#==========================================Solution
maxn = 2000001
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
print(sum(p_list))