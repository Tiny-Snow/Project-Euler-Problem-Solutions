# Project Euler	Problem 022

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Names scores

Using [names.txt](https://projecteuler.net/project/resources/p022_names.txt) (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth $3 + 15 + 12 + 9 + 14 = 53$, is the 938th​ name in the list. So, COLIN would obtain a score of $938 × 53 = 49714$.

What is the total of all the name scores in the file?



## Solution

本题可以直接调用相应的字典排序函数，实现如下：

```python
#==================================================================Solution
#=================================================储存数据
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(BASE_DIR + '/p022_names.txt', mode = 'r') as datafile:
    data_str = datafile.read()
    data = list(data_str.split(','))
for i in range(len(data)):
    data[i] = data[i][1:-1]         # 除去两侧引号
#=================================================排序+计算
data = sorted(data)
def word_score(word):
    score = 0
    for char in word:
        score += ord(char) - 64
    return score
sum_score = 0
for i in range(len(data)):
    sum_score += word_score(data[i]) * (i + 1)
print(sum_score)
#==================================================================Answer
The Answer is 871198282
```

