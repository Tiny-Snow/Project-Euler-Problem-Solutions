# Project Euler	Problem 070

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Totient permutation

Euler's Totient function, $φ(n)$ [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to $n$ which are relatively prime to $n$. For example, as $1, 2, 4, 5, 7$, and $8$, are all less than nine and relatively prime to nine, $φ(9)=6$.
The number 1 is considered to be relatively prime to every positive number, so $φ(1)=1$.

Interestingly, $φ(87109)=79180$, and it can be seen that $87109$ is a permutation of $79180$.

Find the value of $n$, $1 < n < 10^7$, for which $φ(n)$ is a permutation of n and the ratio $n/φ(n)$ produces a minimum.



## Solution

本题还是可以直接调用`Prime`类，当然运行时间较长，我的个人电脑运行时间长达75.66秒，这是因为我们另外重复算了素数幂次，而这在计算 $\varphi(n)$ 时是没有作用的，用埃拉托斯特尼筛法会更快（遍历时不断找到素数，并对含有该素因子的合数的 $\varphi(n)$ 修改，即逐步地做运算：$\varphi_{new}(n) = \varphi_{origin}(n) \times \left(1 - {1 \over  p}\right)$。

用`Prime`工具类实现如下：

```python
#===================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P070')[0] + 'Utility Class')

from prime_utility import *
limit = 10 ** 7
prime_class = Prime(limit)
prime_class._traverse()
prime_class._find_factor()

min_ratio = limit
ans_n = 0
for n in range(2, limit):
    euler = prime_class._euler_func(n)
    if len(str(euler)) != len(str(n)):
        continue
    if sorted(str(euler)) == sorted(str(n)):
        if min_ratio > n / euler:
            min_ratio = n / euler
            ans_n = n
print(ans_n)
#===================================================Answer
The Answer is 8319823
```

