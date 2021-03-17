# Project Euler	Problem 023

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of $28$ would be $1 + 2 + 4 + 7 + 14 = 28$, which means that $28$ is a perfect number.

A number is called deficient if the sum of its proper divisors is less than and it is called abundant if this sum exceeds .nnn

As 12 is the smallest abundant number, $1 + 2 + 3 + 4 + 6 = 16$, the smallest number that can be written as the sum of two abundant numbers is $24$. By mathematical analysis, it can be shown that all integers greater than $28123$ can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.



## Solution

这个问题还是**因数和**的问题，沿用[P021_Note](../P021/P021_Note.md)中的因数和函数算法，实现如下：（计算比较慢，`abundant sum`占有`26667`个数）

```python
#==================================================================================================================================Solution
maxn = 28123
p_list = []
sumd_list = [0 for i in range(maxn + 1)]
sumd_list[1] = 1
prime_list = [1 for i in range(maxn + 1)]
prime_list[1] = 0
for p in range(1, maxn + 1):
    if prime_list[p] == 1:
        p_list.append(p)
        sumd_list[p] = 1 + p            # 质数的因子只有两个
    for j in range(len(p_list)):
        if p * p_list[j] > maxn:
            break
        prime_list[p * p_list[j]] = 0
        if p % p_list[j] == 0:          # 遍历至最小质因数
            p_divided_by_pj = p
            alpha_j = 1
            while(p_divided_by_pj % p_list[j] == 0):
                p_divided_by_pj /= p_list[j]
                alpha_j += 1
            sumd_list[p * p_list[j]] = sumd_list[int(p_divided_by_pj)] * int(((p_list[j] ** (alpha_j + 1) - 1) // (p_list[j] - 1)))
            break 
        else:                           # 没有遍历到质因数
            sumd_list[p * p_list[j]] = sumd_list[p] * sumd_list[p_list[j]]

abundant_numlist = []
for i in range(1, maxn + 1):
    sumd_list[i] -= i
    if sumd_list[i] > i:
        abundant_numlist.append(i)

abundant_sums = []
for i in range(len(abundant_numlist) - 1):
    for j in range(i, len(abundant_numlist)):
        abundant_sum = abundant_numlist[i] + abundant_numlist[j]
        if abundant_sum > maxn:
            break
        if abundant_sum not in abundant_sums:
            abundant_sums.append(abundant_sum)
            print(len(abundant_sums))
print(maxn * (maxn + 1) // 2 - abundant_numsum)
#==================================================================================================================================Answer
The Answer is 4179871
```

