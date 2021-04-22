# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 30 Mar 2021, 17:09
# Project Euler # 085 Counting rectangles

#=============================================================Solution
def get_rectangles(m, n):
    return m * (m + 1) * n * (n + 1) // 4

diff = 10000
area = 0
for m in range(1, int(2 * (2 ** 0.5) * 10 * 3) + 1):
    for n in range(m, int(2 * (2 ** 0.5) * 10 * 3) + 1):
        if abs(get_rectangles(m, n) - 2 * (10 ** 6)) < diff:
            area = m * n
            diff = abs(get_rectangles(m, n) - 2 * (10 ** 6))
print(area)