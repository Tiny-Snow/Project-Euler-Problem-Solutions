# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 20 Feb 2021, 15:54
# Project Euler # 030 Digit fifth powers

#=======================================Solution
k = 1
while k * (9 ** 5) > (10 ** k - 1) // 9:
    k += 1

maxn = 10 ** k
all_sum = 0
for i in range(2, maxn):
    sum = 0
    for j in str(i):
        sum += int(j) ** 5
    if int(sum) == i:
        all_sum += i
print(all_sum)