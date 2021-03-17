# Project Euler	Problem 076

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Counting summations

It is possible to write five as a sum in exactly six different ways:
$$
\begin{array}{l}
{4 + 1}\\
{3 + 2}\\
{3 + 1 + 1}\\
{2 + 2 + 1}\\
{2 + 1 + 1 + 1}\\
{1 + 1 + 1 + 1 + 1}\\
\end{array}
$$
How many different ways can one hundred be written as a sum of at least two positive integers?



## Solution

本题以及之后的[Problem 077](../P077/P077_Note.md)、[Problem 078](../P078/P078_Note.md) 都是属于**欧拉分区函数问题（*Partition Function P*）**。

关于此问题，欧拉给出了基于 ***Pentagonal number*** 的**分区函数生成函数（*generating function*）**，如下：
$$
P(n)=\sum\limits_{k=1}^{n}{(-1)^{k+1}\left[{P\left({n-{{1}\over{2}}k(3k-1)}\right)+P\left({n-{{1}\over{2}}k(3k+1)}\right)}\right]}
$$
或者是下面的形式：
$$
{P(n)=\sum\limits_{k\in Z\backslash \left\{{0}\right\}}{(-1)^{k+1}P\left({n-{{1}\over{2}}k(3k-1)}\right)}}\\
{=P(n-1)+P(n-2)-P(n-5)-P(n-7)+P(n-12)+···}
$$
其中 $k$ 满足五边形数的条件：
$$
-{{\sqrt{24n+1}-1}\over{6}}\leq k\leq{{\sqrt{24n+1}+1}\over{6}}
$$
事实上，上述公式已经为我们提供了最简单、最高效的算法，我们将在[Problem 078](../P078/P078_Note.md)中应用它。



上述有关 *Partition Function P* 的数学知识，参考以下网站：

[MathWorld: Partition Function P](https://mathworld.wolfram.com/PartitionFunctionP.html)

[WikiPedia: Partition (number theory)](https://en.wikipedia.org/wiki/Partition_(number_theory))

[WikiPedia: Partition function (number theory)](https://en.wikipedia.org/wiki/Partition_function_(number_theory))

[WikiPedia: Pentagonal number](https://en.wikipedia.org/wiki/Pentagonal_number#Further_reading)





在本题中，我们使用另一种动态规划算法来实现。

如果我们将 $[n,k]$ 记作将 $n$ 分离为不大于 $k$ 的数之和的方法数，那么显然有下述的递推公式：
$$
[n,k] = [n-k,k] + [n,k-1]
$$
根据上述状态转移方程，我们很容易求出最终的答案 $[100, 100]$ 。

事实上，我们完全可以推广该算法，如果将 $[n,(a_1,a_2,···,a_k)]$ 记作将 $n$ 分离为若干个 $a_1,a_2,···,a_k$ 之和的方法数，那么类似地：
$$
[n,(a_1,a_2,···,a_k)] = [n-a_k,(a_1,a_2,···,a_k)] + [n,(a_1,a_2,···,a_{k-1})]
$$
一个简单的应用是**硬币问题**：将 $10$ 元纸币换做 $1,2,5$ 元硬币，有几种分法？实际上答案即为 $[10,(1,2,5)]$ 。



基于动态规划的实现如下：

```python
#=================================================================================Solution
limit = 100
partition_list = [[0 for j in range(limit + 1)]for i in range(limit + 1)]
partition_list[0] = [1 for j in range(limit + 1)]
for n in range(1, limit + 1):
    for k in range(1, limit + 1):
        partition_list[n][k] = partition_list[n - k][k] + partition_list[n][k - 1]
print(partition_list[100][100] - 1)
#=================================================================================Answer
The Answer is 190569291
```

