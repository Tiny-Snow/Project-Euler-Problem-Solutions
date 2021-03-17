# Project Euler	Problem 058

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
$$
\begin{array}{ccccccc}
{\textbf{37}}&{36}&{35}&{34}&{33}&{32}&{\textbf{31}}\\
{38}&{\textbf{17}}&{16}&{15}&{14}&{\textbf{13}}&{30}\\
{39}&{18}&{\textbf5}&{4}&{\textbf3}&{12}&{29}\\
{40}&{19}&{6}&{1}&{2}&{11}&{28}\\
{41}&{20}&{\textbf7}&{8}&{9}&{10}&{27}\\
{42}&{21}&{22}&{23}&{24}&{25}&{26}\\
{\textbf{43}}&{44}&{45}&{46}&{47}&{48}&{49}
\end{array}
$$
It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?



## Solution

本题与[P028](../P028/P028_Note.md)是类似的。

本题不能够直接调用`Prime`工具类，这是因为我们要判断的素数实在是太分散了，使用简单的遍历判断方法仍然是有效的。

实现如下：

```python
#==========================================Solution
def is_prime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

limit = 15000 ** 2
def find_ans():
    spiral = 1
    spiral_prime = 0
    pointer = 1
    diff = 0
    for layer in range(2, int(limit ** 0.5 + 1)):
        diff += 2
        spiral += 4
        for i in range(4):
            pointer += diff
            if is_prime(pointer) == True:
                spiral_prime += 1
        if spiral_prime / spiral < 0.1:
            return diff + 1

print(find_ans())
#==========================================Answer
The Answer is 26241
```

