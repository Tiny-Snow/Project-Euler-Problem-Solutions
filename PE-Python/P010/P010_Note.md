# Project Euler	Problem 010

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Summation of primes

The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.

Find the sum of all the primes below two million.



## Solution

算法仍然是基于**欧拉线性筛法**，详细内容见：[P007_Note](../P007/P007_Note.md)。

完全可以复用[P007_Note](../P007/P007_Note.md)中的代码，如下：

```python
#==========================================Solution
maxn = 2000001
p_list = []
prime_dict = {}.fromkeys(range(1, maxn), 1)
prime_dict[1] = 0
for p in list(prime_dict.keys()):
    if prime_dict[p] == 1:
        p_list.append(p)
    for j in range(len(p_list)):
        if p * p_list[j] > maxn:
            break
        prime_dict[p * p_list[j]] = 0
        if p % p_list[j] == 0:
            break
print(sum(p_list))
#==========================================Answer
The Answer is 142913828922
```

