# Project Euler	Problem 079

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Passcode derivation

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was $531278$, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: $317$.

The text file, [keylog.txt](https://projecteuler.net/project/resources/p079_keylog.txt), contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.



## Solution

准确来说，严格解答本问题需要获得所有数之间的位置关系（更复杂的还需要考虑到重复出现数字的情况），这样一来问题会变得十分复杂，可能需要模糊/遗传算法。在这里我们只讨论所有数字至多出现一次的情况。

事实上，为了简化问题，我们解密码时可以假定只有一个可能解（即在样本数量足够大时，输出一个**可能性最大**的解）。在本问题中，我们衡量可能性的方法是比较数字分别在密钥的 $1,2,3$ 位上出现的次数。

例如，我们首先可以确定首位和末位的数字 $a_{1},a_{n}$，这两个数字必然会出现在密钥的 $1,3$ 位，但不会出现在 $2$ 位。

之后，在去掉上面的 $a_1,a_n$ 后，我们还可以确定首二位和末二位的数字 $a_{2},a_{n-1}$：$a_2$ 必然在密钥的 $1$ 位上出现次数最多， $a_{n-1}$必然在密钥的 $3$ 位上出现次数最多。

但在之后，我们不能够继续确定了，否则结果将会不是很准确。我们可以先由密钥 $1$ 位（或 $3$ 位）数字出现次数情况，按从多到少（或从少到多）的次序初步得到中间位 $a_3,···,a_{n-2}$ 的排序。

如上所述，这样有可能是不准确的，我们需要通过更准确的密钥 $2$ 位情况来判断：对于前半部分 $a_3,···,a_{n \over 2}$ ，按照在密钥 $2$ 位出现次数从小到大重新排序；对于后半部分 $a_{n \over 2 + 1},···,a_{n-2}$ ，按照在密钥 $2$ 位出现次数从大到小重新排序。上述解法分前半部分和后半部分是依据了对称性（见下述概率分析）。



上述解法依据的是概率分析，统计各个数字出现在 $1,2,3$ 位上的频数作为判断，如下：

$a_k$ 出现在密钥 $1$ 位的次数为：
$$
\begin{array}{ll}
{(a_k)_1 = C_{n-k}^{2}} & {k\leq n-2}
\end{array}
$$
$a_k$ 出现在密钥 $3$ 位的次数为：
$$
\begin{array}{ll}
{(a_k)_3 = C_{k-1}^{2}} & {k \geq 3}
\end{array}
$$
$a_k$ 出现在密钥 $2$ 位的次数为：
$$
\begin{array}{ll}
{(a_k)_2 = (k-1)(n-k)} & {2 \leq k \leq n-1}
\end{array}
$$


根据上述解法，我们写出了下述程序：

```python
import os
BSER_DIR = os.path.dirname(os.path.abspath(__file__))

with open(BSER_DIR + '\p079_keylog.txt', mode = 'r') as datafile:
    key_list = datafile.read().split()

key1_list = []
key2_list = []
key3_list = []
for key in key_list:
    key1_list.append(key[0])
    key2_list.append(key[1])
    key3_list.append(key[2])
key1_dict = {}.fromkeys(set(key1_list))
key2_dict = {}.fromkeys(set(key2_list))
key3_dict = {}.fromkeys(set(key3_list))
for i in set(key1_list):
    key1_dict[i] = key1_list.count(i)
for i in set(key2_list):
    key2_dict[i] = key2_list.count(i)
for i in set(key3_list):
    key3_dict[i] = key3_list.count(i)

n = len(key2_dict) + 2              # n表示密码位数，下面假定n为偶数
num_list = ['' for _ in range(n)]

# 获取首位和末位
for i in key1_dict:
    if i not in key2_dict:
        num_list[0] = i
        break
for i in key3_dict:
    if i not in key2_dict:
        num_list[-1] = i
        break

# 获取首二位和末二位
key1_dict.pop(num_list[0])
key3_dict.pop(num_list[-1])
key1_dict = list(sorted(list(key1_dict.items()), key = lambda x: x[1], reverse = True))
key3_dict = list(sorted(list(key3_dict.items()), key = lambda x: x[1], reverse = True))
num_list[1] = key1_dict[0][0]
num_list[-2] = key3_dict[0][0]

# 初步获取余下的中间位
middle = key1_dict[1:]

# 根据key2的统计对中间位结果进行修改
key2_dict.pop(num_list[1])
key2_dict.pop(num_list[-2])
for i in range(len(middle) // 2 - 1):
    for j in range(i, len(middle) // 2 - 1):
        if key2_dict[middle[j][0]] > key2_dict[middle[j + 1][0]]:
            middle[j], middle[j + 1] = middle[j + 1], middle[j]
for i in range(len(middle) // 2, len(middle) - 1):
    for j in range(i, len(middle) - 1):
        if key2_dict[middle[j][0]] < key2_dict[middle[j + 1][0]]:
            middle[j], middle[j + 1] = middle[j + 1], middle[j]

# 输出最终结果
for i in range(len(middle)):
    num_list[i + 2] = middle[i][0]
num = ''.join(num_list)
print(int(num))
```

上述程序输出结果为`73612890`。但可惜的是，这并不是正确答案！观察数据可以发现， $1$ 必然排在 $6$ 的前面，但是按照概率我们将其排在了后面。显然，当样本量过少而且很偏时，我们的概率估计失效了。



那么，正确解答问题，就必须要保证顺序**满足位置关系**。事实上在数字不重复的情况下并不困难，只需要统计位于每个数字之后的数字有几个即可。例如，末尾数字没有之后的数字，末二位数字只有1个，······，首位数字有 $n-1$个，按照数字数量进行排序即可。

按照正确解法（解法二）的实现如下：

```python
#=================================================================================Solution
import os
BSER_DIR = os.path.dirname(os.path.abspath(__file__))

with open(BSER_DIR + '\p079_keylog.txt', mode = 'r') as datafile:
    key_list = datafile.read().split()

location_dict = {}                      # 储存位置关系，值列表为键的后面的值及其个数
key2_set = set()
for key in key_list:
    k1, k2, k3 = key
    key2_set = set(list(key2_set) + [k2])
    if k1 not in location_dict:
        location_dict[k1] = [[k2, k3], 2]
    else:
        location_dict[k1][0] = list(set(location_dict[k1][0] + [k2, k3]))
        location_dict[k1][1] = len(location_dict[k1][0])
    if k2 not in location_dict:
        location_dict[k2] = [[k3], 1]
    else:
        location_dict[k2][0] = list(set(location_dict[k2][0] + [k3]))
        location_dict[k2][1] = len(location_dict[k2][0])
    if k3 not in location_dict:
        location_dict[k3] = [[], 0]

n = len(key2_set) + 2                   # n表示密码位数，下面假定n为偶数
num_list = ['' for _ in range(n)]
for location in location_dict:
    num_list[n - location_dict[location][1] - 1] = location
num = ''.join(num_list)
print(int(num))
#=================================================================================Answer
The Answer is 73162890
```

