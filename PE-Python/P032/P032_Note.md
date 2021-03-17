# Project Euler	Problem 032

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Pandigital products

We shall say that an *n*-digit number is pandigital if it makes use of all the digits 1 to *n​* exactly once; for example, the 5-digit number, $15234$, is 1 through 5 pandigital.

The product $7254$ is unusual, as the identity, $39 × 186 = 7254$, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.



## Solution

本题需要考虑一下乘积的形式，也就是各个数的**位数**，这是因为所有数的位数加起来必须是9。简单分析以后可以得出，形如 $a \times b = ab$ 的乘积必须拥有如下的形式（假设 $a ≤ b$）：

- $a$ 为1位数，$b$ 为4位数，$a \times b$ 为4位数
-  $a$为2位数，$b$ 为3位数，$a \times b$ 为4位数

因此实现如下，注意最后去重：

```python
#=======================================Solution
num_list = []

def is_pandigital(numstr):
    flag = True
    for i in range(1, 10):
        if str(i) not in numstr:
            flag = False
    return flag

# a为1位数，b为4位数，a * b为4位数
for a in range(1, 10):
    for b in range(1000, 10000):
        if a * b >= 10000:
            break
        numstr = str(a) + str(b) + str(a * b)
        if is_pandigital(numstr) == True:
            num_list.append(a * b)

# a为2位数，b为3位数，a * b为4位数
for a in range(10, 100):
    for b in range(100, 1000):
        if a * b >= 10000:
            break
        numstr = str(a) + str(b) + str(a * b)
        if is_pandigital(numstr) == True:
            num_list.append(a * b)

num_list = list(set(num_list))
print(sum(num_list))
#=======================================Answer
The Answer is 45228
```

