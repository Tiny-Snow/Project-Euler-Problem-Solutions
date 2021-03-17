# Project Euler	Problem 004

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is $9009 = 91 × 99$.

Find the largest palindrome made from the product of two 3-digit numbers.



## Solution

本题利用下述代码能够很方便的得到答案。数据并不大，速度也很快。

```python
#============================================================Solution 1
max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        ij = str(i * j)
        if ij == ''.join(reversed(ij)) and int(ij) > max:
            max = int(ij)
print(max)

#============================================================Answer
The Answer is 906609
```

显然，有以下简单的改进方法（并不改变算法的本质）：

- **不妨假设**`i >= j`，这会避免多次重复的计算。
- **从 $1000$ 向 $100$ 遍历而不是从 $100$ 向 $1000$ 遍历**，这是因为我们要找最大的回文数。

稍加修改即有：

```python
#============================================================Solution 2
max = 0
for i in reversed(range(100, 1000)):
    for j in reversed(range(100, i + 1)):
        ij = str(i * j)
        if ij == ''.join(reversed(ij)) and int(ij) > max:
            max = int(ij)
print(max)

#============================================================Answer
The Answer is 906609
```

当然，这是一个数学问题。我们可以考虑：这是一个**六位回文数**，将六位回文数展开，有下述结果：
$$
\overline{abccba}=100001a+10010b+1100c=11(9091a+910b+100c)
$$
也就是说，必然有一个数是 $11$ 的倍数。当我们确定一个数不为 $11$ 的倍数之后，另一个数就可以以 $11$ 为间隔遍历了。

实现代码如下：

```python
#============================================================Solution 3
max = 0
for i in reversed(range(100, 1000)):
    if i % 11 != 0:
        for j in reversed(range(110, i + 1, 11)):
            ij = str(i * j)
            if ij == ''.join(reversed(ij)) and int(ij) > max:
                max = int(ij)            
    else:
        for j in reversed(range(100, i + 1)):
            ij = str(i * j)
            if ij == ''.join(reversed(ij)) and int(ij) > max:
                max = int(ij)
print(max)

#============================================================Answer
The Answer is 906609
```

Solution 3的想法来源于 *Lster* 。
