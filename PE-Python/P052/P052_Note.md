# Project Euler	Problem 052

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Permuted multiples

It can be seen that the number, $125874$, and its double, $251748$, contain exactly the same digits, but in a different order.

Find the smallest positive integer, $x$, such that $2x, 3x, 4x, 5x$, and $6x$, contain the same digits.



## Solution

比较基础，实现如下：

```python
#================================================================Solution
def is_positive(n):
    for m in range(2, 7):
        if sorted(str(n)) != sorted(str(m * n)):
            return False
    return True

def find_ans():
    k = 0
    while True:
        for x in range(int(10 ** (k - 1)), int((10 ** k) / 6)):
            if is_positive(x) == True:
                return x
        k += 1

print(find_ans())
#================================================================Answer
The Answer is 142857
```

