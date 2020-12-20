# coding: UTF-8
# 图的实现比较多样化， 邻接表、邻接矩阵


# 邻接表实现
class UndirectedGraphAdjacencyList:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def insert(self, a, b):  # a 与 b 之间存在边相连
        if not (a in self.nodes):
            self.nodes.append(a)
            self.edges[a] = list()

        if not (b in self.nodes):
            self.nodes.append(b)
            self.edges[b] = list()

        self.edges[a].append(b)
        self.edges[b].append(a)

    def get_nodes(self, node):
        return self.edges[node]

    def show_nodes(self):
        return self.nodes

    def show_edges(self):
        return self.edges


class UndirectedGraphAdjacencyMatrix:
    def __init__(self, size):
        self.size = size
        self.graph = [[0] * size for _ in range(size)]

    def insert(self, a, b):  # 点的序号要求按照整数顺序记
        # 仅插入一条边的情况
        # 点、边都要插入的情况
        if a <= self.size and b <= self.size:
            self.graph[a - 1][b - 1] = 1
            self.graph[b - 1][a - 1] = 1
        elif a > self.size or b > self.size:
            for _ in range(self.size):
                self.graph[_].append(0)
            self.size += 1
            self.graph.append([0] * self.size)
            # print(self.graph)
            self.graph[a - 1][b - 1] = 1
            self.graph[b - 1][a - 1] = 1

    def get_nodes(self, node):
        result = list()
        for i in range(self.size):
            if self.graph[node][i] == 1:
                result.append(i)
        return result

    def show(self):
        for i in self.graph:
            for j in i:
                print(j, end=" ")
            print(" ")


def main1():
    graph = UndirectedGraphAdjacencyList()
    graph.insert('0', '1')
    graph.insert('0', '2')
    graph.insert('0', '3')
    graph.insert('1', '3')
    graph.insert('2', '3')
    print(graph.show_nodes())
    print(graph.show_edges())
    print(graph.get_nodes('0'))


def main2():
    graph = UndirectedGraphAdjacencyMatrix(5)
    graph.insert(1, 4)
    graph.insert(4, 2)
    graph.insert(4, 5)
    graph.insert(2, 5)
    graph.insert(5, 3)
    graph.insert(6, 3)
    graph.show()


def dfs(graph, initial, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    result.append(initial)
    visited.add(initial)
    for u in graph[initial]:
        if u in visited:
            continue
        visited.add(u)
        dfs(graph, u, visited, result)
    return result


def bfs(graph, initial):
    visited = []
    queue = [initial]
    visited.append(initial)
    while queue:
        v = queue.pop()
        for u in graph[v]:
            if u not in visited:
                visited.append(u)
                queue.append(u)
    return visited


def dijkstra(graph, start, end):
    import heapq
    """
    此处的图存储方式为：
    weighted_graph = {
        '0': [['1', 2], ['2', 5]],
        '1': [['0', 2], ['3', 3], ['4', 1]],
        '2': [['0', 5], ['5', 3]],
        '3': [['1', 3]],
        '4': [['1', 1], ['5', 3]],
        '5': [['2', 3], ['4', 3]]
    }
    """
    heap = [(0, start)]
    visited = []
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.append(u)

        if u == end:
            return cost

        for v, c in graph[u]:
            if v in visited:
                continue
            nxt = cost + c
            heapq.heappush(heap, (nxt, v))
    return -1


if __name__ == '__main__':
    # main1()
    # main2()
    g = {
        '0': ['1', '2'],
        '1': ['0', '3'],
        '2': ['0', '4'],
        '3': ['1'],
        '4': ['2']
    }
    print(dfs(g, '0'))
    print(bfs(g, '0'))
    weighted_graph = {
        '0': [['1', 2], ['2', 5]],
        '1': [['0', 2], ['3', 3], ['4', 1]],
        '2': [['0', 5], ['5', 3]],
        '3': [['1', 3]],
        '4': [['1', 1], ['5', 3]],
        '5': [['2', 3], ['4', 3]]
    }
    shortest = dijkstra(weighted_graph, '4', '2')
    print(shortest)
