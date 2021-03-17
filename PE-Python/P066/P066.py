# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Thu, 4 Mar 2021, 00:03
# Project Euler # 066 Diophantine equation

#===================================================Solution
from fractions import Fraction
from math import sqrt

def get_state_list(n):
    a = int(sqrt(n))
    x = a
    y = 1
    state0 = [a, x, y]
    a = int(y / (sqrt(n) - x))
    x0 = x
    x = int(a * (n - x0 ** 2) / y - x0)
    y = int((n - x0 ** 2) / y)
    state1 = [a, x, y]
    state_list = [state0, state1]
    while True:
        a = int(y / (sqrt(n) - x))
        x0 = x
        x = int(a * (n - x0 ** 2) / y - x0)
        y = int((n - x0 ** 2) / y)
        state = [a, x, y]
        if state in state_list:
            break
        state_list.append(state)
    return state_list

def get_fraction(state_list):
    a = state_list[0][0]
    p0 = a
    q0 = 1
    p1 = a * state_list[1][0] + 1
    q1 = state_list[1][0]
    if len(state_list) == 2:
        i = 1
    else:
        i = 2
    while p1 ** 2 - D * (q1 ** 2) != 1:
        p1, p0 = state_list[i][0] * p1 + p0, p1
        q1, q0 = state_list[i][0] * q1 + q0, q1
        if i == len(state_list) - 1:
            i = 1
        else:
            i += 1
    frac = Fraction(p1, q1)
    return frac

ans_x = 0
ans_D = 0
for D in range(1, 1000):
    if sqrt(D) == int(sqrt(D)):
        continue
    D_state_list = get_state_list(D)
    D_frac = get_fraction(D_state_list)
    x = D_frac._numerator
    if x > ans_x:
        ans_x = x
        ans_D = D
print(ans_D)