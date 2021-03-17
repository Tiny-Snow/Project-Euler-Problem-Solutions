# Project Euler	Problem 057

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Square root convergents

It is possible to show that the square root of two can be expressed as an infinite continued fraction.
$$
\sqrt 2=1+{1 \over 2+{1 \over 2 + {1 \over 2+…}}}
$$
By expanding this for the first four iterations, we get:
$$
1+{1 \over 2}={3 \over 2}=1.5\\
1+{1 \over 2+{1 \over 2}}={7\over 5}=1.4\\
1+{1 \over 2 + {1 \over 2+{1 \over 2}}}={17 \over 12}=1.41666…\\
1+{1 \over 2+{1 \over 2+{1 \over 2+{1 \over 2}}}}={41\over29}=1.41379…
$$
The next three expansions are ${99 \over 70},{ 239\over169}$, and $577\over408$, but the eighth expansion, $1393\over985$, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?



## Solution

我们调用Python的`fractions`模块，使用分数类`Fraction`来方便地表示分数，按照递归式实现如下：

```python
#=================================================Solution
from fractions import Fraction

numerator_more_digits = 0
denominator = Fraction(2, 1)
for i in range(1000):
    num = Fraction(1, 1) + Fraction(1, denominator)
    denominator = Fraction(2, 1) + Fraction(1, denominator)
    if len(str(num.numerator)) > len(str(num.denominator)):
        numerator_more_digits += 1
print(numerator_more_digits)
#=================================================Answer
The Answer is 153
```

