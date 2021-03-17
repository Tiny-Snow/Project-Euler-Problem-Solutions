# Project Euler	Problem 031

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Coin sums

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

​	1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

​	1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?



## Solution

本题就是一个多层的深度循环，如果寻求代码简短化的化应该利用**函数的循环调用**，也就是一种**DFS**，实现如下：

```python
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
#=======================================Answer
The Answer is 73682
```

