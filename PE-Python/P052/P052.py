# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 23 Feb 2021, 20:17
# Project Euler # 052 Permuted multiples

#================================================================Solution
def is_positive(n):
    for m in range(2, 7):
        if sorted(str(n)) != sorted(str(m * n)):
            return False
    return True

def find_ans():
    k = 0
    while True:
        for x in range(int(10 ** (k - 1)), int((10 ** k) / 6)):
            if is_positive(x) == True:
                return x
        k += 1

print(find_ans())