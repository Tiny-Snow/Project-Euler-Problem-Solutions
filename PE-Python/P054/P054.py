# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Wed, 24 Feb 2021, 22:07
# Project Euler # 054 Poker hands

#===========================================================================================================Solution
#===============================================================================储存数据
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(BASE_DIR + '\\p054_poker.txt', mode='r') as datafile:
    data = datafile.readlines()
data1 = ['' for i in range(len(data))]
data2 = ['' for i in range(len(data))]
for i in range(len(data)):
    split_data = data[i].partition('\n')[0].split()
    data1[i] = split_data[0:5]
    data2[i] = split_data[5:10]

#===============================================================================class Poker
class Poker(object):

    proker = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    @staticmethod
    def transfer(char: str) -> int:
        '''用于card value的转换'''
        if char == 'T':
            return 10 
        if char == 'J':
            return 11
        if char == 'Q':
            return 12
        if char == 'K':
            return 13
        if char == 'A':
            return 14
        return int(char)

    #====================================================high card
    @staticmethod
    def high_card(data: list) -> list:
        '''返回card value的有序列表'''
        if len(data) == 0:
            return []
        value_list = []
        for i in range(len(data)):
            value_list.append(Poker.transfer(data[i][0]))
        return list(sorted(value_list))
    
    @staticmethod
    def comp_high_card(data1: list, data2: list) -> int:
        '''比较high card'''
        data1_value = Poker.high_card(data1)
        data2_value = Poker.high_card(data2)
        if len(data1_value) == 0:
            return 0
        for i in reversed(range(len(data1))):
            if data1_value[i] > data2_value[i]:
                return 1
            if data1_value[i] < data2_value[i]:
                return 2
        return 3


    #====================================================one pair
    @staticmethod
    def one_pair(data: list) -> int:
        '''返回最大的one pair，没有则返回0'''
        if len(data) < 2:
            return -1
        max_pair = 0
        for i in range(len(data) - 1):
            for j in range(i + 1, len(data)):
                if Poker.transfer(data[i][0]) == Poker.transfer(data[j][0]):
                    max_pair = max(Poker.transfer(data[i][0]), max_pair)
        return max_pair

    @staticmethod
    def comp_one_pair(data1: list, data2: list) -> int:
        '''比较one pair'''
        data1_one_pair = Poker.one_pair(data1)
        data2_one_pair = Poker.one_pair(data2)
        if data1_one_pair > data2_one_pair:
            return 1
        if data1_one_pair < data2_one_pair:
            return 2
        if data1_one_pair == data2_one_pair == 0:
            return 0
        if data1_one_pair == data2_one_pair == -1:
            return -1
        return 3

    @staticmethod
    def deal_one_pair(data1: list, data2: list) -> tuple:
        '''处理找到one pair之后的data'''
        data1_value = [Poker.transfer(data1[i][0]) for i in range(len(data1))]
        data2_value = [Poker.transfer(data2[i][0]) for i in range(len(data2))]
        max_pair = Poker.one_pair(data1)
        index_list1 = index_list2 = []
        for i in range(len(data1_value)):
            if data1_value[i] == max_pair:
                index_list1.append(i)
            if data2_value[i] == max_pair:
                index_list2.append(i)
        data1.pop(index_list1[0])
        data1.pop(index_list1[1] - 1)
        data2.pop(index_list2[0])
        data2.pop(index_list2[1] - 1)
        return (data1, data2)


    #====================================================two pair
    @staticmethod
    def two_pair(data: list) -> list:
        '''返回可能的two pair，没有则返回空列表'''
        if len(data) < 4:
            return -1
        two_pair = []
        for i in range(len(data) - 1):
            for j in range(i + 1, len(data)):
                if Poker.transfer(data[i][0]) == Poker.transfer(data[j][0]):
                    two_pair.append(Poker.transfer(data[i][0]))
        two_pair = list(set(two_pair))
        if len(two_pair) == 2:
            return list(sorted(two_pair))
        return []
    
    @staticmethod
    def comp_two_pair(data1: list, data2: list) -> int:
        '''比较two pair'''
        data1_two_pair = Poker.two_pair(data1)
        data2_two_pair = Poker.two_pair(data2)
        if data1_two_pair == []:
            max1_1 = max1_2 = 0
        elif data1_two_pair == -1:
            max1_1 = max1_2 = -1
        else:
            max1_1 = data1_two_pair[1]
            max1_2 = data1_two_pair[0]
        if data2_two_pair == []:
            max2_1 = max2_2 = 0
        elif data2_two_pair == -1:
            max2_1 = max2_2 = -1
        else:
            max2_1 = data2_two_pair[1]
            max2_2 = data2_two_pair[0]
        if max1_1 > max2_1:
            return 1
        if max1_1 < max2_1:
            return 2
        if max1_2 > max2_2:
            return 1
        if max1_2 < max2_2:
            return 2
        if max1_1 == max1_2 == max2_1 == max2_2 == 0:
            return 0
        if max1_1 == max1_2 == max2_1 == max2_2 == -1:
            return -1
        return 3

    @staticmethod
    def deal_two_pair(data1: list, data2: list) -> tuple:
        '''处理找到two pair之后的data'''
        data1_value = [Poker.transfer(data1[i][0]) for i in range(len(data1))]
        data2_value = [Poker.transfer(data2[i][0]) for i in range(len(data2))]
        max_two_pair = Poker.two_pair(data1, data2)
        for i in range(len(data1_value)):
            if data1_value[i] not in max_two_pair:
                index1 = i
            if data2_value[i] not in max_two_pair:
                index2 = i
        data1 = [data1[index1]]
        data2 = [data2[index2]]
        return (data1, data2)

    
    #====================================================three of a Kind
    @staticmethod
    def three_of_a_Kind(data: list) -> int:
        '''返回可能的three of a Kind，没有则返回0'''
        if len(data) < 3:
            return -1
        three = 0
        value_list = Poker.high_card(data)
        for i in range(len(data) - 2):
            if value_list[i] == value_list[i + 1] == value_list[i + 2]:
                three = value_list[i]
        return three

    @staticmethod
    def comp_three_of_a_Kind(data1: list, data2: list) -> int:
        '''比较three of a Kind'''
        data1_three_of_a_Kind = Poker.three_of_a_Kind(data1)
        data2_three_of_a_Kind = Poker.three_of_a_Kind(data2)
        if data1_three_of_a_Kind > data2_three_of_a_Kind:
            return 1
        if data1_three_of_a_Kind < data2_three_of_a_Kind:
            return 2
        if data1_three_of_a_Kind == data2_three_of_a_Kind == 0:
            return 0
        if data1_three_of_a_Kind == data2_three_of_a_Kind == -1:
            return -1
        return 3

    @staticmethod
    def deal_three_of_a_Kind(data1: list, data2: list) -> tuple:
        '''处理找到three of a Kind之后的data'''
        data1_value = [Poker.transfer(data1[i][0]) for i in range(len(data1))]
        data2_value = [Poker.transfer(data2[i][0]) for i in range(len(data2))]
        three = Poker.three_of_a_Kind(data1, data2)
        index_list1 = index_list2 = []
        for i in range(len(data1_value)):
            if data1_value[i] != three:
                index_list1.append(i)
            if data2_value[i] != three:
                index_list2.append(i)
        data1 = [data1[index_list1[0]], data1[index_list1[1]]]
        data2 = [data2[index_list2[0]], data2[index_list2[1]]]
        return (data1, data2)


    #====================================================straight
    @staticmethod
    def straight(data: list) -> int:
        '''如果连续返回最小的card value，否则返回0'''
        if len(data) != 5:
            return -1
        value_list = Poker.high_card(data)
        for i in range(len(data) - 1):
            if value_list[i] + 1 != value_list[i + 1]:
                return 0
        return value_list[0]

    @staticmethod
    def comp_straight(data1: list, data2: list) -> int:
        '''比较straight'''
        data1_straight = Poker.straight(data1)
        data2_straight = Poker.straight(data2)
        if data1_straight > data2_straight:
            return 1
        if data1_straight < data2_straight:
            return 2
        if data1_straight == data2_straight == 0:
            return 0
        if data1_straight == data2_straight == -1:
            return -1
        return 3

    @staticmethod
    def deal_straight(data1: list, data2: list) -> tuple:
        '''处理找到straight之后的data'''
        return ([], [])


    #====================================================flush
    @staticmethod
    def flush(data: list) -> list:
        '''如果所有卡的suit都相同，返回排序好的value列表，否则返回空列表'''
        if len(data) != 5:
            return -1
        value_list = []
        for i in range(4):
            if data[i][1] != data[i + 1][1]:
                return value_list
        value_list = Poker.high_card(data)
        return value_list

    @staticmethod
    def comp_flush(data1: list, data2: list) -> int:
        '''比较flush'''
        data1_flush = Poker.flush(data1)
        data2_flush = Poker.flush(data2)
        if data1_flush == data2_flush == -1:
            return -1
        if data1_flush == [] and data2_flush == []:
            return 0
        if data1_flush == [] and data2_flush != []:
            return 2 
        if data1_flush != [] and data2_flush == []:
            return 1 
        for i in reversed(range(5)):
            if data1_flush[i] > data2_flush[i]:
                return 1
            if data1_flush[i] < data2_flush[i]:
                return 2
        return 3

    @staticmethod
    def deal_flush(data1: list, data2: list) -> tuple:
        '''处理找到flush之后的data'''
        return ([], [])


    #====================================================full house
    @staticmethod
    def full_house(data: list) -> list:
        '''如果存在three of a Kind和one pair，返回[three, pair]，否则返回空列表'''
        if len(data) != 5:
            return -1
        ans = []
        value_list = Poker.high_card(data)
        three = Poker.three_of_a_Kind(data)
        if three == 0:
            return ans
        for _ in range(3):
            value_list.remove(three)
        if value_list[0] == value_list[1]:
            ans = [three, value_list[0]]
            return ans
        return ans
    
    @staticmethod
    def comp_full_house(data1: list, data2: list) -> int:
        '''比较full house'''
        data1_full_house = Poker.full_house(data1)
        data2_full_house = Poker.full_house(data2)
        if data1_full_house == []:
            three1 = pair1 = 0
        elif data1_full_house == -1:
            three1 = pair1 = -1
        else:
            three1 = data1_full_house[0]
            pair1 = data1_full_house[1]
        if data2_full_house == []:
            three2 = pair2 = 0
        elif data2_full_house == -1:
            three2 = pair2 = -1
        else:
            three2 = data2_full_house[0]
            pair2 = data2_full_house[1]
        if three1 > three2:
            return 1
        if three1 < three2:
            return 2
        if pair1 > pair2:
            return 1
        if pair1 < pair2:
            return 2
        if three1 == three2 == pair1 == pair2 == 0:
            return 0
        if three1 == three2 == pair1 == pair2 == -1:
            return -1
        return 3

    @staticmethod
    def deal_full_house(data1: list, data2: list) -> tuple:
        '''处理找到full house之后的data'''
        return ([], [])


    #====================================================four of a Kind
    @staticmethod
    def four_of_a_kind(data: list) -> int:
        '''返回可能的four of a Kind，没有则返回0'''
        if len(data) < 4:
            return -1
        four = 0
        value_list = Poker.high_card(data)
        for i in range(2):
            if Poker.transfer(data[i][0]) == Poker.transfer(data[i + 1][0]) == Poker.transfer(data[i + 2][0]) == Poker.transfer(data[i + 3][0]):
                four = data[i][0]
        return four
    
    @staticmethod
    def comp_four_of_a_kind(data1: list, data2: list) -> int:
        '''比较four of a Kind'''
        data1_four_of_a_kind = Poker.four_of_a_kind(data1)
        data2_four_of_a_kind = Poker.four_of_a_kind(data2)
        if data1_four_of_a_kind > data2_four_of_a_kind:
            return 1
        if data1_four_of_a_kind < data2_four_of_a_kind:
            return 2
        if data1_four_of_a_kind == data2_four_of_a_kind == 0:
            return 0
        if data1_four_of_a_kind == data2_four_of_a_kind == -1:
            return -1
        return 3

    @staticmethod
    def deal_four_of_a_kind(data1: list, data2: list) -> tuple:
        '''处理找到four of a Kind之后的data'''
        data1_value = [Poker.transfer(data1[i][0]) for i in range(len(data1))]
        data2_value = [Poker.transfer(data2[i][0]) for i in range(len(data2))]
        four = Poker.four_of_a_kind(data1, data2)
        for i in range(len(data1_value)):
            if data1_value[i] != four:
                index1 = i
            if data2_value[i] != four:
                index2 = i
        data1 = [data1[index1]]
        data2 = [data2[index2]]
        return (data1, data2)


    #====================================================straight flush
    @staticmethod
    def straight_flush(data: list) -> int:
        '''如果满足straight flush，返回最小的value，否则返回0'''
        if len(data) != 5:
            return -1
        value_list = Poker.flush(data)
        if value_list == []:
            return 0
        for i in range(len(data) - 1):
            if value_list[i] + 1 != value_list[i + 1]:
                return 0
        return value_list[0]

    @staticmethod
    def comp_straight_flush(data1: list, data2: list) -> int:
        '''比较straight flush'''
        data1_straight_flush = Poker.straight_flush(data1)
        data2_straight_flush = Poker.straight_flush(data2)
        if data1_straight_flush > data2_straight_flush:
            return 1
        if data1_straight_flush < data2_straight_flush:
            return 2
        if data1_straight_flush == data2_straight_flush == 0:
            return 0
        if data1_straight_flush == data2_straight_flush == -1:
            return -1
        return 3

    @staticmethod
    def deal_straight_flush(data1: list, data2: list) -> tuple:
        '''处理找到straight flush之后的data'''
        return ([], [])


    #====================================================royal flush
    @staticmethod
    def royal_flush(data: list) -> int:
        '''如果满足royal flush，返回1，否则返回0'''
        if len(data) != 5:
            return -1
        if Poker.straight_flush(data) == 10:
            return 1
        return 0

    @staticmethod
    def comp_royal_flush(data1: list, data2: list) -> int:
        '''比较royal flush'''
        data1_royal_flush = Poker.royal_flush(data1)
        data2_royal_flush = Poker.royal_flush(data2)
        if data1_royal_flush > data2_royal_flush:
            return 1
        if data1_royal_flush < data2_royal_flush:
            return 2
        if data1_royal_flush == data2_royal_flush == 0:
            return 0
        if data1_royal_flush == data2_royal_flush == -1:
            return -1
        return 3

    @staticmethod
    def deal_royal_flush(data1: list, data2: list) -> tuple:
        '''处理找到royal flush之后的data'''
        return ([], [])


    #====================================================compare
    comp = [comp_high_card.__func__, comp_one_pair.__func__, comp_two_pair.__func__, comp_three_of_a_Kind.__func__, 
                comp_straight.__func__, comp_flush.__func__, comp_full_house.__func__, comp_four_of_a_kind.__func__, 
                comp_straight_flush.__func__, comp_royal_flush.__func__]
    deal = [None, deal_one_pair.__func__, deal_two_pair.__func__, deal_three_of_a_Kind.__func__, 
                deal_straight.__func__, deal_flush.__func__, deal_full_house.__func__, deal_four_of_a_kind.__func__, 
                deal_straight_flush.__func__, deal_royal_flush.__func__]


    @staticmethod
    def compare(data1: list, data2: list) -> int:
        '''逐一比较Player1和Player2，返回获胜的一方（1或2）'''
        for i in reversed(range(len(Poker.comp))):
            if i == 0:
                return Poker.comp[i](data1, data2)
            ans = Poker.comp[i](data1, data2)
            if ans == -1 or ans == 0:
                continue
            if ans == 3:
                data1, data2 = Poker.deal[i](data1, data2)
            if ans == 1 or ans == 2:
                return ans



if __name__ == '__main__':
    win1 = 0
    for i in range(len(data)):
        if Poker.compare(data1[i], data2[i]) == 1:
            win1 += 1
    print(win1)