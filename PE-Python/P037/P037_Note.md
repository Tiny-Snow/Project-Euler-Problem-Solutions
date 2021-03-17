# Project Euler	Problem 037

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Truncatable primes

The number $3797$ has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: $3797, 797, 97$, and $7$. Similarly we can work from right to left: $3797, 379, 37$, and $3$.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: $2, 3, 5$, and $7$ are not considered to be truncatable primes.



## Solution

本题的难点在于确定素数的遍历范围，但是似乎并没有什么特别好的方法。一种方法是在用欧拉线性筛法筛素数的同时，检查该素数是否是*Truncatable primes*，但是从性能上来说并没有必要去改变底层算法。

下面的实现仍然是利用`Prime`素数工具类完成的：

```python
#================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P037')[0] + 'Utility Class')

from prime_utility import *

limit = 1000000
prime_sum = 0
prime_num = 0
prime_class = Prime(limit)
prime_class._traverse()
prime_list = prime_class._get_prime_list()[4: ]

for p in prime_list:
    if prime_num == 11:
        break
    flag = True
    l = len(str(p))
    for i in range(1, l):
        if prime_class._is_prime(int(str(p)[i: l])) == False:
            flag = False
            break
        if prime_class._is_prime(int(str(p)[: -i])) == False:
            flag = False
            break
    if flag == True:
        prime_sum += p
        prime_num += 1

print(prime_sum)
#================================================================Answer
The Answer is 748317
```

