# Project Euler	Problem 027

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Quadratic primes

Euler discovered the remarkable quadratic formula:
$$
n^2+n+41
$$
It turns out that the formula will produce 40 primes for the consecutive integer values $0≤n≤39$. However, when $n=40$,$40^2+40+41=40(40+1)+41$ is divisible by $41$, and certainly when $n=41$,$41^2+41+41$ is clearly divisible by $41$.

The incredible formula $n^2−79n+1601$ was discovered, which produces 80 primes for the consecutive values $0≤n≤79$. The product of the coefficients, $−79$ and $1601$, is $−126479$.

Considering quadratics of the form:

​	$n^2+an+b$, where$|a|<1000$ and $|b|≤1000$
​	where $|n|$ is the modulus/absolute value of $n$
​	e.g. $|11|=11$ and $|−4|=4$

Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with n=0.



## Solution

解决方法就是首先得到所有素数，然后遍历 $a,b$ ，实现如下：

```python
#===========================================================Solution
#========================================遍历素数
maxn = 1000 * 1000 + 1000 * 1000 + 1000
p_list = []
prime_list = [1 for i in range(maxn + 1)]
prime_list[1] = 0
for p in range(1, maxn + 1):
    if prime_list[p] == 1:
        p_list.append(p)
    for j in range(len(p_list)):
        if p * p_list[j] > maxn:
            break
        prime_list[p * p_list[j]] = 0
        if p % p_list[j] == 0:
            break
#========================================寻找a, b
final_a = 0
final_b = 0
p_num_max = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        p_num = 0
        while(n ** 2 + a * n + b > 0):
            if prime_list[(n ** 2 + a * n + b)] == 1:   #注意负数的情况
                p_num += 1
                n += 1
            else:
                break
        if p_num > p_num_max:
            final_a = a
            final_b = b
            p_num_max = p_num
print(final_a * final_b)
#===========================================================Answer
The Answer is -59231
```

这里有一个技巧：我们没有使用`in`成员操作符判断素数，而是用`prime_list`判断，事实上**列表下标访问要比**`in`**快很多**，因此实际使用时一般利用`prime_list`判断素数（在前面问题的解决中我们一般用的是`in`，甚至使用的是字典而非列表，之后我们将使用优化后的算法）。

使用`prime_list`时就要注意可能存在的**负数情况**，由于下标访问会将负数通过二进制换为正数，但得到的结果将是错误的，因此碰到负数要先舍去。