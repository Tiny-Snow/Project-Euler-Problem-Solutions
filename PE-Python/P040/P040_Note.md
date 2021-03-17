# Project Euler	Problem 040

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:
$$
0.12345678910\textbf1112131415161718192021...
$$
It can be seen that the 12th digit of the fractional part is $1$.

If $d_n$ represents the $n$th digit of the fractional part, find the value of the following expression.

$$
d_1 × d_{10} × d_{100} × d_{1000} × d_{10000} × d_{100000} × d_{1000000}
$$


## Solution

只需要不断地更新字符串即可。实现如下：

```python
#=======================================================Solution
fractional_part = ''
product = 1
i = 1
while len(fractional_part) <= 1000000:
    fractional_part += str(i)
    if i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        product *= int(fractional_part[i - 1])
    i += 1
print(product)
#=======================================================Answer
The Answer is 210
```

