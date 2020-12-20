# coding:UTF-8
# 实现一个并查集


class UnionFind:
    def __init__(self, data_list):
        self.data_list = data_list
        self.parent_dict = dict()
        self.size_dict = dict()
        for node in data_list:
            self.parent_dict[node] = node
            self.size_dict[node] = 1

    def find(self, node):
        parent = self.parent_dict[node]
        if node != parent:
            parent = self.find(parent)
        self.parent_dict[node] = parent
        return parent

    def is_same_set(self, node_a, node_b):
        return self.find(node_a) == self.find(node_b)

    def print_dict(self):
        print(self.parent_dict, self.size_dict)

    def union(self, node_a, node_b):
        if node_a is None or node_b is None:
            return
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)

        if parent_a != parent_b:
            set_size_a = self.size_dict[parent_a]
            set_size_b = self.size_dict[parent_b]
        else:
            return

        if set_size_a >= set_size_b:
            self.parent_dict[parent_b] = parent_a
            self.size_dict[parent_a] = set_size_a + set_size_b
        else:
            self.parent_dict[parent_a] = parent_b
            self.size_dict[parent_b] = set_size_a + set_size_b


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    union_find = UnionFind(a)
    union_find.union(1, 2)
    union_find.union(3, 5)
    union_find.union(3, 1)
    print(union_find.is_same_set(2, 4))


