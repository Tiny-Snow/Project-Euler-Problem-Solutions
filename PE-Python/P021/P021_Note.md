# Project Euler	Problem 021

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Amicable numbers

Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).
If $d(a) = b$ and $d(b) = a$, where $a ≠ b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.

For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are $1, 2, 4, 71$ and $142$; so $d(284) = 220$.

Evaluate the sum of all the amicable numbers under $10000$.



## Solution

本题需要我们计算的是**因数和函数**。显然，因数和函数在质因数分解的基础上有以下计算公式：
$$
\sigma\left({n}\right)=\prod\limits_{k=1}^{s}{{{p_{k}^{\alpha_{k}+1}-1}\over{p_{k}-1}}}
$$
因此，实际上我们需要计算的就是 $n$ 的每个质因数 $p_k$ 及其幂次 $\alpha_k$ 。但是根据我们之前的经验，这样做的时间复杂度很大。因此，我们需要一个递推的方法。

我们仍然沿用[P012_Note](../P012/P012_Note.md)中的欧拉筛法来获取各个数的因子，利用下面的事实：
$$
\sigma(ab) = \sigma(a)\sigma(b),\ if\ gcd(a,b)=1 
$$
我们只需要稍微修改一下代码即可，获取因数和的算法如下：

```python
#==================================================================================================================================Solution
maxn = 10000
p_list = []
sumd_list = [0 for i in range(maxn + 1)]
sumd_list[1] = 1
prime_list = [1 for i in range(maxn + 1)]
prime_list[1] = 0
for p in range(1, maxn + 1):
    if prime_list[p] == 1:
        p_list.append(p)
        sumd_list[p] = 1 + p            # 质数的因子只有两个
    for j in range(len(p_list)):
        if p * p_list[j] > maxn:
            break
        prime_list[p * p_list[j]] = 0
        if p % p_list[j] == 0:          # 遍历至最小质因数
            p_divided_by_pj = p
            alpha_j = 1
            while(p_divided_by_pj % p_list[j] == 0):
                p_divided_by_pj /= p_list[j]
                alpha_j += 1
            sumd_list[p * p_list[j]] = sumd_list[int(p_divided_by_pj)] * int(((p_list[j] ** (alpha_j + 1) - 1) // (p_list[j] - 1)))
            break 
        else:                           # 没有遍历到质因数
            sumd_list[p * p_list[j]] = sumd_list[p] * sumd_list[p_list[j]]
```

上述代码进行了优化：将原先使用的字典全部换为了列表，进一步优化了时间复杂度和效率。



思考一个细节：如果将下面这行代码，也就是上面我们给出的事实，换作其下方一行“于公式更加相似”的代码，得到的结果是否正确呢？

```python
sumd_list[p * p_list[j]] = sumd_list[int(p_divided_by_pj)] * int(((p_list[j] ** (alpha_j + 1) - 1) // (p_list[j] - 1)))
```

```python
sumd_list[p * p_list[j]] = sumd_list[int(p_divided_by_pj)] * sumd_list[int(p * p_list[j] // p_divided_by_pj)]
```

事实上我们考虑 $4$ 这个数字，由于 $4$ 是 $2$ 的平方，将会有`p_divided_by_pj = 1`，而`sumd_list(4)`的初始值为`0`，显然不能得到正确结果。这个细节提示我们：**在计算机中实现数学公式一定要注意可能出现的特殊情况**。



得到了所有数字的因数和后，我们现在要考虑寻找 *Amicable numbers* 了。我们需要保证`d(a) = b and d(b) = a`，实际上就是`a = d(d(a))`，也就是说我们需要找到**因数和函数的二阶不动点**（该因数和需要减去自身）。

具体实现如下：

```python
#==================================================================================================================================Solution
amicable_num = [0 for i in range(maxn + 1)]         # 0表示不是amicable number，1代表是amicable number
amicable_sum = 0
for i in range(1, maxn):
    sumd_list[i] -= i
for i in range(1, maxn):
    if amicable_num[i] == 1:
        continue
    if sumd_list[i] <= maxn:
        if i == sumd_list[sumd_list[i]] and sumd_list[i] != i:
            amicable_sum += (i + sumd_list[i])
            amicable_num[i] = amicable_num[sumd_list[i]] = 1
print(amicable_sum)
#==================================================================================================================================Answer
The Answer is 31626
```

