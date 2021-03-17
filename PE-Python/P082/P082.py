# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 15 Mar 2021, 22:01
# Project Euler # 082 Path sum: three ways

#====================================================================================================================Solution
import os
BSER_DIR = os.path.dirname(os.path.abspath(__file__))

import copy

n = 80
data_list = []
with open(BSER_DIR + '\p082_matrix.txt', mode = 'r') as datafile:
    for _ in range(n):
        data_list.append(list(map(int, datafile.readline().split(','))))

DP_ans = [0] * n                        # 对于每次遍历的第col列，DP_ans[row]代表从末列某位置到达row行col列位置的最短路径
# 出于最小值的考虑，末列不需要进行上下移动
for i in range(n):
    DP_ans[i] = data_list[i][n - 1]
# 开始对每一列进行DP_ans的更新
for col in reversed(range(n - 1)):
    # 先考虑向下的情况
    DP_ans[0] += data_list[0][col]      # 由于不考虑向上移动，首行初始化为向上移动
    for row in range(1, n):
        DP_ans[row] = min(DP_ans[row] + data_list[row][col], DP_ans[row - 1] + data_list[row][col])
    # 再考虑向上的情况
    for row in reversed(range(n - 1)):
        DP_ans[row] = min(DP_ans[row], DP_ans[row + 1] + data_list[row][col])
print(min(DP_ans))