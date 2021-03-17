# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 30 Jan 2021, 13:52
# Project Euler # 014 Longest Collatz sequence

#==========================================================================================Solution
maxn = 1000000
collatz_list = [0] * maxn                               # 以每个数为初始项的序列长度
collatz_list[1] = 1
def collatz(n, len):
    '''传入参数为(目前序列的初始项n，初始序列长度（n之前的）len)，返回值为整个序列的长度'''
    if n == 1:
        return len + 1
    if n % 2 == 0:
        if n / 2 < maxn and collatz_list[int(n / 2)] != 0:      # 首先在序列中查找是否已经找到     
            return len + collatz_list[int(n / 2)]
        else:
            return collatz(int(n / 2), len + 1)
    else:
        if 3 * n + 1 < maxn and collatz_list[3 * n + 1] != 0:   # 首先在字典中查找是否已经找到        
            return len + collatz_list[3 * n + 1]
        else:
            return collatz(3 * n + 1, len + 1)
for i in range(1, maxn):
    collatz_list[i] = collatz(i, 0)
print(collatz_list.index(max(collatz_list)))