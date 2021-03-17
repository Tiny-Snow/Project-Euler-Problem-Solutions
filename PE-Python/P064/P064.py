# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Tue, 2 Mar 2021, 20:34
# Project Euler # 064 Odd period square roots

#=====================================================================Solution
from math import sqrt, gcd

def is_odd(n):
    a = int(sqrt(n))
    x = a
    y = 1
    a = int(y / (sqrt(n) - x))
    x0 = x
    x = int(a * (n - x0 ** 2) / y - x0)
    y = int((n - x0 ** 2) / y)
    state0 = [a, x, y]
    state_list = [state0]
    while True:
        a = int(y / (sqrt(n) - x))
        x0 = x
        x = int(a * (n - x0 ** 2) / y - x0)
        y = int((n - x0 ** 2) / y)
        state = [a, x, y]
        if state in state_list:
            break
        state_list.append(state)
    if state == state0 and len(state_list) % 2 != 0:
        return True
    return False

all_odd = 0
for n in range(2, 10000 + 1):
    if sqrt(n) == int(sqrt(n)):
        continue
    if is_odd(n) == True:
        all_odd += 1
print(all_odd)