# Project Euler	Problem 035

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Circular primes

The number, $197$, is called a circular prime because all rotations of the digits: $197$, $971$, and $719$, are themselves prime.

There are thirteen such primes below 100: $2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79$, and $97$.

How many circular primes are there below one million?



## Solution

这道题还是依托于素数遍历，不过我们现在不再重复造轮子了——我们有了我们自己的**素数工具类**！

这个素数工具类`Prime`位于[`prime_utility`模块](../Utility Class/prime_utility.py)，我们可以方便地调用它进行相应的素数分析，代码将会十分简洁。

我们不详细探讨这个类的功能或是其实现了，具体内容可以见模块类文档。

下面给出了调用`Prime`类方法的示例，简洁的代码迅速解决了本问题：

```python
#==================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P035')[0] + 'Utility Class')

from prime_utility import *

limit = 1000000
circular_primes = 0
prime_class = Prime(limit)
prime_class._traverse()
for p in prime_class._get_prime_list():
    flag = True
    l = len(str(p))
    for i in range(1, l):
        if prime_class._is_prime(int(str(p)[i: l] + str(p)[0: i])) == False:
            flag = False
    if flag == True:
        circular_primes += 1
print(circular_primes)
#==================================================================Answer
The Answer is 55
```

