# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 27 Jan 2021, 20:32
# Project Euler # 002 Even Fibonacci numbers

#================================Solution 1
f1 = 1
f2 = 2
sum = 2
while f1 + f2 <= 4000000:
    if (f1 + f2) % 2 == 0:
        sum += (f1 + f2)
    f1, f2 = f2, f1 + f2
print(sum)

#================================Solution 2
fn_6 = 2
fn_3 = 8
fn = 4 * fn_3 + fn_6
sum = 0
while fn <= 400000:
    sum += fn
    fn_6, fn_3 = fn_3, fn
print(sum)