# Project Euler	Problem 015

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

![img](P015_Note.assets/p015.png)

How many such routes are there through a 20×20 grid?



## Solution

***Lattice paths***是一个经典的组合问题，只需要注意到总共包括 $n$ 次向右走、 $n$ 次向下走，最后一步只有两种选择，前 $2n-1$ 步是组合选择即可，立得结果应该为 $2C_{2n-1}^{n}$。



在编程时，可以调用Python中的`scipy`**科学计算包**来方便地计算。例如使用`special.comb`方法计算组合数、`special.perm`方法计算排列数等。如下：

```python
#=====================================Solution
from scipy.special import *
def Lattice_paths(n):
    return int(2 * comb(2 * n - 1, n))
print(Lattice_paths(20))
#=====================================Answer
The Answer is 137846528820
```

关于`scipy`详情可见：[scipy.org](https://www.scipy.org/)。