# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Fri, 19 Feb 2021, 11:39
# Project Euler # 027 Quadratic primes

#===========================================================Solution
#========================================遍历素数
maxn = 1000 * 1000 + 1000 * 1000 + 1000
p_list = []
prime_list = [1 for i in range(maxn + 1)]
prime_list[1] = 0
for p in range(1, maxn + 1):
    if prime_list[p] == 1:
        p_list.append(p)
    for j in range(len(p_list)):
        if p * p_list[j] > maxn:
            break
        prime_list[p * p_list[j]] = 0
        if p % p_list[j] == 0:
            break
#========================================寻找a, b
final_a = 0
final_b = 0
p_num_max = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        p_num = 0
        while n ** 2 + a * n + b > 0:
            if prime_list[(n ** 2 + a * n + b)] == 1:   #注意负数的情况
                p_num += 1
                n += 1
            else:
                break
        if p_num > p_num_max:
            final_a = a
            final_b = b
            p_num_max = p_num
print(final_a * final_b)