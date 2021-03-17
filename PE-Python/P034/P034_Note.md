# Project Euler	Problem 034

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Digit factorials

$145$ is a curious number, as $1! + 4! + 5! = 1 + 24 + 120 = 145$.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As $1! = 1$ and $2! = 2$ are not sums they are not included.



## Solution

难点在于确定遍历范围。我们知道，随着位数的增加，一边是 $max = k \times9! $ ，一边是 $min = 10^k$ ，显然右式很快就会超过左式。简单计算一下会发现 $k=7$ 的时候就会超过了，也就是说上界至多为6位数。

事实上，我们甚至没必要取上界为`1000000`，考虑 $k=6$ 的时候，$max = 6 \times 9! =2177280$ ，取该数为上界即可。

实现如下：

```python
#================================Solution
from math import *

maxn = 2177280
all_sum = 0
for i in range(10, maxn):
    sum = 0
    for j in str(i):
        sum += factorial(int(j))
    if sum == i:
        all_sum += i
print(all_sum)
```

