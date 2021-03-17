# Project Euler	Problem 025

<p align="right"><i>Tiny Snow</i></p>



## Problem

### 1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:
$$
F_n = F_{n−1} + F_{n−2}, where\ F_1 = 1\ and\ F_2 = 1.
$$
Hence the first 12 terms will be:
$$
F_1 = 1\\
F_2 = 1\\
F_3 = 2\\
F_4 = 3\\
F_5 = 5\\
F_6 = 8\\
F_7 = 13\\
F_8 = 21\\
F_9 = 34\\
F_{10} = 55\\
F_{11} = 89\\
F_{12} = 144
$$


The 12th term, $F_{12}$, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?



## Solution

似乎是一道简单的斐波那契数列问题，解决方法如下：

```python
#=============================Solution
f_1 = 1
f_2 = 1
f_3 = f_1 + f_2
index = 3
while(len(str(f_3)) != 1000):
    f_1 = f_2
    f_2 = f_3
    f_3 = f_1 + f_2
    index += 1
print(index)
#=============================Answer
The Answer is 4782
```

