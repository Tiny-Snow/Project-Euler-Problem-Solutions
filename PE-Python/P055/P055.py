# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 24 Feb 2021, 00:50
# Project Euler # 055 Lychrel numbers

#=================================================Solution
lychrel_numbers = 0
for n in range(1, 10000):
    flag = True
    str_n = str(n)
    reverse_n = ''.join(reversed(str_n))
    for _ in range(50):
        str_n = str(int(str_n) + int(reverse_n))
        reverse_n = ''.join(reversed(str_n))
        if str_n == reverse_n:
            flag = False
            break
    if flag == True:
        lychrel_numbers += 1
print(lychrel_numbers)