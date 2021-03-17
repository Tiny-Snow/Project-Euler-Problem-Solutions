# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 20 Feb 2021, 20:44
# Project Euler # 032 Pandigital products

#=======================================Solution
num_list = []

def is_pandigital(numstr):
    flag = True
    for i in range(1, 10):
        if str(i) not in numstr:
            flag = False
    return flag

# a为1位数，b为4位数，a * b为4位数
for a in range(1, 10):
    for b in range(1000, 10000):
        if a * b >= 10000:
            break
        numstr = str(a) + str(b) + str(a * b)
        if is_pandigital(numstr) == True:
            num_list.append(a * b)

# a为2位数，b为3位数，a * b为4位数
for a in range(10, 100):
    for b in range(100, 1000):
        if a * b >= 10000:
            break
        numstr = str(a) + str(b) + str(a * b)
        if is_pandigital(numstr) == True:
            num_list.append(a * b)

num_list = list(set(num_list))
print(sum(num_list))