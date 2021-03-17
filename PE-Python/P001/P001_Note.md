# Project Euler	Problem 001

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Multiples of 3 and 5

If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3$, $5$, $6$ and $9$. The sum of these multiples is $23$.

Find the sum of all the multiples of $3$ or $5$ below $1000$.



## Solution

使用以下代码可以迅速得到问题的解答。

```python
#=====================================Solution
sum = 0
for i in range(1000):
    if i % 3 == 0:
        sum += i
    if i % 5 == 0:
        sum += i
    if i % 15 == 0:
        sum -= i
print(sum)

#=====================================Answer
The Answer is 233168
```

当然，本题也完全可以用等差数列求解。