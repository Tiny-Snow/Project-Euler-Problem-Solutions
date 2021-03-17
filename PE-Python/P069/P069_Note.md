# Project Euler	Problem 069

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Totient maximum

Euler's Totient function, $φ(n)$ [sometimes called the *phi function*], is used to determine the number of numbers less than $n$ which are relatively prime to $n$. For example, as $1, 2, 4, 5, 7$, and $8$, are all less than nine and relatively prime to nine, $φ(9)=6$.

| n    | Relatively Prime | φ(n) | n/φ(n)    |
| ---- | ---------------- | ---- | --------- |
| 2    | 1                | 1    | 2         |
| 3    | 1,2              | 2    | 1.5       |
| 4    | 1,3              | 2    | 2         |
| 5    | 1,2,3,4          | 4    | 1.25      |
| 6    | 1,5              | 2    | 3         |
| 7    | 1,2,3,4,5,6      | 6    | 1.1666... |
| 8    | 1,3,5,7          | 4    | 2         |
| 9    | 1,2,4,5,7,8      | 6    | 1.5       |
| 10   | 1,3,7,9          | 4    | 2.5       |

It can be seen that *n*=6 produces a maximum $n/φ(n)$ for $n ≤ 10$.

Find the value of $n ≤ 1,000,000$ for which $n/φ(n)$ is a maximum.



## Solution

计算欧拉函数，可以直接调用`Prime`工具类，实现如下：

```python
#===================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P069')[0] + 'Utility Class')

from prime_utility import *
limit = 1000000
prime_class = Prime(limit)
prime_class._traverse()
prime_class._find_factor()

max_euler = 0
for n in range(2, limit + 1):
    euler = prime_class._euler_func(n)
    if n / euler > max_euler:
        max_euler = n / euler
        ans_n = n
print(ans_n)
#===================================================Answer
The Answer is 510510
```