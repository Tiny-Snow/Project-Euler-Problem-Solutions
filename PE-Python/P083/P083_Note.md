# Project Euler	Problem 083

<p align="right"><i>Tiny Snow</i></p>



## Problem

### Path sum: four ways

NOTE: This problem is a significantly more challenging version of [Problem 81](https://projecteuler.net/problem=81).

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.
$$
\begin{pmatrix}
\color{red}{131} & 673 & \color{red}{234} & \color{red}{103} & \color{red}{18}\\
\color{red}{201} & \color{red}{96} & \color{red}{342} & 965 & \color{red}{150}\\
630 & 803 & 746 & \color{red}{422} & \color{red}{111}\\
537 & 699 & 497 & \color{red}{121} & 956\\
805 & 732 & 524 & \color{red}{37} & \color{red}{331}
\end{pmatrix}
$$
Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in [matrix.txt](https://projecteuler.net/project/resources/p083_matrix.txt) (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.



## Solution

注意到，实际上本问题已经是可以任意移动的图论问题了。因此，欲解决本问题，我们需要利用常见的图算法—— **迪杰斯特拉算法（*Dijkstra's algorithm*）**。

迪杰斯特拉算法适用于**在有向非负权图中寻找两点间的最短路径**。事实上，该算法能够找到**以某一点为源点到达图中任意一点的最短路径**。迪杰斯特拉算法是最基本的图论算法之一。

迪杰斯特拉算法的核心如下：

- 首先，我们将图中的所有顶点分为两部分 $S$ 和 $E-S$ 。其中，$E$ 为所有顶点的集合， $S$ 为已经确定了源点到该点的最短路径点的集合。初始化时，将所有点到源点距离设为 $\infin$ ， $S$ 设为空。

- 之后，我们将源点 $v_0$ 加入 $S$ 中，源点到源点的距离为 $0$ 。对于源点的邻接顶点，设其到源点的边长为 $l_{v_1-v_0}$， $l_{v_2-v_0}$，$\cdots$， $l_{v_{k_0}-v_0}$，更新他们到源点的距离为 $d_{v_1} = l_{v_1-v_0}$，$\cdots$，$d_{v_{k_0}} = l_{v_{k_0}-v_0}$ 。

- 初始化完成后，我们来持续更新各点的 $d$ 值：首先从 $E-S$ 中找到现有最小 $d$ 值的点（设为 $v_1'$），将 $v_1'$ 加入 $S$ 中。对于 $E-S$ 中所有 $v_1'$ 的邻接顶点 $v$ ，更新其 $d$ 值：如果 $d_v = \infin$，取 $d_v = d_{v_1'} + l_{v-{v_1'}}$ ；若 $d_v$ 已被更新过，更新 $d_v = min\{d_v,d_{v_1'} + l_{v-{v_1'}}\}$。简单来说，此过程就是一个探路的过程：对于一个之前已经探明了一条路径的顶点 $v$ ，如果发现了一个确定顶点 $v_1'$ 也能够到达 $v$ ，只需要考虑通过 $v_1'$ 的新路径是否更短即可。

- 持续上述的更新过程，直到所有点的 $d$ 值都被确定。至此，我们得到了所有点到达源点的最短路径。

现在，我们来考虑**迪杰斯特拉算法的正确性**：即考虑每次寻找的 $v_1'$ 是否就是 $E-S$ 中距离源点距离最小的点、且距离恰好为 $d_{v_1'}$ 呢？根据归纳假设，我们首先能够明确的是： $d_{v_1'}$ 确是源点通过 $S$ 中的顶点到达 $v_1'$ 的最短路径。这是因为对于每个与 $v_1'$ 邻接的 $S$ 中的顶点，我们都对 $d_{v_1'}$ 进行了更新，而 $S$ 中顶点的 $d$ 值一定是确定的（即使之后有 $E-S$ 中的顶点与之相连，但注意到加入 $S$ 的 $d$ 值是从小到大的），因此该结论没有问题。那么，可能存在通过 $E-S$ 点到达 $v_1'$ 的路径吗？显然，该 $E-S$ 内的点就会有更小的 $d$ 值，与 $v_1'$ 的选取矛盾！因此，迪杰斯特拉算法的正确性得证。

迪杰斯特拉算法的过程已经介绍完整了，但我们还是希望能够简化该算法的思想：实际上，该算法就是不断地确定顶点的 $d$ 值，并根据该 $d$ 值对该顶点的子顶点的距离进行更新。最终，所有点都会被确定，而所有点都根据其父顶点的距离进行了更新，因此保证了算法的正确性。

更多关于该算法的信息可参见：[迪杰斯特拉算法（Dijkstra's algorithm）](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)。

迪杰斯特拉算法的伪码如下：

```
function Dijkstra(Graph, source):

    create vertex set Q

    for each vertex v in Graph:            
        dist[v] ← INFINITY                 
        prev[v] ← UNDEFINED                
        add v to Q                     
    dist[source] ← 0                       
    
    while Q is not empty:
        u ← vertex in Q with min dist[u]   
                                            
        remove u from Q
        
        for each neighbor v of u:           // only v that are still in Q
            alt ← dist[u] + length(u, v)
            if alt < dist[v]:              
                dist[v] ← alt
                prev[v] ← u

    return dist[], prev[]
```



回到本题，现在本题就看起来十分简单了——只需要将矩阵转化为一个有向图即可。实现如下：

```python
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
#====================================================================================================================Answer
The Answer is 425185
```



