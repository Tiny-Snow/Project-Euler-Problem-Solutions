# Project Euler	Problem 039

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Integer right triangles

If $p$ is the perimeter of a right angle triangle with integral length sides, $\{a,b,c\}$, there are exactly three solutions for $p = 120$.
$$
\{20,48,52\}, \{24,45,51\}, \{30,40,50\}​
$$
For which value of $p ≤ 1000$, is the number of solutions maximised?



## Solution

这是一道关于勾股数的问题，我们下面介绍基于**勾股数组**的解法：

我们知道，勾股数 $a^2 + b^2 = c^2$ 可以表示为如下的式子：
$$
a = k(m^2 - n^2),b=2kmn,c=k(m^2+n^2)
$$
那么，勾股数组的和为：
$$
p =a + b + c = 2km(m+n)
$$
其中， $m>n \in \N_+,k\in \N_+$ 。

简单来说，只需要把这个式子全部遍历出来即可。遍历的步骤为：

- 首先确定 $k$ 为 $p/2$ 的一个因数。
- 再确定 $m$ 为 $p/2k$ 的一个因数，满足 $m<\sqrt {p/2k}$ 。
- 计算 $n$ ，满足 $n>0$ 且 $m>n$。

考虑到需要寻找因数，我们直接利用`Prime`类将因数列表导出，进一步提高效率。并且，由于因数至多为 $p/2$ ，因此只需要遍历 $p_{max}/2$ 中所有数的因数即可。

实现如下：

```python
#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P039')[0] + 'Utility Class')

from prime_utility import *

limit = 1000
prime_class = Prime(limit // 2)
prime_class._traverse()
prime_class._find_factor()
factor_list = prime_class._get_factor_list()

def get_setnum(origin_list):
    if origin_list == []:                # 注意空列表情况
        return 0
    num = 1
    for l in range(len(origin_list) - 1):
        flag = True
        for i in range(l + 1, len(origin_list)):
            if origin_list[l] == origin_list[i]:
                flag = False
        if flag == True:
            num += 1
    return num

max_solution = 0
p_ans = 0
for p in range(12, limit, 2):
    solution = 0
    solution_list = []
    for k in factor_list[p // 2]:
        for a in factor_list[p // (2 * k)]:
            if a > (p // (2 * k)) ** 0.5:
                break
            b = p // (2 * k * a) - a
            if a > b and b > 0:
                solution_list.append(list(sorted([k * (a ** 2 - b ** 2), 2 * k * a * b, k * (a ** 2 + b ** 2)])))
    solution = get_setnum(solution_list)
    if solution >= max_solution:
        p_ans = p
        max_solution = solution
print(p_ans)
#===============================================================Answer
The Answer is 840
```

