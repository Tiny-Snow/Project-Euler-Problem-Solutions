# Project Euler	Problem 042

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Coded triangle numbers

The $n^{th}$ term of the sequence of triangle numbers is given by, $t_n = n(n+1)/2$; so the first ten triangle numbers are:
$$
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
$$
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for $SKY$ is $19 + 11 + 25 = 55 = t_10$. If the word value is a triangle number then we shall call the word a triangle word.

Using [words.txt](https://projecteuler.net/project/resources/p042_words.txt) (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?



## Solution

本题并不困难，但是我们要寻求效率更高的算法。在得到所有 *word* 的 *word value* 后，如何判断它是不是一个 *triangle word* 呢？简单来说，就是要把 *2 × word value* 分解成 $n(n+1)$ 的形式。

显然，有：$[\sqrt {2 \times word\ value}] = [\sqrt {n(n+1)}] = n$ ，这样计算出 $n$ 以后就可以判断*2 × word value*是否为 $n(n+1)$ 了。这样我们就能快速判断 *triangle word* ，而无需遍历出所有的 *triangle word* 。

实现如下：

```python
#=================================================================Solution
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(BASE_DIR + '/p042_words.txt', mode = 'r') as datafile:
    data_str = datafile.read()
    data = list(data_str.split(','))

def word_score(word):
    score = 0
    for char in word:
        score += ord(char) - 64
    return score

triangle_words = 0

for i in range(len(data)):
    data[i] = word_score(data[i][1:-1])
    n = int((2 * data[i]) ** 0.5)
    if n * (n + 1) == 2 * data[i]:
        triangle_words += 1
print(triangle_words)
#=================================================================Answer
The Answer is 162
```

当然，准确来说，解二次方程有 $n = (\sqrt {1+8\times word\ value}-1)/2$ ，因此就需要保证 $1+8t$ 为奇数的完全平方数。这是另外一种判断方法。