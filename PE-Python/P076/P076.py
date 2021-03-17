# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 10 Mar 2021, 16:41
# Project Euler # 076 Counting summations

#=================================================================================Solution
limit = 100
partition_list = [[0 for j in range(limit + 1)]for i in range(limit + 1)]
partition_list[0] = [1 for j in range(limit + 1)]
for n in range(1, limit + 1):
    for k in range(1, limit + 1):
        partition_list[n][k] = partition_list[n - k][k] + partition_list[n][k - 1]
print(partition_list[100][100] - 1)