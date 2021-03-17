# Project Euler	Problem 038

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:
$$
192 × 1 = 192\\
192 × 2 = 384\\
192 × 3 = 576
$$
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of $192$ and $(1,2,3)$

The same can be achieved by starting with 9 and multiplying by $1, 2, 3, 4$, and $5$, giving the pandigital, $918273645$, which is the concatenated product of $9$ and $(1,2,3,4,5)$.

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with $(1,2, ... , n)$ where $n > 1$?



## Solution

关键在于确定遍历范围，显然当遍历范围达到 $10000$ 时，此时 $n_{min} = 2$ 会使得`product`超过9位，因此遍历范围应该设置在 $[1,9999]$ 。

另外，我们使用Python的`sorted()`内置函数实现排序以便判断，注意**字符串排序后，应该将迭代器传入**`join()`**方法中**。实现如下：

```python
#================================================================Solution
product_max = 0
for n in range(1, 10000):
    k = 2
    product = str(n)
    while len(product) < 9:
        product += str(k * n)
        k += 1
    if ''.join(sorted(product)) == '123456789':
        product_max = max(product_max, int(product))
print(product_max)
#================================================================Answer
The Answer is 932718654
```

