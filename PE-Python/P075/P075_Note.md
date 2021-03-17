# Project Euler	Problem 075

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Singular integer right triangles

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
$$
\begin{array}{l}
{\textbf{12 cm}: (3,4,5)}\\
{\textbf{24 cm}: (6,8,10)}\\
{\textbf{30 cm}: (5,12,13)}\\
{\textbf{36 cm}: (9,12,15)}\\
{\textbf{40 cm}: (8,15,17)}\\
{\textbf{48 cm}: (12,16,20)}
\end{array}
$$
In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
$$
\begin{array}{l}
{\textbf{120 cm}: (30,40,50), (20,48,52), (24,45,51)}
\end{array}
$$
Given that $L$ is the length of the wire, for how many values of $L ≤ 1,500,000$ can exactly one integer sided right angle triangle be formed?



## Solution

沿用[Problem 039](../P039/P039_Note.md)的勾股数组算法，结合一般列表的去重方法，实现如下：

```python
#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P075')[0] + 'Utility Class')

from prime_utility import *

limit = 1500000
prime_class = Prime(limit // 2)
prime_class._traverse()
prime_class._find_factor()
factor_list = prime_class._get_factor_list()

def set_list(origin_list):              # 列表去重
    if origin_list == []:
        return []
    new_list = []
    for i in range(len(origin_list)):
        if origin_list[i] not in new_list:
            new_list.append(origin_list[i])
    return new_list


num = 0
for p in range(12, limit, 2):
    solutions = []
    for k in factor_list[p // 2]:
        for a in factor_list[p // (2 * k)]:
            if a > (p // (2 * k)) ** 0.5:
                break
            b = p // (2 * k * a) - a
            if a > b and b > 0:
                solutions.append(list(sorted([k * (a ** 2 - b ** 2), 2 * k * a * b, k * (a ** 2 + b ** 2)])))
    solutions = set_list(solutions)
    if len(solutions) == 1:
        num += 1
print(num)
#===============================================================Answer
The Answer is 161667
```

