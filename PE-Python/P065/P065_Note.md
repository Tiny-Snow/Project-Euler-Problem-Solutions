# Project Euler	Problem 065

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Convergents of e

The square root of 2 can be written as an infinite continued fraction.

$$
\sqrt 2 = 1 + {1 \over 2 + {1 \over 2 + {1 \over 2 + {1 \over 2 +…}}}}
$$
The infinite continued fraction can be written, $\sqrt 2=[1;(2)]$, $(2)$ indicates that $2$ repeats *ad infinitum*. In a similar way, $\sqrt {23}=[4;(1,3,1,8)]$.

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for 2.

$$
1+{1 \over 2} = {3 \over 2}\\
1 + {1 \over 2 + {1 \over 2}} = {7 \over 5}\\
1 + {1 \over 2 + {1 \over 2 + {1 \over 2}}}={17 \over 12}\\
1 + {1 \over 2 + {1 \over 2 + {1 \over 2 + {1 \over2}}}} = {41 \over 29}
$$
Hence the sequence of the first ten convergents for $\sqrt 2$ are:

$$
1,{3 \over 2},{7 \over 5},{17 \over 12},{41\over 29},{99 \over 70},{239 \over 169},{577 \over 408},{1393 \over 985},{3363 \over 2378},...
$$
What is most surprising is that the important mathematical constant,
$$
e=[2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].​
$$
The first ten terms in the sequence of convergents for $e$ are:

$$
2,3,{8 \over 3},{11 \over 4},{19 \over 7},{87 \over 32},{106 \over 39},{193 \over 71},{1264 \over 465},{1457 \over 536},...
$$
The sum of digits in the numerator of the 10th convergent is $1+4+5+7=17$.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for $e$.



## Solution

从底部开始算连分数，很容易得出相应结果。实现如下：

```python
#===================================================Solution
from fractions import Fraction

num_list = [2]
for k in range(1, 34):
    num_list.append(1)
    num_list.append(2 * k)
    num_list.append(1)

p = len(num_list) - 1
e = Fraction(1, num_list[p])
p -= 1
while p > 0:
    e += num_list[p]
    e = Fraction(1, e)
    p -= 1
e += num_list[p]

sum = 0
for i in str(e._numerator):
    sum += int(i)
print(sum)
#===================================================Answer
The Answer is 272
```

