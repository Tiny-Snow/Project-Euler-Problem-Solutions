# Project Euler	Problem 087

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Prime power triples

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:
$$
\begin{array}{l}
28 = 2^2 + 2^3 + 2^4\\
33 = 3^2 + 2^3 + 2^4\\
49 = 5^2 + 2^3 + 2^4\\
47 = 2^2 + 3^3 + 2^4\\
\end{array}
$$
How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?



## Solution

利用 `Prime`工具类，直接遍历求解。

实现如下：

```python
#=================================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P087')[0] + 'Utility Class')

from prime_utility import *

limit = int(50000000 ** 0.5)
prime_class = Prime(limit)
prime_class._traverse()
prime_list = prime_class._get_prime_list()

sum_list = []
for i in range(len(prime_list)):
    if prime_list[i] ** 2 >= 50000000:
        break
    for j in range(len(prime_list)):
        if prime_list[i] ** 2 + prime_list[j] ** 3>= 50000000:
            break
        for k in range(len(prime_list)):
            if prime_list[i] ** 2 + prime_list[j] ** 3 + prime_list[k] ** 4 >= 50000000:
                break
            sum_list.append(prime_list[i] ** 2 + prime_list[j] ** 3 + prime_list[k] ** 4)
sum_list = list(set(sum_list))
print(len(sum_list))
#=================================================================================Answer
The Answer is 1097343
```

