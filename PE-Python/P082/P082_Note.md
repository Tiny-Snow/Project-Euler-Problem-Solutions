# Project Euler	Problem 082

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Path sum: three ways

NOTE: This problem is a more challenging version of [Problem 81](https://projecteuler.net/problem=81).

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.
$$
\begin{pmatrix}
131 & 673 & \color{red}{234} & \color{red}{103} & \color{red}{18}\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & 150\\
630 & 803 & 746 & 422 & 111\\
537 & 699 & 497 & 121 & 956\\
805 & 732 & 524 & 37 & 331
\end{pmatrix}
$$
Find the minimal path sum from the left column to the right column in [matrix.txt](https://projecteuler.net/project/resources/p082_matrix.txt) (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.



## Solution

本题要比[Problem 081](../P081/P081_Note.md)难上许多，一方面，之前的问题只需要考虑向下和向右的情况，另一方面，上一个问题的起点和终点是固定的。但是，在本题中，起点和终点是不固定的，并且运动方向能够向上或向下。那么怎么解决本问题呢？

事实上，在本题中，动态规划还是可以使用的，只不过要稍微转变一下思路。

在本题中，起点和终点是不确定的，但是所有的路径都可以归结为：从首列运动到末列。在上一题中，我们定义了一个新的 $n \times n$ 矩阵来储存从固定的起点（或终点）出发到达该点所经过的最短路径；在本题中，我们重新对 $n \times n$ 矩阵进行定义——**从首列（或末列）到达该点所经过的最短距离**。在遍历中，我们**将三方向运动转化为遍历的两方向运动**，从而能够在单列中使用动态规划、并在列之间使用动态规划。

如下图所示，我们建立下述矩阵（ $a[row][col]$ 对应位置的原数据为 $d[row][col]$）：
$$
\left(
{\begin{array}{ccccc}
{a_{11}}&{a_{12}}&{a_{13}}&{\cdots}&{a_{1(n-2)}}&{a_{1(n-1)}}&{a_{1n}}\\
{a_{21}}&{a_{22}}&{a_{23}}&{\cdots}&{a_{2(n-2)}}&{a_{2(n-1)}}&{a_{2n}}\\
{a_{31}}&{a_{32}}&{a_{33}}&{\cdots}&{a_{3(n-2)}}&{a_{3(n-1)}}&{a_{3n}}\\
{\vdots}&{\cdots}&{\ddots}&{}&{}&{}{\cdots}&{\vdots}\\
{\vdots}&{\cdots}&{}&{\ddots}&{}&{}{\cdots}&{\vdots}\\
{\vdots}&{\cdots}&{}&{}&{\ddots}&{}{\cdots}&{\vdots}\\
{a_{(n-2)1}}&{a_{(n-2)2}}&{a_{(n-2)3}}&{\cdots}&{a_{(n-2)(n-2)}}&{a_{(n-2)(n-1)}}&{a_{(n-2)n}}\\
{a_{(n-1)1}}&{a_{(n-1)2}}&{a_{(n-1)3}}&{\cdots}&{a_{(n-1)(n-2)}}&{a_{(n-1)(n-1)}}&{a_{(n-1)n}}\\
{a_{n1}}&{a_{n2}}&{a_{n3}}&{\cdots}&{a_{n(n-2)}}&{a_{n(n-1)}}&{a_{nn}}\\
\end{array}}
\right)
$$
我们从首列开始进行状态转移。

首先，按照我们的定义，首列均为 $a[row][1] = d[row][1]$。

之后我们考虑第2列。怎么解决要同时考虑上移和下移的问题呢？我们不妨**先考虑单向移动**（例如下移）的情况，而这个情况是比较简单的，有：
$$
\begin{array}{l}
a[1][2] = a[1][1] + d[1][2]\\
a[2][2] = \min\{a[2][1] + d[2][2], a[1][2] + d[2][2]\}\\
\cdots\\
a[n][2] = \min\{a[n][1] + d[1][2], a[n-1][2] + d[n][2]\}\\
\end{array}
$$
那么，现在我们是否能够继续考虑上移的情况呢？注意到**动态规划是一个递归的过程**——也就是说，依据算法，**只需要上一个部分满足我们的定义，下一部分就一定能够符合。**应用在本题中，即：如果能够通过适当的算法，使得 $a[n-1][2]$ 称为三向移动到该位置的最短路径，那么之后的 $a[n-2][2],\cdots,a[1][2]$ 都可以成为符合定义的值，从而完成了列中的动态规划；这样一来，我们就从上一符合定义的列得到了下一符合定义的列，从而实现了列间的动态规划。

现在我们来具体考虑上移问题。由于 $a[n][2]$ 位于末行，不可能通过上移获得，因此通过上一列经过右移和下移得到的 $a[n][2]$ 必定符合定义（证明很容易，考虑到上一列已经固定，依据定义在右移前不需要上下移动，而在下一列，也即第2列中，凡是经过上移到达 $a[n][2]$ 位置的必然经过了重复路径，因此目前得到的 $a[n][2]$ 确为最小值）。再考虑 $a[n-1][2]$，$a[n-1][2]$ 可从 $a[n][2]$ 上移得到，也可从上方下移得到（下移的最小值即为目前的 $a[n-1][2]$），因此有： $a[n-1][2] = \min\{a[n-1][2], a[n][2]+d[n][2]\}$。这样得到的 $a[n-1][2]$ 也符合定义了，之后递推就可以得到整个满足定义的列，进而整个矩阵也满足定义了。

最后，我们所需的最短路径即为末列 $a[k][n]$ 的最小值。



综观上述解题过程，我们发现有以下两个关键点：

- **对三方向运动的拆解**：三方向运动看似难了许多，但是仍然有一个**整体上的趋势**（在本题中，这一趋势是右移）。那么，如果我们运用列之间的动态规划算法，定义动态规划矩阵为从一固定的首列位置出发到达相应位置的最短路径，在每一次遍历中，将上一列的值全部求出，注意下一列的**首行不可下移得到、末行不能上移得到**，从而证实了**上移和下移是可以拆解分析的**。
- **对动态规划矩阵的重新定义**：在上述固定起点的分析过程中，我们发现在上一列之间是不能上下移动的（因为根据定义，上一列的每一位置都已经取得了最短路径）。如果我们不将起点固定，将动态规划矩阵定义为首列到达相应位置的最短路径，我们发现上一列仍然不能上下移动，那么动态规划过程将是完全一样的！另外，在解题过程中我们发现，事实上我们不需要整个矩阵，只需要一列 $a[row]$ 数据就可以完成整个动态规划过程。**经过对动态规划矩阵的重新定义**，我们**大大减少了原方法的时空需求**，极大地增加了效率。



下面是应用上述改进解法的实现（本实现是从末列出发的）：

```python
#====================================================================================================================Solution
import os
BSER_DIR = os.path.dirname(os.path.abspath(__file__))

import copy

n = 80
data_list = []
with open(BSER_DIR + '\p082_matrix.txt', mode = 'r') as datafile:
    for _ in range(n):
        data_list.append(list(map(int, datafile.readline().split(','))))

DP_ans = [0] * n                        # 对于每次遍历的第col列，DP_ans[row]代表从末列某位置到达row行col列位置的最短路径
# 出于最小值的考虑，末列不需要进行上下移动
for i in range(n):
    DP_ans[i] = data_list[i][n - 1]
# 开始对每一列进行DP_ans的更新
for col in reversed(range(n - 1)):
    # 先考虑向下的情况
    DP_ans[0] += data_list[0][col]      # 由于不考虑向上移动，首行初始化为向上移动
    for row in range(1, n):
        DP_ans[row] = min(DP_ans[row] + data_list[row][col], DP_ans[row - 1] + data_list[row][col])
    # 再考虑向上的情况
    for row in reversed(range(n - 1)):
        DP_ans[row] = min(DP_ans[row], DP_ans[row + 1] + data_list[row][col])
print(min(DP_ans))
#====================================================================================================================Answer
The Answer is 260324
```

