# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 30 Mar 2021, 20:56
# Project Euler # 086 Cuboid route

#=================================================================================Solution
int_len_num = 0
a = 0
while int_len_num <= 10 ** 6:
    a += 1
    for sum_bc in range(2, 2 * a + 1):
        if (a ** 2 + (sum_bc) ** 2) ** 0.5 == int((a ** 2 + (sum_bc) ** 2) ** 0.5):
            if sum_bc > a + 1:
                if sum_bc % 2 == 0:
                    int_len_num += a - sum_bc // 2 + 1
                else:
                    int_len_num += a - (sum_bc - 1) // 2
            else:
                int_len_num += sum_bc // 2
print(a)