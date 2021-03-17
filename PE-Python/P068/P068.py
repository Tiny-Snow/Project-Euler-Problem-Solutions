# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 6 Mar 2021, 13:28
# Project Euler # 068 Magic 5-gon ring

#================================================================================Solution
import itertools

def find_magic_group(n, digit):                 # 返回和为digit的三元组
    group_list = []
    for group in itertools.combinations(range(1, 2 * n + 1), 3):
        if sum(group) == digit:
            group_list.append(group)
    return group_list

def find_comb(n, group_list):                   # 返回符合的三元组组合及内环数字
    if len(group_list) < n:
        return []

    ans_comb = []
    for comb in itertools.combinations(group_list, n):
        ans = []
        for group in comb:
            ans += group
        
        if len(set(ans)) == 2 * n:          # 保证10个数均出现
            seconds = 0                     # 判断出现两次的数的个数，即内环上的数
            second_list = []
            for i in range(1, 2 * n + 1):
                if ans.count(i) == 2:
                    seconds += 1
                    second_list.append(i)
            if seconds == n:                # 保证内环有五个数
                group_flag = True
                for group in comb:
                    group_seconds = 0       # 判断每个三元组中的内环数个数
                    for i in group:
                        if i in second_list:
                            group_seconds += 1
                    if group_seconds != 2:  # 保证每个三元组中的内环数个数为2
                        group_flag = False
                        break
                if group_flag == True:
                    ans_comb.append([comb, second_list])
    return ans_comb


n = 5
ans_list = []
for digit in range(2 * n + 3, 6 * n - 2):
    group_list = find_magic_group(n, digit)
    ans_comb = find_comb(n, group_list)
    if ans_comb != []:
        for comb in ans_comb:
            if 10 not in comb[1]:           # 保证数字总位数为16
                ans_list.append(comb)       # 获得所有可能的16-digit组合

def get_next_group(string, second, next_group_list, first_dict):    # 迭代函数，传入余下三元组集合和上一个末尾内环数，获得下一个相邻的三元组
    if len(next_group_list) == 0:
        return string
    for group in next_group_list:
        if second in group:
            temp_group = list(group)
            temp_group.remove(first_dict[group])
            temp_group.remove(second)
            next_second = temp_group[0]
            string += str(first_dict[group]) + str(second) + str(next_second)
            next_group_list.remove(group)
            return get_next_group(string, next_second, next_group_list, first_dict)


max_string = '0'                            # 获得最终的结果
for comb in ans_list:
    group_comb = comb[0]
    second_list = comb[1]
    first_dict = {}.fromkeys(group_comb)    # 将三元组与其中的外环数映射起来
    for group in group_comb:
        for i in group:
            if i not in second_list:
                first_dict[group] = i
    min_first = min(first_dict.values())    # 从外环最小数开始
    for group in group_comb:
        if min_first in group:
            del_group = group               # 需要去掉的第一个组
    next_group_list = list(group_comb)
    next_group_list.remove(del_group)
    del_group = list(del_group)
    del_group.remove(min_first)             # 遍历第一个内环数的两种可能
    string1 = get_next_group(str(min_first) + str(del_group[1]) + str(del_group[0]), del_group[0], next_group_list, first_dict)
    strint2 = get_next_group(str(min_first) + str(del_group[1]) + str(del_group[0]), del_group[1], next_group_list, first_dict)
    max_string = str(max(int(max_string), int(string1), int(strint2)))
print(max_string)