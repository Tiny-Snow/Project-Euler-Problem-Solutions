# Project Euler	Problem 067

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Maximum path sum II

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
$$
\boldsymbol {3}\\
\boldsymbol {7}\ 4\\
2\ \boldsymbol {4}\ 6\\
8\ 5\ \boldsymbol {9}\ 3\\
$$
That is, $3 + 7 + 4 + 9 = 23$.

Find the maximum total from top to bottom in [triangle.txt](https://projecteuler.net/project/resources/p067_triangle.txt) (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

**NOTE:** This is a much more difficult version of [Problem 18](https://projecteuler.net/problem=18). It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)



## Solution

解法是和[Project Euler  Problem 018](../P018/P018_Note.md)完全一样的**动态规划**算法。实现如下：

```python
#===================================================================================================================Solution
#=================================================储存数据
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(BASE_DIR + '/p067_triangle.txt', mode = 'r') as datafile:
    data_str = datafile.readlines()
data = []
lines = len(data_str)
for i in range(lines):
    tempdata = data_str[i].split()
    for j in range(len(tempdata)):
        data.append(int(tempdata[j]))
#=================================================动态规划
data_sum = data
for i in reversed(range(lines - 1)):
    for j in range(i + 1):
        data_sum[i * (i + 1) // 2 + j] += max(data[(i + 1) * (i + 2) // 2 + j], data[(i + 1) * (i + 2) // 2 + j + 1])
print(data_sum[0])
#===================================================================================================================Answer
The Answer is 7273
```

