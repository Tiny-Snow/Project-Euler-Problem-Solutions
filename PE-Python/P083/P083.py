# -*- coding:UTF-8 -*-
# Author：Tiny Snow
# Date: Sat, 27 Mar 2021, 22:48
# Project Euler # 083 Path sum: four ways

#====================================================================================================================Solution
#========================================================================构建一个基本的有向有权图
class Node(object):
    def __init__(self, value: int, parent_node: set, child_node: set) -> None:
        self._value = value
        self._parent_node = parent_node
        self._child_node = child_node

import os
BSER_DIR = os.path.dirname(os.path.abspath(__file__))

n = 80
data_list = []
with open(BSER_DIR + '\p083_matrix.txt', mode = 'r') as datafile:
    for _ in range(n):
        data_list.append(list(map(int, datafile.readline().split(','))))

node_matrix = [[Node(data_list[row][col], set(), set()) for col in range(n)] for row in range(n)]
for row in range(1, n - 1):
    for col in range(1, n - 1):
        node_matrix[row][col]._parent_node = set(list(node_matrix[row][col]._parent_node) + [node_matrix[row - 1][col], node_matrix[row][col - 1],
                                            node_matrix[row + 1][col], node_matrix[row][col + 1]])
        node_matrix[row][col]._child_node = set(list(node_matrix[row][col]._child_node) + [node_matrix[row - 1][col], node_matrix[row][col - 1],
                                            node_matrix[row + 1][col], node_matrix[row][col + 1]])
for row in range(1, n - 1):
    node_matrix[row][0]._parent_node = set(list(node_matrix[row][0]._parent_node) + [node_matrix[row - 1][0], node_matrix[row + 1][0], node_matrix[row][1]])
    node_matrix[row][0]._child_node = set(list(node_matrix[row][0]._child_node) + [node_matrix[row - 1][0], node_matrix[row + 1][0], node_matrix[row][1]])
    node_matrix[row][n - 1]._parent_node = set(list(node_matrix[row][n - 1]._parent_node) + [node_matrix[row - 1][n - 1], node_matrix[row + 1][n - 1], node_matrix[row][n - 2]])
    node_matrix[row][n - 1]._child_node = set(list(node_matrix[row][n - 1]._child_node) + [node_matrix[row - 1][n - 1], node_matrix[row + 1][n - 1], node_matrix[row][n - 2]])
for col in range(1, n - 1):
    node_matrix[0][col]._parent_node = set(list(node_matrix[0][col]._parent_node) + [node_matrix[0][col - 1], node_matrix[0][col + 1], node_matrix[1][col]])
    node_matrix[0][col]._child_node = set(list(node_matrix[0][col]._child_node) + [node_matrix[0][col - 1], node_matrix[0][col + 1], node_matrix[1][col]])
    node_matrix[n - 1][col]._parent_node = set(list(node_matrix[n - 1][col]._parent_node) + [node_matrix[n - 1][col - 1], node_matrix[n - 1][col + 1], node_matrix[n - 2][col]])
    node_matrix[n - 1][col]._child_node = set(list(node_matrix[n - 1][col]._child_node) + [node_matrix[n - 1][col - 1], node_matrix[n - 1][col + 1], node_matrix[n - 2][col]])
node_matrix[0][0]._parent_node = set([node_matrix[0][1], node_matrix[1][0]])
node_matrix[0][0]._child_node = set([node_matrix[0][1], node_matrix[1][0]])
node_matrix[n - 1][0]._parent_node = set([node_matrix[n - 1][1], node_matrix[n - 2][0]])
node_matrix[n - 1][0]._child_node = set([node_matrix[n - 1][1], node_matrix[n - 2][0]])
node_matrix[0][n - 1]._parent_node = set([node_matrix[0][n - 2], node_matrix[1][n - 1]])
node_matrix[0][n - 1]._child_node = set([node_matrix[0][n - 2], node_matrix[1][n - 1]])
node_matrix[n - 1][n - 1]._parent_node = set([node_matrix[n - 1][n - 2], node_matrix[n - 2][n - 1]])
node_matrix[n - 1][n - 1]._child_node = set([node_matrix[n - 1][n - 2], node_matrix[n - 2][n - 1]])

node_list = []
for row in range(n):
    for col in range(n):
        node_list.append(node_matrix[row][col])

#========================================================================开始执行Dijkstra算法
def Dijkstra(node_list: list) -> dict:
    dijkstra_dict = {}.fromkeys(node_list, float('inf'))
    defined_dict = {}
    node_num = len(node_list)

    dijkstra_dict[node_list[0]] = node_list[0]._value
    defined_dict[node_list[0]] = node_list[0]._value
    for child in node_list[0]._child_node:
        dijkstra_dict[child] = child._value + dijkstra_dict[node_list[0]]
    dijkstra_dict.pop(node_list[0])

    while len(dijkstra_dict) > 0:
        no_infinity_dict = {}
        for node in dijkstra_dict:
            if dijkstra_dict[node] != float('inf'):
                no_infinity_dict[node] = dijkstra_dict[node]
        min_value = min(no_infinity_dict.values())
        for node in no_infinity_dict:
            if no_infinity_dict[node] == min_value:
                min_node = node
        defined_dict[min_node] = dijkstra_dict[min_node]
        for child in min_node._child_node:
            if child in dijkstra_dict:
                if dijkstra_dict[child] == float('inf'):
                    dijkstra_dict[child] = defined_dict[min_node] + child._value
                else:
                    dijkstra_dict[child] = min(dijkstra_dict[child], defined_dict[min_node] + child._value)
        dijkstra_dict.pop(min_node)

    return defined_dict

defined_dict = Dijkstra(node_list)
print(defined_dict[node_list[-1]])