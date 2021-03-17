# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 20 Feb 2021, 20:13
# Project Euler # 031 Coin sums

#=======================================Solution
ways = 0
coins = [200, 100, 50, 20, 10, 5, 2, 1]

def way(money, coin):
    if coin == 7:
        global ways
        ways += 1
        return
    i = 0
    while i * coins[coin] <= money:
        way(money - i * coins[coin], coin + 1)
        i += 1

way(200, 0)
print(ways)