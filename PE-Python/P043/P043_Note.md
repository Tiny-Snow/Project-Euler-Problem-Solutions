# Project Euler	Problem 043

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Sub-string divisibility

The number, $1406357289$, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let $d_1$ be the 1st digit,  $d_2$be the 2nd digit, and so on. In this way, we note the following:

- $d_2d_3d_4=406$ is divisible by $2$
- $d_3d_4d_5=063$ is divisible by $3$
- $d_4d_5d_6=635$ is divisible by $5$
- $d_5d_6d_7=357$ is divisible by $7$
- $d_6d_7d_8=572$ is divisible by $11$
- $d_7d_8d_9=728$ is divisible by $13$
- $d_8d_9d_10=289$ is divisible by $17$

Find the sum of all 0 to 9 pandigital numbers with this property.



## Solution

本题我们还是调用`itertools.permutations`方法获得排列结果，注意排除首位为0的情况。实现如下：

```python
#==========================================================================Solution
import itertools

prime_list = [2, 3, 5, 7, 11, 13, 17]
def is_right(num, prime_list):
    for i in range(len(prime_list)):
        if int(num[i + 1: i + 4]) % prime_list[i] != 0:
            return False
    return True

all_sum = 0
for num_tuple in list(itertools.permutations([i for i in range(0, 10)], 10)):
    if num_tuple[0] == 0:       # 首位为0的情况
        continue
    num = ''
    for i in num_tuple:
        num += str(i)
    if is_right(num, prime_list) == True:
        all_sum += int(num)
print(all_sum)
#==========================================================================Answer
The Answer is 16695334890
```

