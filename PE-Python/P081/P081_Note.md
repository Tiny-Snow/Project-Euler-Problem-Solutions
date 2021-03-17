# Project Euler	Problem 081

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by **only moving to the right and down**, is indicated in bold red and is equal to $2427$.
$$
\begin{pmatrix}
\color{red}{131} & 673 & 234 & 103 & 18\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
630 & 803 & \color{red}{746} & \color{red}{422} & 111\\
537 & 699 & 497 & \color{red}{121} & 956\\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}
$$
Find the minimal path sum from the top left to the bottom right by only moving right and down in [matrix.txt](https://projecteuler.net/project/resources/p081_matrix.txt) (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.



## Solution

这是一道十分经典的动态规划问题。由于起点和终点是固定的，使用一个 $n \times n$ 的数组储存从终点开始到达相应位置的最短路径长度，实现如下：

```python
#======================================================================================Solution
import os
BSER_DIR = os.path.dirname(os.path.abspath(__file__))

n = 80
data_list = []
with open(BSER_DIR + '\p081_matrix.txt', mode = 'r') as datafile:
    for _ in range(n):
        data_list.append(list(map(int, datafile.readline().split(','))))

DP_list = data_list.copy()                      # DP_list储存每个位置到达右下角的最短路径
# 末列和末行只有一种选择
for i in reversed(range(n - 1)):
    DP_list[n - 1][i] += DP_list[n - 1][i + 1]
    DP_list[i][n - 1] += DP_list[i + 1][n - 1]
# 其余位置均有两种选择
for i in reversed(range(n - 1)):
    for j in reversed(range(n - 1)):
        DP_list[i][j] += min(DP_list[i][j + 1], DP_list[i + 1][j])
print(DP_list[0][0])
#======================================================================================Answer
The Answer is 427337
```

