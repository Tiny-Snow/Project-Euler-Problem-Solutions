# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 20 Feb 2021, 15:00
# A Utility Class for Prime Analysis

class Prime(object):
    '''class Prime用于进行素数相关的问题分析。
    目前class Prime的主要功能有：
      - 遍历连续区间的所有素数
      - 对连续区间的所有合数进行质因数分解，获得每个数的所有因数
      - 计算常见的数论函数：
         -- 素数个数函数
         -- 欧拉函数
         -- 素因数个数函数
         -- 因子个数函数
         -- 因数和函数
         -- 除数函数
         -- 莫比乌斯函数
    '''


    def __init__(self, limit: int) -> None:
        '''limit为素数处理的区间上限'''
        if not (type(limit) == int and limit > 1):
            raise TypeError('The input parameter must be an integer greater than 1.')
        
        self.__limit = limit

        self.__prime = []                                               # __prime储存区间内所有的素数

        self.__number = [1 for i in range(self.__limit + 1)]            # __number储存区间内所有数的素数信息，1为素数，0为非素数
        self.__number[0] = self.__number[1] = 0

        self.__l_prime_factor = [1 for i in range(self.__limit + 1)]    # __l_prime_factor储存区间内所有合数的最小质因数，非合数默认为1
        self.__l_prime_factor[0] = 0

        self.__prime_factor = [{} for i in range(self.__limit + 1)]     # __prime_factor储存所有数的质因数及其幂次，以键值对 质因数:幂次 储存
        
        self.__factor = [[1] for i in range(self.__limit + 1)]          # __factor按从小到大的顺序储存所有数的所有因数
        self.__factor[0] = [0]


    def _traverse(self) -> None:
        '''遍历区间内所有的素数，储存区间内所有数的素数信息，并记录所有数的最小质因数，该函数在初始化时调用'''
        for p in range(1, self.__limit + 1):
            if self.__number[p] == 1:
                self.__prime.append(p)
            for j in range(len(self.__prime)):
                if p * self.__prime[j] > self.__limit:
                    break
                self.__number[p * self.__prime[j]] = 0
                self.__l_prime_factor[p * self.__prime[j]] = self.__prime[j]
                if p % self.__prime[j] == 0:
                    break

    def _find_factor(self) -> None:
        '''获取区间内所有数的所有质因数及其幂次、所有因数，该函数在初始化时调用'''
        for n in range(2, self.__limit + 1):
            if self.__number[n] == 1:                # 素数情况
                self.__prime_factor[n][n] = 1
                self.__factor[n].append(n)
            else:                               # 合数情况
                min_p = self.__l_prime_factor[n]
                self.__prime_factor[n][min_p] = 1
                for prime in self.__prime_factor[n // min_p].keys():
                    if prime == min_p:
                        self.__prime_factor[n][min_p] += self.__prime_factor[n // min_p][min_p]
                    else:
                        self.__prime_factor[n][prime] = self.__prime_factor[n // min_p][prime]
                self.__factor[n] += self.__factor[n // min_p]
                for origin in self.__factor[n // min_p]:
                    self.__factor[n].append(min_p * origin)
            self.__factor[n] = list(sorted(list(set(self.__factor[n]))))      # 去重、排序

    
    def _get_prime_list(self) -> list:
        '''返回素数列表__prime'''
        return self.__prime
    
    def _get_number_list(self) -> list:
        '''返回素数信息列表__number'''
        return self.__number

    def _get_l_prime_factor_list(self) -> list:
        '''返回合数最小质因数列表__l_prime_factor'''
        return self.__l_prime_factor
    
    def _get_prime_factor_list(self) -> list:
        '''返回 质因数:幂次 列表__prime_factor'''
        return self.__prime_factor

    def _get_factor_list(self) -> list:
        '''返回因数列表__factor'''
        return self.__factor

    def _is_prime(self, p: int) -> bool:
        '''判断p是否是区间内的素数，返回一个bool值'''
        if not (type(p) == int and p > 0 and p <= self.__limit):
            return False
        if self.__number[p] == 1:
            return True
        return False
    
    def _get_prime_index(self, p: int) -> int:
        '''返回p在素数列表中的位置，即第几个素数，非素数返回None'''
        if self._is_prime(p) == True:
            return self.__prime.index(p) + 1
        return None

    def _prime_number(self, n: int) -> int:
        '''计算素数个数函数，返回区间内所有素数的个数'''
        if not (type(n) == int and n > 0 and n <= self.__limit):
            raise TypeError('The input parameter must be in the specified interval.')
        num = 0
        for p in range(1, n):
            if self.__number[p] == 1:
                num += 1
        return num

    def _euler_func(self, n: int) -> int:
        '''计算欧拉函数，返回小于或等于n的正整数中与n互质的数的数目'''
        if not (type(n) == int and n > 0 and n <= self.__limit):
            raise TypeError('The input parameter must be in the specified interval.')
        product = n
        for p in self.__prime_factor[n].keys():
            product *= (1 - 1 / p)
        return int(product)
    
    def _omega_func(self, n: int) -> int:
        '''计算素因子个数函数，返回n的素因子个数'''
        if not (type(n) == int and n > 0 and n <= self.__limit):
            raise TypeError('The input parameter must be in the specified interval.')
        return len(self.__prime_factor[n])

    def _factor_num(self, n: int) -> int:
        '''计算因子个数函数，返回n的因子个数'''
        if not (type(n) == int and n > 0 and n <= self.__limit):
            raise TypeError('The input parameter must be in the specified interval.')
        return len(self.__factor[n])

    def _sigma_factor(self, n: int) -> int:
        '''计算因数和函数，返回n的所有因数和'''
        if not (type(n) == int and n > 0 and n <= self.__limit):
            raise TypeError('The input parameter must be in the specified interval.')
        return sum(self.__factor[n])

    def _divisor_func(self, n: int, k: int) -> float:
        '''计算除数函数，返回各因子的k次方和。
           k = 0时，等价于因子个数函数；
           k = 1时，等价于因子和函数。
        '''
        if not (type(n) == int and n > 0 and n <= self.__limit):
            raise TypeError('The input parameter must be in the specified interval.')
        sum = 0
        for d in self.__factor[n]:
            sum += d ** k
        return sum

    def _mobius_func(self, n: int) -> int:
        '''计算莫比乌斯函数'''
        if not (type(n) == int and n > 0 and n <= self.__limit):
            raise TypeError('The input parameter must be in the specified interval.')
        if n == 1:
            return 1
        if 2 ** len(self.__prime_factor[n]) == self._factor_num(n):
            return (-1) ** len(self.__prime_factor[n])
        return 0
