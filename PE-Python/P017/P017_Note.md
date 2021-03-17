# Project Euler	Problem 017

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Number letter counts

If the numbers $1$ to $5$ are written out in words: one, two, three, four, five, then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.

If all the numbers from $1$ to $1000$ (one thousand) inclusive were written out in words, how many letters would be used?



**NOTE:** Do not count spaces or hyphens. For example, $342$ (three hundred and forty-two) contains $23$ letters and $115$ (one hundred and fifteen) contains $20$ letters. The use of "and" when writing out numbers is in compliance with British usage.



## Solution

本题本质上是写一个用于**数字英文翻译器**的**专家系统**。

下面是这个专家系统的一个较成熟的实现，鉴于翻译规则，之后追加位数的方法都是相同的。

```python
#==========================================================================================================================Solution
# 个位数字列表
letter_list_1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# [10,20)数字列表
letter_list_2 = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
# 十位数字列表
letter_list_3 = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
# 百位、千位数字列表
letter_list_4 = ['hundred']
letter_list_5 = ['thousand']
def num_to_letter(n):
    '''该数字-字母函数转换限于[0,10000)以内的数，不含空格和连字符'''
    sumlen = len(str(n))
    # [0,10)
    if sumlen == 1:
        return letter_list_1[n]
    if sumlen == 2:
        # 整十的倍数（注意个位的0）
        if n % 10 == 0:
            return letter_list_3[int(str(n)[0])]
        # (10,20)
        elif n < 20:
            return letter_list_2[int(str(n)[1])]
        # [20,100)内其他的数
        else:
            return letter_list_3[int(str(n)[0])] + letter_list_1[int(str(n)[1])]
    # [100,1000)
    if sumlen == 3:
        # 整百倍数
        if n % 100 == 0:
            return letter_list_1[int(str(n)[0])] + letter_list_4[0]
        else:
            return letter_list_1[int(str(n)[0])] + letter_list_4[0] + 'and' + num_to_letter(n % 100)
    # [1000,10000)
    if sumlen == 4:
        # 整千倍数
        if n % 1000 == 0:
            return letter_list_1[int(str(n)[0])] + letter_list_5[0]
        else:
            return letter_list_1[int(str(n)[0])] + letter_list_5[0] + num_to_letter(n % 1000)
letter_sum = 0
for i in range(1, 1001):
    letter_sum += len(num_to_letter(i))
print(letter_sum)
#==========================================================================================================================Answer
The Answer is 21124
```

当然，就这个题目而言，目的只是计数。如果要优化的话，只需要统计前99个数即可。