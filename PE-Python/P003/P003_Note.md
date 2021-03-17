# Project Euler	Problem 003

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Largest prime factor

The prime factors of $13195$ are $5$, $7$, $13$ and $29$.

What is the largest prime factor of the number $600851475143$ ?



## Solution

解决本问题的关键在于熟练利用一些遍历素因数的结论。我们使用以下的思路：

**思路**	从小到大遍历 $[0,[\sqrt n]$ 中的数 $p$ ，如果 $p|n$ ，就将 $n$ 的 $p$ 幂次全部除尽。能够保证：每次得到的 $p$ 一定为 $n$ 的素因数。

证明是显然的，既然我们是从小到大遍历的，我们就将素因数展开中每个素因数的幂次全部除去了。

这种做法最终将会遍历完 $[0,[\sqrt n]$ ，最终得到一个余下的数 $m$ 。显然，不可能存在两个大于 $\sqrt n$ 的素因子，一个大于 $\sqrt n$ 的素因子的幂次也只能为 $1$ 。因此，余下的 $m$ 最终只可能是最大的素因数（有可能就是 $n$ 本身），或是 $1$ 。



基于上述思路，我们得到以下算法：

```python
#====================================Solution
from math import *

n = 600851475143
p_list = []
for i in range(3, int(sqrt(n)), 2):
    if n % i == 0:
        p_list.append(i)
        while n % i == 0:
            n /= i
print(max(n, max(p_list)))

#====================================Answer
The Answer is 6857
```