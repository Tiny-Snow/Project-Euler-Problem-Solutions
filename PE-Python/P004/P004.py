# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 27 Jan 2021, 22:41
# Project Euler # 004 Largest palindrome product

#============================================================Solution 1
max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        ij = str(i * j)
        if ij == ''.join(reversed(ij)) and int(ij) > max:
            max = int(ij)
print(max)

#============================================================Solution 2
max = 0
for i in reversed(range(100, 1000)):
    for j in reversed(range(100, i + 1)):
        ij = str(i * j)
        if ij == ''.join(reversed(ij)) and int(ij) > max:
            max = int(ij)
print(max)

#============================================================Solution 3
max = 0
for i in reversed(range(100, 1000)):
    if i % 11 != 0:
        for j in reversed(range(110, i + 1, 11)):
            ij = str(i * j)
            if ij == ''.join(reversed(ij)) and int(ij) > max:
                max = int(ij)            
    else:
        for j in reversed(range(100, i + 1)):
            ij = str(i * j)
            if ij == ''.join(reversed(ij)) and int(ij) > max:
                max = int(ij)
print(max)