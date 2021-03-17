# Project Euler	Problem 030

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
$$
1634 = 1^4 + 6^4 + 3^4 + 4^4\\
8208 = 8^4 + 2^4 + 0^4 + 8^4\\
9474 = 9^4 + 4^4 + 7^4 + 4^4
$$
As $1 = 1^4$ is not a sum it is not included.

The sum of these numbers is $1634 + 8208 + 9474 = 19316$.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.



## Solution

首先要确定遍历的范围，这里算出左式的最小值和右式的最大值即可。

至于遍历没有什么很简便的方法，直接暴力求解，实现如下：

```python
#=======================================Solution
k = 1
while k * (9 ** 5) > (10 ** k - 1) // 9:
    k += 1

maxn = 10 ** k
all_sum = 0
for i in range(2, maxn):
    sum = 0
    for j in str(i):
        sum += int(j) ** 5
    if int(sum) == i:
        all_sum += i
print(all_sum)
#=======================================Answer
The Answer is 443839
```

