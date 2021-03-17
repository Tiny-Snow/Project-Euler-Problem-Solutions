# Project Euler	Problem 074

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Digit factorial chains

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
$$
1! + 4! + 5! = 1 + 24 + 120 = 145
$$
Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
$$
\begin{array}{l}
{169 → 363601 → 1454 → 169}\\
{871 → 45361 → 871}\\
{872 → 45362 → 872}
\end{array}
$$
It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
$$
\begin{array}{l}
{69 → 363600 → 1454 → 169 → 363601 (→ 1454)}\\
{78 → 45360 → 871 → 45361 (→ 871)}\\
{540 → 145 (→ 145)}
\end{array}
$$
Starting with $69$ produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?



## Solution

本题又是找循环的问题。按照以前类似题目的做法，要得到每个数的链长，我们还是要**储存中途的结果**，记录每一次链上出现的数对应的最短链长以减少遍历次数，具体实现是使用递归函数。

注意本题的链可能会很长，当链长超过60之后就不符合要求，应当停止遍历，不然会报错`RecursionError`。这是因为Python的递归深度默认不超过1000。

基于递归的事先如下：

```python
#=====================================================================================================================Solution
from math import factorial

limit = 1000000
chain_dict = {}             # 储存在chains中遍历过的数与chain长度的对应关系

def find_chain_len(n, start, chain_list):           # 对于以start位置的n开始的chain求len；如果chain_len大于60次返回False
    chain_len = start
    if chain_len >= 60:                             # 长于60的chain直接舍去
        return False
    if n in chain_dict:                             # 尝试寻找以前遍历的结果
        chain_len += chain_dict[n] - 1
        return chain_len
    now_n = 0
    for i in str(n):
        now_n += factorial(int(i))
    if now_n in chain_list:                         # 下一个数形成环得到结果
        return chain_len
    chain_list.append(now_n)                        # 没有形成环，记录在chain中
    chain_len = find_chain_len(now_n, start + 1, chain_list)
    if chain_len != False:                          # 如果得到非False的len结果，将len储存在dict中并返回
        chain_dict[n] = chain_len - start + 1
        return chain_len
    return False

num = 0
for n in range(1, limit + 1):
    if find_chain_len(n, 1, [n]) == 60:
        num += 1
print(num)
#=====================================================================================================================Answer
The Answer is 402
```

