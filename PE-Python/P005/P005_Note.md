# Project Euler	Problem 005

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Smallest multiple

$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from $1$ to $20$?



## Solution

就是求最小公倍数，算法如下：

```python
#==========================================Solution
from math import *

n_lcm = 1
for i in range(1, 21):
    n_lcm = int((n_lcm * i)/gcd(n_lcm, i))
print(n_lcm)
#==========================================Answer
The Answer is 232792560
```