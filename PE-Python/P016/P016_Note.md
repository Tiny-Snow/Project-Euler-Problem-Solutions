# Project Euler	Problem 016

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Power digit sum

$2^15 = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.

What is the sum of the digits of the number $2^{1000}$?



## Solution

使用下面的代码：

```python
#=====================================Solution
data = str(2 ** 1000)
sum = 0
for i in data:
    sum += int(i)
print(sum)
#=====================================Answer
The Answer is 1366
```

