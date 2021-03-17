# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 20 Feb 2021, 22:45
# Project Euler # 035 Circular primes

#===========================================Solution
maxn = 1000000
double_base_palindromes_sum = 0
for i in range(1, maxn, 2):
    if str(i) == str(i)[ : : -1]:
        i_bin = str(bin(i))[2: ]
        if i_bin == i_bin[ : : -1]:
            double_base_palindromes_sum += i
print(double_base_palindromes_sum)