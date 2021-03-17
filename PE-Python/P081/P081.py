# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 15 Mar 2021, 16:34
# Project Euler # 081 Path sum: two ways

#======================================================================================Solution
import os
BSER_DIR = os.path.dirname(os.path.abspath(__file__))

n = 80
data_list = []
with open(BSER_DIR + '\p081_matrix.txt', mode = 'r') as datafile:
    for _ in range(n):
        data_list.append(list(map(int, datafile.readline().split(','))))

DP_list = data_list.copy()                      # DP_list储存每个位置到达右下角的最短路径
# 末列和末行只有一种选择
for i in reversed(range(n - 1)):
    DP_list[n - 1][i] += DP_list[n - 1][i + 1]
    DP_list[i][n - 1] += DP_list[i + 1][n - 1]
# 其余位置均有两种选择
for i in reversed(range(n - 1)):
    for j in reversed(range(n - 1)):
        DP_list[i][j] += min(DP_list[i][j + 1], DP_list[i + 1][j])
print(DP_list[0][0])