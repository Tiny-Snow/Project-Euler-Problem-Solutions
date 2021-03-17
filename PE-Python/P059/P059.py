# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Fri, 26 Feb 2021, 23:26
# Project Euler # 059 XOR decryption

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