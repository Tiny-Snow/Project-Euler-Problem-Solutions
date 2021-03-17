# Project Euler	Problem 006

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Sum square difference

The sum of the squares of the first ten natural numbers is ,
$$
1^2+2^2+...+10^2=385
$$
The square of the sum of the first ten natural numbers is ,
$$
(1+2+...+10)^2=552=3025
$$
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
$$
3025−385=2640
$$
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.



## Solution

了解平方和公式即可：

```python
#==========================================Solution
n = 100
sum_square = n * (n + 1) *(2 *n + 1) // 6
square_sum = (n * (n + 1) // 2) ** 2
print(square_sum - sum_square)
#==========================================Answer
The Answer is 25164150
```

