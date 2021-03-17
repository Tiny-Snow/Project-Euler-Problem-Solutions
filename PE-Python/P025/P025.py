# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 17 Feb 2021, 20:18
# Project Euler # 025 1000-digit Fibonacci number


#=============================Solution
f_1 = 1
f_2 = 1
f_3 = f_1 + f_2
index = 3
while len(str(f_3)) != 1000:
    f_1 = f_2
    f_2 = f_3
    f_3 = f_1 + f_2
    index += 1
print(index)