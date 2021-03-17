# Project Euler	Problem 024

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, $3124$ is one possible permutation of the digits $1, 2, 3$ and $4$. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of $0, 1$ and $2$ are:
$$
012\  021\  102\  120\  201\  210
$$
What is the millionth lexicographic permutation of the digits $0, 1, 2, 3, 4, 5, 6, 7, 8$ and $9$?



## Solution

本题我们没有必要借助编程计算，只需要依靠计算器计算即可。

我们知道***Lexicographic permutations***，也就是**字典排序**，是从右至左进行的。例如，在进行 $1,2,3,4,5$ 的字典排序时，首先会完成 $2345$ 的字典排序，然后将 $1$ 与 $2$ 交换位置，再进行 $1345$ 的排序，依此类推地进行下去。

依此规律，我们知道完成 $9$ 个数的字典排序需要 $9! = 362880$ 次，有 $9!\times2 <1000000<9!\times 3$ ，也就是第一个数字为 $2$ ，余下 $274240$ 次。

接下来对 $013456789$ 进行字典排序（注意已经进行过一次 $123456789$ 和 $023456789$的字典排序了），有 $8!\times 6<274240<8!\times 7$ ，因此第二个数字是 $7$ ，余下 $32320$ 次。

…… ……

通过上述规律的寻找，我们了解实际上就是寻找下面的表达式：
$$
1000000=a_9\times9!+a_8\times8!+···+a_1\times1!
$$
其中，根据字典排序轮数 $a_9,a_8,···,a_1$ 来求出 $1000000$ 个数的第 $1,2,···,9$ 位的数字。

得到：第 $1000000$ 个数为：$2783915460$ 。