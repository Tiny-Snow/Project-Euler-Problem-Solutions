# Project Euler	Problem 050

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:
$$
41 = 2 + 3 + 5 + 7 + 11 + 13
$$
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to $953$.

Which prime, below one-million, can be written as the sum of the most consecutive primes?



## Solution

本题当然是暴力遍历求解，但是遍历要注意技巧：

- 选取`start`和`end`作为上下界；
- 大部分的素数和都会超过1000000，遍历到该值以上后就应该进行下一次遍历（`end`从小到大遍历）；
- 没有必要对于每个`start`和`end`界都重新计算一遍素数和，只需要在每次`end += 1`的时候累加一个素数即可。

实现如下：

```python
#===============================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P050')[0] + 'Utility Class')

from prime_utility import *
limit = 1000000
prime_class = Prime(limit)
prime_class._traverse()
prime_list = prime_class._get_prime_list()
prime_num = len(prime_list)

max_len = 0
ans_p = 0
for start in range(prime_num - 1):
    p_sum = prime_list[start]
    for end in range(start + 1, prime_num):
        p_sum += prime_list[end]
        if p_sum > limit:
            break
        if prime_class._is_prime(p_sum) == True and end - start > max_len:
            ans_p = p_sum
            max_len = end - start
print(ans_p)
#===============================================================Answer
The Answer is 997651
```

