# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 1 Mar 2021, 17:54

# Project Euler # 062 Cubic permutations

#=========================================================================================================================Solution
def get_min_permutation(n):        # 得到排列最小数
    return ''.join(sorted(str(n ** 3)))

min_dict = {}                       # 保存排列最小数和对应排列中cube的个数，从而不需要对每个三次方数重新排列
num_dict = {}                       # 保存每个三次方数对应的排列最小数和能够产生cube的排列最小数
cube = 1
while True:
    min_cube = get_min_permutation(cube)
    if min_cube not in min_dict:
        min_dict[min_cube] = 1
        num_dict[min_cube] = cube ** 3
        cube += 1
        continue
    min_dict[min_cube] += 1
    if min_dict[min_cube] == 5:
        print(num_dict[min_cube])
        break
    cube += 1