# Project Euler	Problem 014

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:
$$
n → n/2\ (n\ is\ even)\\
n → 3n + 1\ (n\ is\ odd)
$$
Using the rule above and starting with $13$, we generate the following sequence:
$$
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
$$
It can be seen that this sequence (starting at $13$ and finishing at $1$) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.

Which starting number, under one million, produces the longest chain?

**NOTE:** Once the chain starts the terms are allowed to go above one million.



## Solution

该问题是经典的***Collatz Problem***。算法是基础的函数迭代，可以利用已经找到数据优化。

实现如下：

```python
#==========================================================================================Solution
maxn = 1000000
collatz_list = [0] * maxn                               # 以每个数为初始项的序列长度
collatz_list[1] = 1
def collatz(n, len):
    '''传入参数为(目前序列的初始项n，初始序列长度（n之前的）len)，返回值为整个序列的长度'''
    if n == 1:
        return len + 1
    if n % 2 == 0:
        if n / 2 < maxn and collatz_list[int(n / 2)] != 0:      # 首先在序列中查找是否已经找到     
            return len + collatz_list[int(n / 2)]
        else:
            return collatz(int(n / 2), len + 1)
    else:
        if 3 * n + 1 < maxn and collatz_list[3 * n + 1] != 0:   # 首先在字典中查找是否已经找到        
            return len + collatz_list[3 * n + 1]
        else:
            return collatz(3 * n + 1, len + 1)
for i in range(1, maxn):
    collatz_list[i] = collatz(i, 0)
print(collatz_list.index(max(collatz_list)))
#==========================================================================================Answer
The Answer is 837799
```

