# Project Euler	Problem 072

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Counting fractions

Consider the fraction, $n/d$, where $n$ and $d$ are positive integers. If $n<d$ and $HCF(n,d)=1$, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for $d ≤ 8$ in ascending order of size, we get:
$$
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
$$
It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for $d ≤ 1,000,000$?



## Solution

显然，**最简分数的个数就是分母的欧拉函数**，直接调`Prime`工具类即可。

实现如下：

```python
#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P072')[0] + 'Utility Class')

from prime_utility import *
limit = 10 ** 6
prime_class = Prime(limit)
prime_class._traverse()
prime_class._find_factor()

num = 0
for d in range(2, limit + 1):
    num += prime_class._euler_func(d)
print(num)
#===============================================================Answer
The Answer is 303963552391
```

