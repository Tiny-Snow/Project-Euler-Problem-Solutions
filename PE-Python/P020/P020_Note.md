# Project Euler	Problem 020

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Factorial digit sum

$n!$ means $*n* × (*n* − 1) × ... × 3 × 2 × 1$

For example, $10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800$,
and the sum of the digits in the number $10!$ is  $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$.

Find the sum of the digits in the number $100!$



## Solution

对于阶乘，我们直接调用Python的`math`模块中的`factorial`方法计算，速度很快。

```python
#============================Solution
from math import *
num_str = str(factorial(100))
num_sum = 0
for i in num_str:
    num_sum += int(i)
print(num_sum)
#============================Answer
The Answer is 648
```

当然可能会有一些另外的考虑，例如去掉所有的 $10$ 的幂次，这是因为计算时不用考虑 $0$。这一考虑可以用十分简单的方法实现：因为 $5$ 的因子数总是少于2的因字数，因此有 $5$ 就可以除去（实际上是除以 $10$），这样也可以减小数字大小，节约空间。

鉴于上述算法并没有实际上的必要性，我们在这里不给出实现。