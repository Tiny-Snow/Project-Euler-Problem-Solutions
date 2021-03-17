# Project Euler	Problem 048

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Self powers

The series, $1^1 + 2^2 + 3^3 + ... + 10^{10} = 10405071317$.

Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + ... + 1000^{1000}$.



## Solution

并没有能够实际意义上减小计算量的数论方法（取一些同余后计算量几乎一样，应用欧拉定理 $\varphi(10^{10}) = 4 \times10^9$ 又太大了）。直接遍历即可：

```python
#===================================Solution
sum = 0
for k in range(1,1000 + 1):
    sum  = (sum + k ** k) % 10 ** 10
print(sum)
#===================================Answer
The Answer is 9110846700
```

