# Project Euler	Problem 086

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Cuboid route

A spider, $S$, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, $F$, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from $S$ to $F$ is 10 and the path is shown on the diagram.

![img](P086_Note.assets/p086.png)

However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of $M$ by $M$ by $M$, for which the shortest route has integer length when $M = 100$. This is the least value of $M$ for which the number of solutions first exceeds two thousand; the number of solutions when $M = 99$ is 1975.

Find the least value of $M$ such that the number of solutions first exceeds one million.



## Solution

本题最关键的问题如何减少不必要的遍历次数。我们知道，首先可以对边长排序：$a \geq b \geq c$ ，这样我们只需要在所有遍历到的符合条件的三元组 $(a,b,c)$ 的个数 $\geq 1000000$ 即可结束遍历，$M = a$ 。

但是，如果对每个 $(b,c)$ 遍历，从时间复杂度上来说是不现实的。有没有别的方法呢？

考虑最短的边 $\sqrt{a^2 + (b+c)^2}$ 为整数，注意 $a$ 是固定的，只需要 $b + c$ 满足上式为整数，那么任何 $b + c$ 的分划 $(b,c)$ 都是符合条件的。因此，实际上我们只要在区间 $[2,2a]$ 内遍历出符合的 $b+c$ ，再算出分划数即可。

注意这里有一个易错点：对于所有情况来说，分划数均为 $[(b+c)/2]$ 吗？注意：我们还要满足一个先决条件，即 $a \geq b \geq c$，那么当 $b + c > a + 1$ 时，此时有 $a\geq b \geq (b + c) / 2$ ，因此实际的分划数为：
$$
\begin{array}{ll}
{a - (b + c)/2 + 1} & {a\ is\ even}\\
{a - (b + c + 1)/2 + 1} & {a\ is\ odd}\\
\end{array}
$$
实现如下：

```python
#=================================================================================Solution
int_len_num = 0
a = 0
while int_len_num <= 10 ** 6:
    a += 1
    for sum_bc in range(2, 2 * a + 1):
        if (a ** 2 + (sum_bc) ** 2) ** 0.5 == int((a ** 2 + (sum_bc) ** 2) ** 0.5):
            if sum_bc > a + 1:
                if sum_bc % 2 == 0:
                    int_len_num += a - sum_bc // 2 + 1
                else:
                    int_len_num += a - (sum_bc - 1) // 2
            else:
                int_len_num += sum_bc // 2
print(a)
#=================================================================================Answer
The Answer is 1818
```

