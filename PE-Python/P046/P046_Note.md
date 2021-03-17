# Project Euler	Problem 046

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
$$
9 = 7 + 2×1^2\\
15 = 7 + 2×2^2\\
21 = 3 + 2×3^2\\
25 = 7 + 2×3^2\\
27 = 19 + 2×2^2\\
33 = 31 + 2×1^2
$$
It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?



## Solution

没有什么好的数学方法，最简单的方法是按照平方数进行遍历，实现如下：

```python
#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P046')[0] + 'Utility Class')

from prime_utility import *
limit = 10000
prime_class = Prime(limit)
prime_class._traverse()

for n in range(9, limit, 2):
    if prime_class._is_prime(n) == True:
        continue
    flag = False
    for k in range(1, int((n / 2) ** 0.5) + 1):
        if prime_class._is_prime(n - 2 * (k ** 2)) == True:
            flag = True
            break
    if flag == False:
        print(n)
        break
#===============================================================Answer
The Answer is 5777
```

