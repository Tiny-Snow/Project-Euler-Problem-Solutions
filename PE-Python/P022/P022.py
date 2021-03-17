# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 16 Feb 2021, 23:33
# Project Euler # 022 Names scores

#==================================================================Solution
#=================================================储存数据
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(BASE_DIR + '/p022_names.txt', mode = 'r') as datafile:
    data_str = datafile.read()
    data = list(data_str.split(','))
for i in range(len(data)):
    data[i] = data[i][1:-1]         # 除去两侧引号
#=================================================排序+计算
data = sorted(data)
def word_score(word):
    score = 0
    for char in word:
        score += ord(char) - 64
    return score
sum_score = 0
for i in range(len(data)):
    sum_score += word_score(data[i]) * (i + 1)
print(sum_score)