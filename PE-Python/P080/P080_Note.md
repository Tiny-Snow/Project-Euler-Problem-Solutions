# Project Euler	Problem 080

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Square root digital expansion

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is $1.41421356237309504880...$, and the digital sum of the first one hundred decimal digits is $475$.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.



## Solution

在[Problem 066](../P066/P066_Note.md)中，我们详细展示了如何利用连分数理论，使用分数来逼近 $\sqrt{D}$ 。

但是，本题要求我们处理的是小数。那么，怎么**在Python中进行分数和小数之间的转换呢**？我们结合`fractions`模块和`decimal`模块来实现这一转换，实现如下：

```python
from fractions import Fraction
from decimal import Decimal

frac = Fraction(1, 3)
deci = Decimal(frac._numerator) / Decimal(frac._denominator)
```

通过**设置精度**，我们能够实现小数间的精确运算：

```python
getcontext().prec = ...
```

既然我们能够进行小数的精确运算了，事实上也没必要运用连分数了，我们直接设置相应精度，实现如下：

```python
#====================================================Solution
from decimal import *

getcontext().prec = 110         # 设置精度为110
digit_sum = 0
for D in range(1, 100 + 1):
    if D ** 0.5 == int(D ** 0.5):
        continue
    digit = str(Decimal(D).sqrt())[:101]
    for i in digit:
        if i != '.':
            digit_sum += int(i)
print(digit_sum)
#====================================================Answer
The Answer is 40886
```

