# Project Euler	Problem 064

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Odd period square roots

All square roots are periodic when written as continued fractions and can be written in the form:
$$
\sqrt N = a_0 + {1 \over a_1 + {1 \over a_2 + {1 \over a_3+…}}}
$$
For example, let us consider $23$:
$$
\sqrt {23} = 4 + \sqrt  {23} − 4 = 4 + {1 \over {1 \over \sqrt {23} - 4}}= 4 + {1 \over 1 + {\sqrt {23} − 3 \over 7}}
$$
If we continue we would get the following expansion:
$$
\sqrt {23} = 4 + {1 \over 1 + {1 \over 3 + {1 \over 1 + {1 \over 8 + …}}}}
$$
The process can be summarised as follows:

$$
\begin{array}{l}
{{a}_{0}{=}{4}{,}\frac{1}{\sqrt{23}{-}{4}}{=}\frac{\sqrt{23}{+}{4}}{7}{=}{1}{+}\frac{\sqrt{23}{-}{3}}{7}}\\
{{a}_{1}{=}{1}{,}\frac{7}{\sqrt{23}{-}{3}}{=}\frac{{7}{(}\sqrt{23}{+}{3}{)}}{14}{=}{3}{+}\frac{\sqrt{23}{-}{3}}{2}}\\
{{a}_{2}{=}{3}{,}\frac{2}{\sqrt{23}{-}{3}}{=}\frac{{2}{(}\sqrt{23}{+}{3}{)}}{14}{=}{1}{+}\frac{\sqrt{23}{-}{4}}{7}}\\
{{a}_{3}{=}{1}{,}\frac{7}{\sqrt{23}{-}{4}}{=}\frac{{7}{(}\sqrt{23}{+}{4}{)}}{7}{=}{8}{+}\sqrt{23}{-}{4}}\\
{{a}_{4}{=}{8}{,}\frac{1}{\sqrt{23}{-}{4}}{=}\frac{\sqrt{23}{+}{4}}{7}{=}{1}{+}\frac{\sqrt{23}{-}{3}}{7}}\\
{{a}_{5}{=}{1}{,}\frac{7}{\sqrt{23}{-}{3}}{=}\frac{{7}{(}\sqrt{23}{+}{3}{)}}{14}{=}{3}{+}\frac{\sqrt{23}{-}{3}}{2}}\\
{{a}_{6}{=}{3}{,}\frac{2}{\sqrt{23}{-}{3}}{=}\frac{{2}{(}\sqrt{23}{+}{3}{)}}{14}{=}{1}{+}\frac{\sqrt{23}{-}{4}}{7}}\\
{{a}_{7}{=}{1}{,}\frac{7}{\sqrt{23}{-}{4}}{=}\frac{{7}{(}\sqrt{23}{+}{4}{)}}{7}{=}{8}{+}\sqrt{23}{-}{4}}
\end{array}
$$
It can be seen that the sequence is repeating. For conciseness, we use the notation $\sqrt {23}=[4;(1,3,1,8)]$, to indicate that the block $(1,3,1,8)$ repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:
$$
\begin{array}{l, l}
{\sqrt 2=[1;(2)]} & {period=1}\\
{\sqrt 3=[1;(1,2)]} & { period=2}\\
{\sqrt 5=[2;(4)]} & {period=1}\\
{\sqrt 6=[2;(2,4)]} & {period=2}\\
{\sqrt 7=[2;(1,1,1,4)]} & {period=4}\\
{\sqrt 8=[2;(1,4)]} & {period=2}\\
{\sqrt {10}=[3;(6)]}& {period=1}\\
{\sqrt {11}=[3;(3,6)]} & {period=2}\\
{\sqrt {12}=[3;(2,6)]} & {period=2}\\
{\sqrt {13}=[3;(1,1,1,1,6)]} & {period=5}
\end{array}
$$
Exactly four continued fractions, for $N≤13$, have an odd period.

How many continued fractions for $N≤10000$ have an odd period?



## Solution

本题是有关**二次根式的简单循环连分数**的问题，需要用到以下的结论：

通过观察我们可以发现，连分数可以写成以下形式：
$$
\sqrt N = a_0 + {\sqrt N - x_0 \over y_0} = a_0 + {1 \over a_1 + {\sqrt N - x_1 \over y_1}} = ···
$$
其中，$a_0 = [\sqrt n]$，$x_ 0 = a_0$，$ y_0 = 1$，并且有递推式：
$$
{y_{k-1} \over {\sqrt N - x_{k-1}}} = a_{k} + {\sqrt N - x_{k} \over y_{k}}
$$
我们有：
$$
LHS - a_k= {y_{k-1}(\sqrt N + x_{k-1}) - a_k(N - x_{k-1}^2) \over N - x_{k-1}^2}
$$
其中：
$$
a_k = \left[{y_{k-1} \over {\sqrt N - x_{k-1} ^ 2}}\right]
$$
解得：
$$
{y_k = {N - x_{k-1}^2 \over y_{k-1}}},{x_k = {a_k \over y_{k-1}}(N - x_{k-1}^2)}
$$
上述递推式成立的充要条件是：
$$
N - x_{k-1}^2 \equiv 0\ (\bmod y_{k-1})
$$


我们有结论：**二次代数数都是循环连分数，并且循环节从 $a_1$ 开始**。（该结论并用于验证**佩尔方程可解性**）也就是说，我们只需要找到一定存在的循环节即可。

类似于无限小数找循环节，我们知道，如果我们需要确定循环节，就**需要找到足够的信息来确定当前状态，该状态包括当前的数、并且可以推导出下一个数**。在本题中，我们需要当前的数 $a_k$，还需要用于确定 $a_{k+1}$ 的 $x_k,y_k$ ，如果这些信息都相同，那么状态就相同，之后必定会循环。这是**确定循环节的通法**。



根据上述数学方法，我们实现如下：

```python
#=====================================================================Solution
from math import sqrt, gcd

def is_odd(n):
    a = int(sqrt(n))
    x = a
    y = 1
    a = int(y / (sqrt(n) - x))
    x0 = x
    x = int(a * (n - x0 ** 2) / y - x0)
    y = int((n - x0 ** 2) / y)
    state0 = [a, x, y]
    state_list = [state0]
    while True:
        a = int(y / (sqrt(n) - x))
        x0 = x
        x = int(a * (n - x0 ** 2) / y - x0)
        y = int((n - x0 ** 2) / y)
        state = [a, x, y]
        if state in state_list:
            break
        state_list.append(state)
    if state == state0 and len(state_list) % 2 != 0:
        return True
    return False

all_odd = 0
for n in range(2, 10000 + 1):
    if sqrt(n) == int(sqrt(n)):
        continue
    if is_odd(n) == True:
        all_odd += 1
print(all_odd)
#=====================================================================Answer
The Answer is 1322
```

