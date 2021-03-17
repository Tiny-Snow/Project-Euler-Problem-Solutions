# Project Euler	Problem 047

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:
$$
14 = 2 × 7\\
15 = 3 × 5
$$
The first three consecutive numbers to have three distinct prime factors are:
$$
644 = 2^2× 7 × 23\\
645 = 3 × 5 × 43\ \ \\
646 = 2 × 17 × 19
$$
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?



## Solution

直接调用`Prime`素数工具类获得苏因子个数即可。实现如下：

```python
#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P047')[0] + 'Utility Class')

from prime_utility import *
limit = 200000
prime_class = Prime(limit)
prime_class._traverse()
prime_class._find_factor()
prime_factor_list = prime_class._get_prime_factor_list()

for n in range(647, limit):
    flag = True
    for i in range(4):
        if len(prime_factor_list[n + i]) != 4:
            flag = False
            break
    if flag == True:
        print(n)
        break
```

