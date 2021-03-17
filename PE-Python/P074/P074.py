# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 9 Mar 2021, 17:57
# Project Euler # 074 Digit factorial chains

#=====================================================================================================================Solution
from math import factorial

limit = 1000000
chain_dict = {}             # 储存在chains中遍历过的数与chain长度的对应关系

def find_chain_len(n, start, chain_list):           # 对于以start位置的n开始的chain求len；如果chain_len大于60次返回False
    chain_len = start
    if chain_len >= 60:                             # 长于60的chain直接舍去
        return False
    if n in chain_dict:                             # 尝试寻找以前遍历的结果
        chain_len += chain_dict[n] - 1
        return chain_len
    now_n = 0
    for i in str(n):
        now_n += factorial(int(i))
    if now_n in chain_list:                         # 下一个数形成环得到结果
        return chain_len
    chain_list.append(now_n)                        # 没有形成环，记录在chain中
    chain_len = find_chain_len(now_n, start + 1, chain_list)
    if chain_len != False:                          # 如果得到非False的len结果，将len储存在dict中并返回
        chain_dict[n] = chain_len - start + 1
        return chain_len
    return False

num = 0
for n in range(1, limit + 1):
    if find_chain_len(n, 1, [n]) == 60:
        num += 1
print(num)