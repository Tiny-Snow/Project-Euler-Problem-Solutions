# Project Euler	Problem 059

<p align="right"><i>Tiny Snow</i></p>



## Problem

### XOR decryption

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using [p059_cipher.txt](https://projecteuler.net/project/resources/p059_cipher.txt) (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.



## Solution

本题牵涉到基础的密码学，使用了最基础的**XOR加密**，即**异或加密算法**。

所谓异或运算，就是指二进制下的每位数字，**相同取0，不同取1**。异或加密十分好理解，对于原文字符 $c$ 和解密字符 $k$ ，取异或运算 $c\oplus k$ ，结果即作为加密后的字符。显然，如果要求密码难以破解，应当任意生成一个与原文长度相同的密钥。但是，实际情况下多使用少量的几个字符作为密钥，对原文进行循环的异或加密。

异或运算有以下重要的**性质**：

- **归零律**：$a \oplus a = 0$
- **恒等律**：$a \oplus 0 = a$
- **交换律**：$a \oplus b = b \oplus a$
- **结合律**：$a \oplus b \oplus c = a \oplus (b \oplus c) = (a \oplus b) \oplus c$
- **自反性**：$a \oplus b \oplus a = b$

由上述性质，我们可以得到下述的**异或解密原理**：
$$
d = a \oplus b \oplus c \oplus ··· \Rightarrow d \oplus b \oplus c \oplus ···  = a
$$
也就是说，**对于异或加密后的文本，我们再进行一次异或加密后就可以得到原文（并且不用考虑异或加密的顺序）**。

那么，解密最关键的问题就归结为：如何判断一个文本是不是原文？

我们给出一种思路：计算文章中出现的英文字母、数字和标点符号的数目，越多说明越有可能是原文。

实现如下：

```python
#===================================================================Solution
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(BASE_DIR + '\\p059_cipher.txt', mode='r') as datafile:
    data = datafile.read().split(',')

def XOR_3(data: list, key1: str, key2: str, key3: str) -> list:
    new_data = ['' for _ in range(len(data))]
    for i in range(0, len(data), 3):
        new_data[i] = str(int(data[i]) ^ ord(key1))
        new_data[i + 1] = str(int(data[i + 1]) ^ ord(key2))
        new_data[i + 2] = str(int(data[i + 2]) ^ ord(key3))
    return new_data

# 计算文章中出现的英文字母、数字和标点符号的数目，越多说明越有可能是原文
def sum_text(data: list) -> int:
    text_sum = 0
    for c in data:
        if int(c) >= ord('A') and int(c) <= ord('z'):
            text_sum += 1
        if int(c) >= ord('0') and int(c) <= ord('9'):
            text_sum += 1
        if int(c) == ord(' ') or int(c) == ',' or int(c) == '.':
            text_sum += 1
    return text_sum


max_text_sum = 0
for key1 in range(ord('e'), ord('e') + 1):
    for key2 in range(ord('a'), ord('z') + 1):
        for key3 in range(ord('a'), ord('z') + 1):
            new_data = XOR_3(data, chr(key1), chr(key2), chr(key3))
            text_sum = sum_text(new_data)
            if text_sum > max_text_sum:
                real_data = new_data
                max_text_sum = text_sum

ascii_sum = 0
for i in real_data:
    ascii_sum += int(i)
print(ascii_sum)
#===================================================================Answer
The Answer is 129448
```

事实上，上述算法还可以进一步优化：由于循环加密中，不同密钥间互不相干，因此可以逐个确定密钥，而无需使用三重循环遍历。