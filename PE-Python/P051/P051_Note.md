# Project Euler	Problem 051

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Prime digit replacements

By replacing the $1^{st}$ digit of the 2-digit number $*3$, it turns out that six of the nine possible values: $13, 23, 43, 53, 73$, and $83$, are all prime.

By replacing the $3^{rd}$ and $4^{th}$ digits of $56**3$ with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: $56003, 56113, 56333, 56443, 56663, 56773$, and $56993$. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.



## Solution

本题首先需要实现**替换数字**这一功能，我们实现的方法是传入原数字和更改的位数列表，利用字符串的切片进行操作。

注意这一功能实现的细节：

- 我们需要**排除位数改变的情况**，这个比较容易被忽视。
- 我们**默认改变的位数**`index`**不可能为最后一位**，这是因为若改变最后一位的话，10个数字中有5个是偶数，不符合条件。

我们传入的改变位数列表`index_list`需要从`itertools.combinations`方法中获得所有组合情况，再判断符合的情况，一旦符合立即输出最小的素数（注意，不是当前遍历的原数字`n`，而是得到的最小素数）。

可惜的是，上述方法并不能有效地处理重复情况，事实上也很难得出一种有效地去重方法。这是因为存在相当一部分的数字，都可以通过更换一定位数的相同数字的操作来变为相同数字，很难找到其中的规律。

结合上述分析的实现如下：

```python
#===================================================================================Solution
import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append(BASE_DIR.partition('P051')[0] + 'Utility Class')

from prime_utility import *
limit = 1000000
prime_class = Prime(limit)
prime_class._traverse()

import itertools

def transfer(n: str, index_list: list):
    prime_num = 0
    min_p = limit
    for i in range(0, 10):
        p = n
        for index in index_list:
            p = p[:index] + str(i) + p[index + 1:]
        if len(str(int(p))) != len(str(int(n))):              # 排除位数改变的情况
            continue
        if prime_class._is_prime(int(p)) == True:
            prime_num += 1
            min_p = min(min_p, int(p))
    if prime_num >= 8:
        return min_p
    return False

def find_ans():
    for n in range(56003, limit):
        n_len = len(str(n))
        for index_num in range(1, n_len):
            for index_list in itertools.combinations([i for i in range(0, n_len - 1)], index_num):
                ans = transfer(str(n), list(index_list))
                if ans != False:
                    return ans

print(find_ans())
#===================================================================================Answer
The Answer is 121313
```

