# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 2 Mar 2021, 16:47
# Project Euler # 063 Powerful digit counts

#=====================================================================Solution
num = 0
for a in range(1, 10):
    n = 1
    while len(str(a ** n)) == n:
        n += 1
        num += 1
print(num)