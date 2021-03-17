# Project Euler	Problem 009

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, $a < b < c$, for which,
$$
a^2 + b^2 = c^2
$$
For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.

There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.
Find the product $abc$.



## Solution

本问题的算法是基础的，关键在于如何能够借助不等式去约束范围。

由 $a + b + c = 1000$ 易知：
$$
10^6 = (a+b+c)^2 = a^2 + b^2 + c^2 + 2c(a+b) +2ab = 2c^2 + 2c(1000-c) + 2ab = 2000c +2ab
$$
显然由上式可知：$c < 500$ 。

由 $AM-GM$ 不等式：
$$
10^6 = 2000c +2ab \leq 2000c + {{1}\over{2}}(a+b)^2 \leq 2000c + {{1}\over{2}}(1000-c)^2
$$
解上述一元二次方程得：$c > 250(\sqrt 5 - 1)$ 。

根据上述约束，我们就可以在一个小得多的区间尝试了。代码如下：

```python
#==================================================Solution
for c in range(int(250 * (5 ** 0.5 - 1)), 500):
    for a in range(1, 1000 - c):
        b = 1000 - a - c
        if a ** 2 + b ** 2 == c ** 2:
            print(a * b * c)
            break
#==================================================Answer
The Answer is 31875000
```