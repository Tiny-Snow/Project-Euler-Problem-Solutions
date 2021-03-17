# Project Euler	Problem 049

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Prime permutations

The arithmetic sequence, $1487, 4817, 8147$, in which each of the terms increases by $3330$, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?



## Solution

本题我们将使用`itertools`模块获得4位数字的排列结果和3个数字的组合结果。实现的关键在于数据类型转换和重复结果的略去，实现如下：

```python
#===================================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P049')[0] + 'Utility Class')

from prime_utility import *
limit = 10000
prime_class = Prime(limit)
prime_class._traverse()

import itertools

ans_list = []
for num in range(1000, 10000):
    permutations = list(itertools.permutations(list(str(num)), 4))
    for num1, num2, num3 in list(itertools.combinations(permutations, 3)):
        num1 = int(num1[0] + num1[1] + num1[2] + num1[3])
        num2 = int(num2[0] + num2[1] + num2[2] + num2[3])
        num3 = int(num3[0] + num3[1] + num3[2] + num3[3])
        num1, num2, num3 = tuple(sorted((num1, num2, num3)))
        if len(str(num1)) == len(str(num2)) == len(str(num3)) == 4:
            if num1 == num2 or num1 in ans_list:        # 去除三数相同结果和重复结果
                continue
            if num2 - num1 == num3 - num2 and prime_class._is_prime(num1) == True and\
                    prime_class._is_prime(num2) == True and prime_class._is_prime(num3) == True:
                print(num1, num2, num3)
                ans_list.append(num1)
#===================================================================================Answer
The Answer is 296962999629
```

