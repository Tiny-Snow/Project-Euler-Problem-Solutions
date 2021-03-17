# Project Euler	Problem 071

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Ordered fractions

Consider the fraction, $n/d$, where $n$ and $d$ are positive integers. If $n<d$ and $HCF(n,d)=1$, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for $d ≤ 8$ in ascending order of size, we get:
$$
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, \textbf{2/5}, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
$$
It can be seen that 2/5 is the fraction immediately to the left of $3/7$.

By listing the set of reduced proper fractions for $d ≤ 1,000,000$ in ascending order of size, find the numerator of the fraction immediately to the left of $3/7$.



## Solution

解决方法并不复杂，我们的思路是不断地遍历和比较，更新最小差和分数结果。减小多余遍历的关键在于选定遍历起点和方向。

我们知道，由于要使得 $n/d$ 与 $3/7$ 尽可能接近，那么应当从 $n = 3n/7$ 开始从大到小地遍历，筛选到最简分数后立即停止 $n$ 的遍历。

实现如下：

```python
#===================================================Solution
from fractions import Fraction
from math import gcd

diff = 1
ans_frac = Fraction(0, 1)
for d in range(1, 1000000 + 1):
    for n in reversed(range(1, int(3 * d / 7))):
        if (Fraction(2, 5) - Fraction(n, d)) > diff:
            break
        if gcd(n, d) == 1:
            ans_frac = Fraction(n, d)
            diff = Fraction(2, 5) - Fraction(n, d)
            break
print(ans_frac._numerator)
#===================================================Answer
The Answer is 428570
```

