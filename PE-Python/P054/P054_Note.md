# Project Euler	Problem 054

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Poker hands

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

- **High Card**: Highest value card.
- **One Pair**: Two cards of the same value.
- **Two Pairs**: Two different pairs.
- **Three of a Kind**: Three cards of the same value.
- **Straight**: All cards are consecutive values.
- **Flush**: All cards of the same suit.
- **Full House**: Three of a kind and a pair.
- **Four of a Kind**: Four cards of the same value.
- **Straight Flush**: All cards are consecutive values of same suit.
- **Royal Flush**: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

<table>
    <tr align="center">
        <th>Hand</th>
        <th>Player1</th>
        <th>Player2</th>
        <th>Winner</th>
    </tr>
    <tr align="center">
        <th>1</th>
        <td>5H 5C 6S 7S KD<p>
            Pair of Fives</p>
        </td>
        <td>2C 3S 8S 8D TD<p>
            Pair of Eights</p>
        </td>
        <td>Player2</td>
    </tr>
    <tr align="center">
        <th>2</th>
        <td>5D 8C 9S JS AC<p>
            Highest card Ace</p>
        </td>
        <td>2C 5C 7D 8S QH<p>
            Highest card Queen</p>
        </td>
        <td>Player 1</td>
    </tr>
    <tr align="center">
        <th>3</th>
        <td>2D 9C AS AH AC<p>
            Three Aces</p>
        </td>
        <td>3D 6D 7D TD QD<p>
            Flush with Diamonds</p>
        </td>
        <td>Player 2</td>
    </tr>
    <tr align="center">
        <th>4</th>
        <td>4D 6S 9H QH QC<p>
            Pair of Queens</p><p>
            Highest card Nine</p>
        </td>
        <td>3D 6D 7D TD QD<p>
            Pair of Queens</p><p>
            Highest card Seven</p>
        </td>
        <td>Player 1</td>
    </tr>
    <tr align="center">
        <th>5</th>
        <td>2H 2D 4C 4D 4S<p>
            Full House</p><p>
            With Three Fours</p>
        </td>
        <td>3C 3D 3S 9S 9D<p>
            Full House</p><p>
            with Three Threes</p>
        </td>
        <td>Player 1</td>
    </tr>
</table>

The file, [poker.txt](https://projecteuler.net/project/resources/p054_poker.txt), contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?



## Solution

本题是一个大代码量的工程性编程问题，具有一定的难度（主要在于编程上），需要注意的事项如下：

- 需要将字母表示的`card value`换为数字，其中`T`表示10。
- 比较是从大往小比的，即从`Royal Flush`开始，一直比较到`High Card`，如果有相同类别的应当先比较大小，再进行下一类别的比较。
- 注意：每次双方找到相同的高类别的牌时，进行下一次比较前应当把这一类别的牌去除（即**出低类别牌前应当先把高类别的牌打出**）。这是最难实现、最易忽视的部分。

在下述实现中，我们将所有类别处理相关的方法封装在一个`Poker`静态类中。我们为每一类别引入了三种方法，分别是**单Player处理**、**双Player比较`comp`**、**同类别牌去除`deal`**，并且引入了**函数指针**，将静态方法本身`function.__func__`存入列表中循环调用并不断更新`data1`和`data2`，体现了高度复用性。另外，每个方法实现时还有很多细节可以进一步理解体会。

下面是所有代码的实现：

```python
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
#===========================================================================================================Answer
The Answer is 376
```

