# coding: utf-8


class TrieNode:
    def __init__(self):
        self.nodes = dict()
        self.is_leaf = False

    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def search(self, word):
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf

    # def __str__(self):
    #     return str(self.nodes)


if __name__ == '__main__':
    trie = TrieNode()
    l = ['good', 'god', 'body', 'somebody', 'life']
    for i in l:
        trie.insert(i)
    # print(trie)
    print(trie.search('google'))
    print(trie.search('god'))
