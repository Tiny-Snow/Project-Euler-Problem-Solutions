# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 30 Jan 2021, 22:10
# Project Euler # 016 Power digit sum

#=====================================Solution
data = str(2 ** 1000)
sum = 0
for i in data:
    sum += int(i)
print(sum)