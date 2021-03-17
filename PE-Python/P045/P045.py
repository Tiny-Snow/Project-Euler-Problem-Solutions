# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 22 Feb 2021, 13:49
# Project Euler # 045 Triangular, pentagonal, and hexagonal

#======================================================================================================Solution
def is_pentagon(num):
    n = int(((2 / 3) * num) ** 0.5) + 1
    if n * (3 *n - 1) == 2 * num:
        return True
    return False

def is_hexagon(num):
    n = int((num / 2) ** 0.5) + 1
    if n * (2 *n - 1) == num:
        return True
    return False

start = 286
while True:
    if is_pentagon(start * (start + 1) // 2) == True and is_hexagon(start * (start + 1) // 2) == True:
        break
    start += 1
print(start * (start + 1) // 2)