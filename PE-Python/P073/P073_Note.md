# Project Euler	Problem 073

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Counting fractions in a range

Consider the fraction, $n/d$, where $n$ and $d$ are positive integers. If $n<d$ and $HCF(n,d)=1$, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for $d ≤ 8$ in ascending order of size, we get:
$$
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, \textbf{3/8}, \textbf{2/5}, \textbf{3/7}, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
$$
It can be seen that there are 3 fractions between $1/3$ and $1/2$.

How many fractions lie between $1/3$ and $1/2$ in the sorted set of reduced proper fractions for $d ≤ 12,000$?



## Solution

本题还是找到合适的区间遍历，实现如下：

```python
#===================================================Solution
from math import gcd

num = 0
for d in range(4, 12000 + 1):
    for n in range(int(d / 3) + 1, int(d / 2) + 1):
        if gcd(n, d) == 1:
            num += 1
print(num)
#===================================================Answer
The Answer is 7295372
```

