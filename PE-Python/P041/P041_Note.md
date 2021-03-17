# Project Euler	Problem 041

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Pandigital prime

We shall say that an $n$-digit number is pandigital if it makes use of all the digits 1 to $n$ exactly once. For example, $2143$ is a 4-digit pandigital and is also prime.

What is the largest $n$-digit pandigital prime that exists?



## Solution

本题需要调用两个模块来方便我们的计算：一个自然是素数处理`Prime`类，遍历素数；另一个是`itertools`模块，调用其中的排列组合相关功能。

本题的关键在于确定遍历范围`limit`，肯定不能让范围达到 $10^9$ 之巨，我们需要用一些数学手段。

我们知道，*n-digit number* 的最大特点是其各位数字为 $1$ 到 $n$ ，能否利用该特点判断该数是否是素数呢？最好的方法是寻找**和 $n$ 相关的数论性质**。对于各位数字，我们知道 $\mod 9$ 是最方便的，直接将原数同余为数字和——而其**数字和是固定的**！那么 $1$ 到 $n$ 的任意一个排列满足： 
$$
(12···n) \equiv 1 + 2 + ··· + n\equiv n(n+1)/2\mod 9
$$
当然，由于我们希望排除更多的 $n$ ，进一步取 $\mod 3$ ：
$$
(12···n) \equiv n(n+1)/2\mod 3
$$
考虑以下结果：

<table>
    <tr>
        <th align = "center">n</th>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
        <td>7</td>
        <td>8</td>
        <td>9</td>
    </tr>
    <tr>
        <th align = "center">n(n+1)/2</th>
        <td>1</td>
        <td>3</td>
        <td>6</td>
        <td>10</td>
        <td>15</td>
        <td>21</td>
        <td>28</td>
        <td>36</td>
        <td>45</td>
    </tr>    
</table>

因此，我们只需要考虑 $n = 1,4,7$ 的情况即可。

实现如下：

```python
#=============================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P041')[0] + 'Utility Class')

from prime_utility import *
limit = 10 ** 7             # n = 1, 4, 7
prime_class = Prime(limit)
prime_class._traverse()

import itertools

def find_prime(n):
    max_prime = 0
    for p_tuple in list(itertools.permutations([i for i in range(1, n + 1)], n)):
        p = ''
        for i in p_tuple:
            p += str(i)
        if prime_class._is_prime(int(p)) == True:
            max_prime = max(max_prime, int(p))
    return max_prime

ans = max(find_prime(1), find_prime(4), find_prime(7))
print(ans)
#=============================================================================Answer
The Answer is 7652413
```

