# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 30 Jan 2021, 14:10
# Project Euler # 015 Lattice paths

#=====================================Solution
from scipy.special import *
def Lattice_paths(n):
    return int(2 * comb(2 * n - 1, n))
print(Lattice_paths(20))