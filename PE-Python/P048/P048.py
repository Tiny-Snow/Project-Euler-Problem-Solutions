# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 22 Feb 2021, 17:55
# Project Euler # 048 Self powers

#===================================Solution
sum = 0
for k in range(1,1000 + 1):
    sum  = (sum + k ** k) % 10 ** 10
print(sum)