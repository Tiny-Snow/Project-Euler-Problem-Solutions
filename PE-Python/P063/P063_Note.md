# Project Euler	Problem 063

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Powerful digit counts

The 5-digit number, $16807=7^5$, is also a fifth power. Similarly, the 9-digit number, $134217728=8^9$, is a ninth power.

How many *n*-digit positive integers exist which are also an *n*th power?



## Solution

本题比较简单，显然 *n*-digit positive integers 增长的要比 *n*th power 快。遍历 *n*th power 即可，实现如下：

```python
#=====================================================================Solution
num = 0
for a in range(1, 10):
    n = 1
    while len(str(a ** n)) == n:
        n += 1
        num += 1
print(num)
#=====================================================================Answer
The Answer is 49
```

