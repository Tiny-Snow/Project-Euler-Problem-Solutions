# Project Euler	Problem 078

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Coin partitions

Let $p(n)$ represent the number of different ways in which $n$ coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so $p(5)=7$.
$$
\begin{array}{l}
{OOOOO}\\
{OOOO\ \ O}\\
{OOO\ \ OO}\\
{OOO\ \ O\ \ O}\\
{OO\ \ OO\ \ O}\\
{OO\ \ O\ \ O\ \ O}\\
{O\ \ O\ \ O\ \ O\ \ O}
\end{array}
$$
Find the least value of $n$ for which $p(n)$ is divisible by one million.



## Solution

我们现在使用[Problem 076](../P076/P076_Note.md)中欧拉提供的 *generating function* ，实现如下：

```python
#=================================================================================Solution
partition_dict = {0: 1, 1: 1}
n = 2
while True:
    sum_p = 0
    for k in range(-int(((24 * n + 1) ** 0.5 - 1) / 6), int(((24 * n + 1) ** 0.5 + 1) / 6) + 1):
        if k == 0:
            continue
        sum_p += int(((-1) ** (k + 1))) * partition_dict[int(n - k * (3 * k - 1) // 2)]
    partition_dict[n] = sum_p
    if str(sum_p)[-6:] == '000000':
        print(n)
        break
    n += 1
#=================================================================================Answer
The Answer is 55374
```

