# Project Euler	Problem 066

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Diophantine equation

Consider quadratic Diophantine equations of the form:
$$
x^2 – Dy^2 = 1
$$
For example, when $D=13$, the minimal solution in $x$ is $649^2 – 13×180^2 = 1$.

It can be assumed that there are no solutions in positive integers when $D$ is square.

By finding minimal solutions in $x$ for $D = {2, 3, 5, 6, 7}$, we obtain the following:
$$
\begin{array}{c}
3^2 – 2×2^2 = 1\\
2^2 – 3×1^2 = 1\\
\textbf9^2 – 5×4^2 = 1\\
5^2 – 6×2^2 = 1\\
8^2 – 7×3^2 = 1
\end{array}
$$
Hence, by considering minimal solutions in $x$ for $D ≤ 7$, the largest $x$ is obtained when $D=5$.

Find the value of $D ≤ 1000$ in minimal solutions of $x$ for which the largest value of $x$ is obtained.



## Solution

经过[Problem 64](../P064/P064_Note.md)和[Problem 65](../P065/P065_Note.md)的铺垫，终于到了 ***Pell equation*** 了！这里我们解的是**第一类佩尔方程**，即 *Pell equation*Ⅰ 。



佩尔方程的解一般十分巨大，肯定不能遍历求解。一般来说，要求用计算机解第一类佩尔方程的最小解，多用**连分数解法**。

注意如下的变形：
$$
x^2 – Dy^2 = 1 \Longrightarrow x = \sqrt {Dy ^ 2 + 1}
$$
显然，当 $x \rightarrow \infty$ 时， $y \rightarrow \infty$ ，并且有 $\sqrt D \approx x / y$ 。另外，我们知道 $\sqrt D$ 可以用连分数无限逼近。如果满足$|p^2-a^2q^2|<a$，那么 $p/q$ 必为 $a$ 的一个渐近值。所谓佩尔方程的连分数解法，就是去依次检验渐近值 $p_n/q_n$ ，如果一旦 $x = p_n, y = q_n$ 满足佩尔方程，那么我们就取得了最小解。



对于连分数 $[a;a_1,a_2,···,a_n]$ ，$p_n,q_n$ 的递推公式如下：
$$
\left\{{\begin{array}{l}
{p_1 = a, p_2 = aa_1 + 1, ···,p_{k+1} = a_{k}p_{k} + p_{k-1},k \geq 2}\\
{q_1 = 1, q_2 = a_1, ···,q_{k+1} = a_{k}q_{k} + q_{k-1},k \geq 2}
\end{array}}\right.
$$
事实上，最小解满足：
$$
(x,y) =
\left\{{\begin{array}{ll}
{(p_{n-1},q_{n-1})} & {if\ n\ is\ even}\\
{(p_{2n-1},q_{2n-1})} & {if\ n\ is\ odd}
\end{array}}\right.
$$


对于得到的最小解 $x_0 = p, y_0 = q$，佩尔方程全部根的集合为：
$$
x^2 – Dy^2 = (p^2-Dq^2)^n = 1
$$
由佩尔方程解的递归式：
$$
\left\{{\begin{array}{l}
{x_{n+1} = x_0x_n + Dy_0y_n}\\
{y_{n+1} = y_0x_n + x_0y_n}
\end{array}}\right.
$$
得通解为：
$$
\left\{{\begin{array}{l}
{x = {(p+\sqrt Dq)^n + (p-\sqrt Dq)^n \over 2}}\\
{x = {(p+\sqrt Dq)^n - (p-\sqrt Dq)^n \over 2\sqrt D}}
\end{array}}\right.
$$


以上数学结论，详细证明可参见：https://www.math.uchicago.edu/~may/VIGRE/VIGRE2008/REUPapers/Yang.pdf



根据上述数学结论，我们只需要根据连分数的递推式，遍历找到最小解即可。

实现如下：

```python
#===================================================Solution
from fractions import Fraction
from math import sqrt

def get_state_list(n):
    a = int(sqrt(n))
    x = a
    y = 1
    state0 = [a, x, y]
    a = int(y / (sqrt(n) - x))
    x0 = x
    x = int(a * (n - x0 ** 2) / y - x0)
    y = int((n - x0 ** 2) / y)
    state1 = [a, x, y]
    state_list = [state0, state1]
    while True:
        a = int(y / (sqrt(n) - x))
        x0 = x
        x = int(a * (n - x0 ** 2) / y - x0)
        y = int((n - x0 ** 2) / y)
        state = [a, x, y]
        if state in state_list:
            break
        state_list.append(state)
    return state_list

def get_fraction(state_list):
    a = state_list[0][0]
    p0 = a
    q0 = 1
    p1 = a * state_list[1][0] + 1
    q1 = state_list[1][0]
    if len(state_list) == 2:
        i = 1
    else:
        i = 2
    while p1 ** 2 - D * (q1 ** 2) != 1:
        p1, p0 = state_list[i][0] * p1 + p0, p1
        q1, q0 = state_list[i][0] * q1 + q0, q1
        if i == len(state_list) - 1:
            i = 1
        else:
            i += 1
    frac = Fraction(p1, q1)
    return frac

ans_x = 0
ans_D = 0
for D in range(1, 1000):
    if sqrt(D) == int(sqrt(D)):
        continue
    D_state_list = get_state_list(D)
    D_frac = get_fraction(D_state_list)
    x = D_frac._numerator
    if x > ans_x:
        ans_x = x
        ans_D = D
print(ans_D)
#===================================================Answer
The Answer is 661
```

