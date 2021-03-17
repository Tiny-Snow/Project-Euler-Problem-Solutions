# Project Euler	Problem 007

<p align="right"><i>Tiny Snow</i></p>



## Problem

### 10001st prime

By listing the first six prime numbers: $2$, $3$, $5$, $7$, $11$, and $13$, we can see that the $6_{th}$ prime is $13$.

What is the $10 001_{st}$ prime number?



## Solution

本题的实质是让我们计算**素数个数**$\pi (n)$。



寻找素数，首先要指定一个区间包含了我们要找的所有素数。这个问题需要的是素数定理：



​	**素数定理**（***the Prime Number Theorem, PNT***）

​	当 $x\rightarrow\infty$ 时，不超过 $x$ 的素数个数 $\pi(x)$ 满足：
$$
\pi (x)\sim{{x}\over{\ln(x)}}
$$


本题中，我们要估计的是第 $10001$ 个素数，按照素数定理指出 $x\approx 116671$ 。

从下述结果中，我们将从实际验证这一结果。



本题的另外一个关键在于测试素数，我们肯定不能用最原始的试除法，而应该采用**筛法**。最古老的素数筛法是埃拉托斯特尼筛法：



​	**埃拉托斯特尼筛法**（***sieve of Eratosthenes***）

​	要得到 $[2,n]$ 以内的所有素数，只需要把不大于 $\sqrt n$ 的所有素数的倍数剔除，剩下的都是素数。





下面是使用埃拉托斯特尼筛法的一个实现：

```python
#=============================================================Solution 1
maxn = 116672
p_num = 0
# 初始化认为全部为素数，1为素数，0不为素数
prime_dict = {}.fromkeys(range(1, maxn), 1)   
prime_dict[1] = 0
for p in prime_dict:
    if prime_dict[p] == 1:
        for i in range(p ** 2, maxn, p):    # 筛去所有的p的倍数
            prime_dict[i] = 0
        p_num += 1
        if p_num == 10001:
            print(p)
            break
#=============================================================Answer
The Answer is 104743
```



这个筛法对于这个小区间已经够快了，但是注意到该筛法存在重复筛选——对于每个合数的每个非 $1$ 因子，该合数均被筛了一次。

如何改进该筛法呢？实现的关键在于要保证每个合数只被筛一次——保证**每个合数都被其最小质因数筛去**。

实现该要求的筛法称为**欧拉线性筛法**。该筛法的实现关键是**固定了被筛去合数的形式**，**只会被其最小质因数筛去一次**。



​	**欧拉线性筛法**

​	依次将每个找到的素数存储起来。对于遍历的每个 $p$ ，显然其所有素因数都已经被找到。

​	此时不是简单地筛去 $p$ 所有的倍数，而是以 $p$ 为倍数、依次以找到的素因子为最小素因子来筛去相应的合数。

​	因此，遍历素因子的时候，需要保证当前的素因子是合数的最小素因子，那么当遍历至 $p$ 的最小素因子时应该立即跳出循环。

​	上述操作保证了每个合数只会被其最小素因数筛去，并且只会被筛去一次。这是由于被筛去的合数拥有 $n = p_i · p$ 的形式（其中 $p_i$ 为 	$[2,p-1]$ 内的素数），当该合数的最小素因数 $p_m > p$ 时不可能被筛去，因此每个合数只会被其最小素因数筛去；当该合数的最小素	因数位于 $[2,p]$ 内时，被筛去的条件必须要满足 $n = p_i · p$ 的形式，实际上必须有 $p_m = p_i$，那么 $p$ 就是固定的，只会被筛去一次。



使用欧拉筛法的实现如下：

```python
#=============================================================Solution 2
maxn = 116672
p_list = []
prime_dict = {}.fromkeys(range(1, maxn), 1)
prime_dict[1] = 0
for p in list(prime_dict.keys()):
    if prime_dict[p] == 1:
        p_list.append(p)
    for j in range(len(p_list)):
        if p * p_list[j] > maxn:
            break
        prime_dict[p * p_list[j]] = 0
        if p % p_list[j] == 0:
            break
print(p_list[10000])
#=============================================================Answer
The Answer is 104743
```

事实上，对于**积性函数**，上述线性筛法的思想都是通用的。



另外，关于编码方面，有一个遍历字典的易错点：

Python 3规定遍历字典的时候（即在 `for i in dict`时）不能修改字典元素，也就是说，下面的代码会报错：

```python
for i in dict:
    dict[i] = None
#=============================================================
RuntimeError: dictionary changed size during iteration
```

如果需要修改字典元素，就不能采用直接遍历字典的方法（直接遍历`keys()`或`values()`也不行），如下：

```python
for i in list(dict.keys()):
    dict[i] = None
```

