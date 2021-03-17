# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Fri, 19 Feb 2021, 13:30
# Project Euler # 028 Number spiral diagonals

#==========================================Solution
spiral_diagonal_sum = 1
pointer = 1
diff = 0
for layer in range(2, (1001 + 1) // 2 + 1):
    diff += 2
    for i in range(4):
        pointer += diff
        spiral_diagonal_sum += pointer
print(spiral_diagonal_sum)