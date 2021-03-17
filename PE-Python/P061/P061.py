# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sun, 28 Feb 2021, 14:12
# Project Euler # 061 Cyclical figurate numbers

#=====================================================================Solution
triangle_list = []
n = 0
while n * (n + 1) // 2 < 10000:
    if n * (n + 1) // 2 >= 1000:
        triangle_list.append(n * (n + 1) // 2)
    n += 1

square_list = []
n = 0
while n ** 2 < 10000:
    if n ** 2 >= 1000:
        square_list.append(n ** 2)
    n += 1

pentagonal_list = []
n = 0
while n * (3 * n - 1) // 2 < 10000:
    if n * (3 * n - 1) // 2 >= 1000:
        pentagonal_list.append(n * (3 * n - 1) // 2)
    n += 1

hexagonal_list = []
n = 0
while n * (2 * n - 1) < 10000:
    if n * (2 * n - 1) >= 1000:
        hexagonal_list.append(n * (2 * n - 1))
    n += 1

heptagonal_list = []
n = 0
while n * (5 * n - 3) // 2 < 10000:
    if n * (5 * n - 3) // 2 >= 1000:
        heptagonal_list.append(n * (5 * n - 3) // 2)
    n += 1

octagonal_list = []
n = 0
while n * (3 * n - 2) < 10000:
    if n * (3 * n - 2) >= 1000:
        octagonal_list.append(n * (3 * n - 2))
    n += 1

def find_ans(l1, l2, l3, l4, l5, l6):
    for n6 in l6:
        for n1 in l1:
            if int(str(n1)[:2]) > int(str(n6)[2:]):
                break
            if int(str(n1)[:2]) < int(str(n6)[2:]):
                continue
            for n2 in l2:
                if int(str(n2)[:2]) > int(str(n1)[2:]):
                    break
                if int(str(n2)[:2]) < int(str(n1)[2:]):
                    continue
                for n3 in l3:
                    if int(str(n3)[:2]) > int(str(n2)[2:]):
                        break
                    if int(str(n3)[:2]) < int(str(n2)[2:]):
                        continue
                    for n4 in l4:
                        if int(str(n4)[:2]) > int(str(n3)[2:]):
                            break
                        if int(str(n4)[:2]) < int(str(n3)[2:]):
                            continue
                        for n5 in l5:
                            if int(str(n5)[:2]) > int(str(n4)[2:]):
                                break
                            if int(str(n5)[:2]) < int(str(n4)[2:]):
                                continue
                            if int(str(n6)[:2]) == int(str(n5)[2:]):
                                return sum([n1, n2, n3, n4, n5, n6])

import itertools
for l in itertools.permutations([triangle_list, square_list, pentagonal_list, hexagonal_list, heptagonal_list, octagonal_list], 6):
    ans = find_ans(l[0], l[1], l[2], l[3], l[4], l[5])
    if ans != None:
        print(ans)
        break