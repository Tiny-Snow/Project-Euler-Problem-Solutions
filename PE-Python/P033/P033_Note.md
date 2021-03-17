# Project Euler	Problem 033

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Digit cancelling fractions

The fraction $49/98$ is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that $49/98 = 4/8$, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, $30/50 = 3/5$, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.



## Solution

事实上本题就是要求找到形如 $AB/BC$ 的分数，满足该分数 $< 1$ ，并且 $AB/BC = A/C$ 。我们甚至可以通过一些数学分析让 $A,B,C$ 的区间变得更小，但是没必要，简单遍历即可。

需要注意的是小心分母为0的情况（也即 $C$ 为0的情况），并且要考虑**乘积**`product`**不能够使用浮点运算**。具体实现如下：

 ```python
#====================================================================Solution
from math import *

def is_curious(m, n):
    flag = False
    if str(m)[1] == str(n)[0] and str(n)[1] != '0':
        if int(str(m)[0]) / int(str(n)[1]) == m / n:
            flag = True
    return flag

product_numerator = 1
product_denominator = 1

for m in range(10, 100):
    for n in range(m + 1, 100):
        if m % 10 == 0 and n % 10 == 0:
            continue
        if is_curious(m, n) == True:
            product_numerator *= m
            product_denominator *= n

print(product_denominator // gcd(product_denominator, product_numerator))
#====================================================================Answer
The Answer is 100
 ```

