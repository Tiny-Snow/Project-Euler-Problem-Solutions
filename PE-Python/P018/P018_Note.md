# Project Euler	Problem 018

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
$$
\boldsymbol {3}\\
\boldsymbol {7}\ 4\\
2\ \boldsymbol {4}\ 6\\
8\ 5\ \boldsymbol {9}\ 3\\
$$
That is, $3 + 7 + 4 + 9 = 23$.

Find the maximum total from top to bottom of the triangle below:
$$
75\\
95\ 64\\
17\ 47\ 82\\
18\ 35\ 87\ 10\\
20\ 04\ 82\ 47\ 65\\
19\ 01\ 23\ 75\ 03\ 34\\
88\ 02\ 77\ 73\ 07\ 63\ 67\\
99\ 65\ 04\ 28\ 06\ 16\ 70\ 92\\
41\ 41\ 26\ 56\ 83\ 40\ 80\ 70\ 33\\
41\ 48\ 72\ 33\ 47\ 32\ 37\ 16\ 94\ 29\\
53\ 71\ 44\ 65\ 25\ 43\ 91\ 52\ 97\ 51\ 14\\
70\ 11\ 33\ 28\ 77\ 73\ 17\ 78\ 39\ 68\ 17\ 57\\
91\ 71\ 52\ 38\ 17\ 14\ 91\ 43\ 58\ 50\ 27\ 29\ 48\\
63\ 66\ 04\ 68\ 89\ 53\ 67\ 30\ 73\ 16\ 69\ 87\ 40\ 31\\
04\ 62\ 98\ 27\ 23\ 09\ 70\ 98\ 73\ 93\ 38\ 53\ 60\ 04\ 23
$$
**NOTE:** As there are only 16384 routes, it is possible to solve this problem by trying every route. However, [Problem 67](https://projecteuler.net/problem=67), is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)



## Solution

本题的暴力解法是显而易见的，一种常见的暴力解法是利用深度优先搜索（DFS），这种暴力方法借助递归实现。

但是，显然我们明白，从上至下的决策是不确定的，而解决该**不确定性**的方法也很显然：从下至上依次确定决策。

我们可以给每一个数加上一个**特征值**，对应其在向下的所有路径中所能取得的最大和。显然，从下到上我们能够依次确定这些特征值，而确定的方法也很简单——只需要依据下一行相邻的两个特征值即可。

特征值数组显然满足以下递推式：
$$
sum[k][j] = array[k][j] + max\{sum[k+1][j],sum[k+1][j+1]\}
$$
遍历到最后，$sum[0][0]$ 就是我们要求的最大值。



上述算法被称为**动态规划**。动态规划是一种广泛应用于运筹学的算法，用于求解**决策问题最优化**。

动态规划的核心思想是：

- **将一个问题分解为若干个子问题**：例如，本问题就被分解为若干个从下至上的决策过程，**方向很关键**。
- **将每个子问题的结果保留供后续的子问题使用**：这是动态规划算法的关键。例如，本问题的决策（子问题）是“从下一行相邻的两个数种选取一个以保证和最大”，那么我们需要保留的结果就是下一行每个数的向下遍历最大和。这样，每一个数的特征值都只需要计算一次即可，减少了无意义的重复计算。

动态规划是基础算法之一，**其过程类似于求解一个递推数列**，应用的关键在于**合理分解子问题，使得之前的结果能够被充分利用**。



下面是算法的实现：

```python
#===================================================================================================================Solution
#=================================================储存数据
data_str = '''\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
data_lines = data_str.splitlines()
data = []
lines = len(data_lines)
for i in range(lines):
    tempdata = data_lines[i].split()
    for j in range(len(tempdata)):
        data.append(int(tempdata[j]))
#=================================================动态规划
data_sum = data
for i in reversed(range(lines - 1)):
    for j in range(i + 1):
        data_sum[i * (i + 1) // 2 + j] += max(data[(i + 1) * (i + 2) // 2 + j], data[(i + 1) * (i + 2) // 2 + j + 1])
print(data_sum[0])
#===================================================================================================================Answer
The Answer is 1074
```



另外，[Project Euler  Problem 067](../P067/P067_Note.md)的问题和该问题完全相同（只是数据量更大），应用的算法仍然还是几乎一样的动态规划。