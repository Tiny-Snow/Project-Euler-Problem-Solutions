# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Thu, 25 Feb 2021, 20:52
# Project Euler # 058 Spiral primes

#==========================================Solution
def is_prime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

limit = 15000 ** 2
def find_ans():
    spiral = 1
    spiral_prime = 0
    pointer = 1
    diff = 0
    for layer in range(2, int(limit ** 0.5 + 1)):
        diff += 2
        spiral += 4
        for i in range(4):
            pointer += diff
            if is_prime(pointer) == True:
                spiral_prime += 1
        if spiral_prime / spiral < 0.1:
            return diff + 1

print(find_ans())