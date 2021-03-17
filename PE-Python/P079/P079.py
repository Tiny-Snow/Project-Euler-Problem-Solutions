# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Fri, 12 Mar 2021, 13:19
# Project Euler # 079 Passcode derivation

#=================================================================================Solution
import os
BSER_DIR = os.path.dirname(os.path.abspath(__file__))

with open(BSER_DIR + '\p079_keylog.txt', mode = 'r') as datafile:
    key_list = datafile.read().split()

location_dict = {}                      # 储存位置关系，值列表为键的后面的值及其个数
key2_set = set()
for key in key_list:
    k1, k2, k3 = key
    key2_set = set(list(key2_set) + [k2])
    if k1 not in location_dict:
        location_dict[k1] = [[k2, k3], 2]
    else:
        location_dict[k1][0] = list(set(location_dict[k1][0] + [k2, k3]))
        location_dict[k1][1] = len(location_dict[k1][0])
    if k2 not in location_dict:
        location_dict[k2] = [[k3], 1]
    else:
        location_dict[k2][0] = list(set(location_dict[k2][0] + [k3]))
        location_dict[k2][1] = len(location_dict[k2][0])
    if k3 not in location_dict:
        location_dict[k3] = [[], 0]

n = len(key2_set) + 2                   # n表示密码位数，下面假定n为偶数
num_list = ['' for _ in range(n)]
for location in location_dict:
    num_list[n - location_dict[location][1] - 1] = location
num = ''.join(num_list)
print(int(num))