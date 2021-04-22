# Project Euler	Problem 085

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Counting rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

![img](P085_Note.assets/p085.png)

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.



## Solution

本问题是很简单的组合计数问题。考虑在 $m \times n$ 的长方形中分割出 $i \times j$ 大小的长方形，有 $(m - i + 1)(n - j + 1)$ 种分割方法。

因此，计数有：
$$
\sum_{i = 1}^{m}\sum_{j = 1}^{n}(m - i + 1)(n - j + 1) = \sum_{i = 1}^{m}\sum_{j = 1}^{n}ij = {m(m + 1)n(n + 1) \over 4}
$$
因此，立刻得到如下实现：

```python
#=============================================================Solution
def get_rectangles(m, n):
    return m * (m + 1) * n * (n + 1) // 4

diff = 10000
area = 0
for m in range(1, int(2 * (2 ** 0.5) * 10 * 3) + 1):
    for n in range(m, int(2 * (2 ** 0.5) * 10 * 3) + 1):
        if abs(get_rectangles(m, n) - 2 * (10 ** 6)) < diff:
            area = m * n
            diff = abs(get_rectangles(m, n) - 2 * (10 ** 6))
print(area)
#=============================================================Answer
The Answer is 2772
```

