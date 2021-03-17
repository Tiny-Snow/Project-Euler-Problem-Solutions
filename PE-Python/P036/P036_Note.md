# Project Euler	Problem 036

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Double-base palindromes

The decimal number, $585 = 10010010012 (binary)$, is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)



## Solution

本题利用Python字符串的**切片倒置方法**`str[ : : -1]`能够马上得到解答，不过注意`bin()`函数返回的二进制表达前面有`0b`。

实现如下：

```python
#===========================================Solution
maxn = 1000000
double_base_palindromes_sum = 0
for i in range(1, maxn, 2):
    if str(i) == str(i)[ : : -1]:
        i_bin = str(bin(i))[2: ]
        if i_bin == i_bin[ : : -1]:
            double_base_palindromes_sum += i
print(double_base_palindromes_sum)
#===========================================Answer
The Answer is 872187
```

