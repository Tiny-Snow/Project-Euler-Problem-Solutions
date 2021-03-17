# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 30 Jan 2021, 12:33
# Project Euler # 012 Highly divisible triangular number

#==================================================================Solution 1
def triangle_number(n):
    return int(n * (n+1) / 2)
maxn = 100000000
p_list = []
d_dict = {}.fromkeys(range(1, maxn))
d_dict[1] = 1
prime_dict = {}.fromkeys(range(1, maxn), 1)
prime_dict[1] = 0
for p in list(prime_dict.keys()):
    if prime_dict[p] == 1:
        p_list.append(p)
        d_dict[p] = 2            # 质数的因子只有两个
    for j in range(len(p_list)):
        if p * p_list[j] > maxn:
            break
        prime_dict[p * p_list[j]] = 0
        if p % p_list[j] == 0:
            p_divided_by_pj = p
            while p_divided_by_pj % p_list[j] == 0:                # 遍历至最小质因数时，利用d(n)为积性函数
                p_divided_by_pj /= p_list[j]
            d_dict[p * p_list[j]] = d_dict[p] + d_dict[p_divided_by_pj]
            break 
        else:
            d_dict[p * p_list[j]] = d_dict[p] * d_dict[p_list[j]]   # 未遍历至最小质因数时，利用d(n)为积性函数
n = 1
while triangle_number(n) < maxn:
    t = triangle_number(n)
    if d_dict[t] >= 500:
        print(t)
        break
    n += 1
#==================================================================Solution 2
def d(n):
    d = 0
    for i in range(1, int(n ** 0.5)):
        if n % i == 0:
            if i ** 2 == n:
                d += 1
            else:
                d += 2
    return d
n = 1
while True:
    if d(n * (n + 1) // 2) >= 500:
        print(n * (n + 1) // 2)
        break
    n += 1