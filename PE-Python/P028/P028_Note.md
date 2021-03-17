# Project Euler	Problem 028

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
$$
\begin{array}{ccccc}
{\textbf{21}} & {22} & {23} & {24} & {\textbf{25}}\\
{20} & {\textbf{7}} & {8} & {\textbf{9}} & {10}\\
{19} & {6} & {\textbf{1}} & {2} & {11}\\
{18} & {\textbf{5}} & {4} & {\textbf{3}} & {12}\\
{\textbf{17}} & {16} & {15} & {14} & {\textbf{13}}\\
\end{array}
$$
It can be verified that the sum of the numbers on the diagonals is $101$.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?



## Solution

似乎一种很直接的方法是去建立一个二维数组去逐一访问，但是这样势必会占用大量空间。有没有别的方法呢？

当然有了，我们观察到每一层螺旋都要选出4个角的数，每个角上的数之间的差为 $0,2,4,···$，并且每层的第一个角上的数与前一层最后一个角上的数的差为本层的角上的数之间的差，依此规律很容易找到所有的数，并且只需要用一个指针`pointer`去遍历即可。

实现如下：

```python
#==========================================Solution
spiral_diagonal_sum = 1
pointer = 1
diff = 0
for layer in range(2, (1001 + 1) // 2 + 1):
    diff += 2
    for i in range(4):
        pointer += diff
        spiral_diagonal_sum += pointer
print(spiral_diagonal_sum)
#==========================================Answer
The Answer is 669171001
```

