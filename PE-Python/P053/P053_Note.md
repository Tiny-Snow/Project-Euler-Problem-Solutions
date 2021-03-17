# Project Euler	Problem 053

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Combinatoric selections

There are exactly ten ways of selecting three from five, $12345$:

$$
123, 124, 125, 134, 135, 145, 234, 235, 245, and\ 345
$$
In combinatorics, we use the notation, $\left({\begin{array}{l}{5}\\{3}\end{array}}\right)=10$.

In general, 
$$
\left({\begin{array}{l}{n}\\{r}\end{array}}\right)={n!\over r!(n-r)!}
$$
where $r≤n, n!=n×(n−1)×...×3×2×1$, and $0!=1$.

It is not until $n=23$, that a value exceeds one-million: $\left({\begin{array}{l}{23}\\{10}\end{array}}\right)=1144066$.

How many, not necessarily distinct, values of $\left({\begin{array}{l}{n}\\{r}\end{array}}\right)$ for $1≤n≤100$, are greater than one-million?



## Solution

本题不是很困难，计算组合数调用`scipy.special.comb`方法，遍历考虑如下的事实：

显然有 $C_{n+1}^r>C_n^r$ ，也就是说，当 $C_n^r > 1000000$ 时，必然有 $C_{n+1}^r > 1000000$ 。因此，我们只需要找到对于 $n$ 满足条件的 $r$ 的区间 $[left, right]$ ，那么该区间内的 $r$ 必然也对 $n+1$ 满足条件。因此，我们就可以不遍历这一区间的 $r$ ，从而大幅减小遍历次数。

依据上述规则实现的算法如下：

```python
#==============================================Solution
import itertools
from scipy.special import comb

origin = 1
while comb(origin, origin // 2) <= 1000000:
    origin += 1
left = origin // 2
right = origin // 2 + 1
greater_num = 2
for l in reversed(range(0, left)):
    if comb(origin, l) < 1000000:
        break
    left = l
    greater_num += 1
for r in range(right + 1, origin + 1):
    if comb(origin, r) < 1000000:
        break
    right = r
    greater_num += 1

for n in range(origin + 1, 100 + 1):
    greater_num += (right - left + 1)
    for l in reversed(range(0, left)):
        if comb(n, l) < 1000000:
            break
        left = l
        greater_num += 1
    for r in range(right + 1, n + 1):
        if comb(n, r) < 1000000:
            break
        right = r
        greater_num += 1
print(greater_num)
#==============================================Answer
The Answer is 4075
```

