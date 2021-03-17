# Project Euler	Problem 060

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Prime pair sets

The primes $3, 7, 109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime. The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.



## Solution

本体数据量和运算量十分巨大，稍有不慎就会超出计算机的算力。要注意以下几点：

- 我们不能够遍历出所有的素数（这是因为需要寻找的数太过分散），最好的方法是先遍历出 *Prime pair set* 中的素数，然后对它们组合出的数使用试除法判断是否为素数。
- 进行组合遍历时，一定要注意每次进入更深一层循环时，要首先判断已经有的素数是否满足条件。例如对于遍历到的素数 $p_1, p_2,p_3$ ，在遍历 $p_4$ 前如果发现 $p_1, p_2,p_3$ 根本不是一个 *Prime pair set* ，那么就无需遍历 $p_4$ 了。这是大幅度减少循环次数的关键所在。

依照上述原则，我们得出下述不是那么严谨的算法：

```python
#==================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P060')[0] + 'Utility Class')

from prime_utility import *
limit = 10000
prime_class = Prime(limit)
prime_class._traverse()
prime_list = prime_class._get_prime_list()

def is_prime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

def is_prime_pair(p1, p2):
    if is_prime(int(str(p1) + str(p2))) == True and is_prime(int(str(p2) + str(p1))) == True:
        return True
    return False

def is_prime_pair_set(prime_set):
    for p1 in range(len(prime_set) - 1):
        for p2 in range(p1 + 1, len(prime_set)):
            if is_prime_pair(prime_set[p1], prime_set[p2]) != True:
                return False
    return True

def find_ans():
    for i1 in range(len(prime_list) - 4):
        for i2 in range(i1 + 1, len(prime_list) - 3):
            if is_prime_pair_set([prime_list[i1], prime_list[i2]]) == True:
                for i3 in range(i2 + 1, len(prime_list) - 2):
                    if is_prime_pair_set([prime_list[i1], prime_list[i2], prime_list[i3]]) == True:
                        for i4 in range(i3 + 1, len(prime_list) - 1):
                            if is_prime_pair_set([prime_list[i1], prime_list[i2], prime_list[i3], prime_list[i4]]) == True:
                                for i5 in range(i4 + 1, len(prime_list)):
                                    if is_prime_pair_set([prime_list[i1], prime_list[i2], prime_list[i3], prime_list[i4], prime_list[i5]]) == True:
                                        return sum([prime_list[i1], prime_list[i2], prime_list[i3], prime_list[i4], prime_list[i5]])
print(find_ans())
#==================================================================Answer
The Answer is 26033
```

如何得出真正最小的答案（而不是第一个）呢？最好的、也是最快最有效的方法是**传入1亿以内的素数列表**。