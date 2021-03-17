# Project Euler	Problem 062

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Cubic permutations

The cube, $41063625 (345^3)$, can be permuted to produce two other cubes: $56623104 (384^3)$ and $66430125 (405^3)$. In fact, $41063625$ is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.



## Solution

本题的分析过程如下：

- 首先要确定以底数还是三次方数进行遍历。我们的原则是：**遍历最紧凑的数列**，因此应当以底数进行遍历。
- 遍历的过程中不应该对每个底数产生的三次方数遍历排列，这样会造成巨量的重复判断。解决的方法是：对所有相同排列的数选取一个**特征值**（例如**最大值/最小值**），将这一系列的数中的 *cube* 数量储存在该特征值上。这是**对于数字排列的通用解法**。
- 注意上述解法中，需要储存键值对 *cube* 特征值 : 排列中 *cube* 的数量，显然由于 *cube* 可能会非常大且十分分散，因此不适合使用列表，应当使用字典。
- 如果我们选取最小值为特征值，“对应”是没有问题的，即排列中的每个数都对应到了同一个值上，但是**该值不是我们要求的最小值**——我们要求的最小值应当是能够产生 *cube* 的最小值。一个简单的方法是：可以另外开辟出一个字典，来对应排列最小值和能够产生 *cube* 的最小值（即储存首先得到该排列最小值的 *cube* ）。
- 当然，如果我们选取最大值为特征值，仍然存在上述输出最小值的问题，而且需要重新开辟空间来储存过程中遍历到的 *cube* 以便得到答案中的最小值，实际应用中会比上一种方法效率低得多。因此，在实际实现中，我们使用最小值作为特征值。

具体的实现如下：

```python
#=========================================================================================================================Solution
def get_min_permutation(n):        # 得到排列最小数
    return ''.join(sorted(str(n ** 3)))

min_dict = {}                       # 保存排列最小数和对应排列中cube的个数，从而不需要对每个三次方数重新排列
num_dict = {}                       # 保存每个三次方数对应的排列最小数和能够产生cube的排列最小数
cube = 1
while True:
    min_cube = get_min_permutation(cube)
    if min_cube not in min_dict:
        min_dict[min_cube] = 1
        num_dict[min_cube] = cube ** 3
        cube += 1
        continue
    min_dict[min_cube] += 1
    if min_dict[min_cube] == 5:
        print(num_dict[min_cube])
        break
    cube += 1
#=========================================================================================================================Answer
The Answer is 127035954683
```

