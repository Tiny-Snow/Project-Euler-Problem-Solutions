# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 22 Feb 2021, 13:00
# Project Euler # 044 Pentagon numbers

#================================================================================================================================Solution
def is_pentagon(num):
    n = int(((2 / 3) * num) ** 0.5) + 1
    if n * (3 *n - 1) == 2 * num:
        return True
    return False

pentagon_list = []
limit = 10000
for n in range(1, limit + 1):
    pentagon_list.append(n * (3 * n - 1) // 2)

min_diff = pentagon_list[limit - 1] - pentagon_list[0]

for k in range(2, limit):
    if pentagon_list[k] - pentagon_list[k - 1] > min_diff:      # 考虑相邻两个pentagon number之差已经超过min_diff的情况，终止k的遍历
        break
    for j in reversed(range(1, k)):
        if pentagon_list[k] - pentagon_list[j] > min_diff:      # 考虑遍历时p[k] - p[j]之差已经超过min_diff，跳出j的遍历
            break
        if is_pentagon(pentagon_list[k] - pentagon_list[j]) == True and is_pentagon(pentagon_list[k] + pentagon_list[j]) == True:
            min_diff = min(min_diff, pentagon_list[k] - pentagon_list[j])
print(min_diff)