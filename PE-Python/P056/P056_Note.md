# Project Euler	Problem 056

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Powerful digit sum

A googol ($10^{100}$) is a massive number: one followed by one-hundred zeros; $100^{100}$ is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only $1$.

Considering natural numbers of the form, $a^b$, where $a, b < 100$, what is the maximum digital sum?



## Solution

直接遍历即可，实现如下：

```python
#=================================================Solution
max_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        num = a ** b
        num_sum = 0
        for char in str(num):
            num_sum += int(char)
            max_sum = max(max_sum, num_sum)
print(max_sum)
#=================================================Answer
The Answer is 972
```

