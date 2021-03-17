# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Mon, 22 Feb 2021, 10:45
# Project Euler # 042 Coded triangle numbers

#=================================================================Solution
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(BASE_DIR + '/p042_words.txt', mode = 'r') as datafile:
    data_str = datafile.read()
    data = list(data_str.split(','))

def word_score(word):
    score = 0
    for char in word:
        score += ord(char) - 64
    return score

triangle_words = 0

for i in range(len(data)):
    data[i] = word_score(data[i][1:-1])
    n = int((2 * data[i]) ** 0.5)
    if n * (n + 1) == 2 * data[i]:
        triangle_words += 1
print(triangle_words)