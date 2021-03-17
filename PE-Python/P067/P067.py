# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Fri, 5 Feb 2021, 22:41
# Project Euler # 067 Maximum path sum II

#===================================================================================================================Solution
#=================================================储存数据
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(BASE_DIR + '/p067_triangle.txt', mode = 'r') as datafile:
    data_str = datafile.readlines()
data = []
lines = len(data_str)
for i in range(lines):
    tempdata = data_str[i].split()
    for j in range(len(tempdata)):
        data.append(int(tempdata[j]))
#=================================================动态规划
data_sum = data
for i in reversed(range(lines - 1)):
    for j in range(i + 1):
        data_sum[i * (i + 1) // 2 + j] += max(data[(i + 1) * (i + 2) // 2 + j], data[(i + 1) * (i + 2) // 2 + j + 1])
print(data_sum[0])