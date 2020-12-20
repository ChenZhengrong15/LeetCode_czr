# coding: UTF-8
# 单链表
# 双链表


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def link_append(self, item):
        element = Node(item)
        cur = self.head
        if self.head:
            while cur:
                cur = cur.next
            cur.next = element
        else:
            self.head = element

    def is_empty(self):
        return not self.head

    def get_length(self):
        cur = self.head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        return length

    def link_insert(self, position, new_element):
        if position < 0 or position > self.get_length():
            raise IndexError("Invalid position, position out of range")
        temp = self.head
        cur_position = 0
        pre = None
        while cur_position < position:
            pre = temp
            temp = temp.next
            cur_position += 1
        pre.next = new_element
        new_element.next = temp

    def link_remove(self, position):
        if position < 0 or position > self.get_length():
            raise IndexError("Invalid position, position out of range")
        cur_position = 0
        temp = self.head
        while temp is not None:
            if position == 0:
                self.head = temp.next
                temp.next = None
                return

            pre = temp
            temp = temp.next
            cur_position += 1
            if cur_position == position:
                pre.next = temp.next
                temp.next = None
                return

    def link_reverse(self):
        pre = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        self.head = pre

    def link_print(self):
        temp = self.head
        lst = []
        while temp is not None:
            lst.append(temp.data)
            temp = temp.next
        print("Link List: ", lst)

    def convert2link(self, data_list):
        self.head = Node(data_list[0])
        temp = self.head
        for i in data_list[1:]:
            temp.next = Node(i)
            temp = temp.next
        # return self

    def link_search(self, data):
        temp = self.head
        indexes = []  # 记录索引
        cur_position = 0
        while temp:
            if temp.data == data:
                indexes.append(cur_position)
            temp = temp.next
            cur_position += 1
        if not indexes:
            return False
        else:
            return indexes


class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self._head = None

    def link_append(self, element):  # 尾部插入
        node = DoubleNode(element)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not Node:
                cur = cur.next
            cur.next = Node
            node.prev = cur

    def link_add(self, element):  # 头部插入
        node = DoubleNode(element)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def link_remove(self, position):  # position 是索引
        if position < 0 or position >= self.get_length():
            raise IndexError("Invalid position, position out of range")
        elif self.is_empty():
            raise IndexError("Empty linked list...")
        else:
            cur_position = 0
            temp = self._head
            if position == 0:
                if self._head.next is None:
                    self._head = None
                else:
                    temp.next.prev = None
                    self._head = temp.next
                return
            while cur_position < position:
                temp = temp.next
                cur_position += 1
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

    def link_insert(self, item, position):  # position 索引
        if position < 0 or position > self.get_length():
            raise IndexError("Invalid position, position out of range")
        elif position == 0:
            self.link_add(item)
        elif position == self.get_length()-1:
            self.link_append(item)
        else:
            node = DoubleNode(item)
            cur_position = 0
            temp = self._head
            while cur_position < position:
                cur_position += 1
                temp = temp.next
            node.prev = temp
            node.next = temp.next
            temp.next.prev = node
            temp.next = node

    def is_empty(self):
        return self._head is None

    def get_length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def link_search(self, data):
        indexes = []
        temp = self._head
        idx = 0
        while temp is not None:
            if temp.data == data:
                indexes.append(idx)
            temp = temp.next
            idx += 1
        if indexes:
            return indexes
        else:
            return False

    def convert2doublelist(self, data_list):
        self._head = DoubleNode(data_list[0])
        temp = self._head
        for i in data_list[1:]:
            node = DoubleNode(i)
            temp.next = node
            node.prev = temp
            temp = temp.next

    def link_print(self):
        lst = []
        temp = self._head
        while temp is not None:
            lst.append(temp.data)
            temp = temp.next
        print("Double link list: ", lst)


if __name__ == '__main__':
    l = [3, 6, 4, 5, 6, 9]
    dl = DLinkedList()
    dl.convert2doublelist(l)
    dl.link_print()
    h = Node(0)
    sl = LinkedList()
    # aa = sl.convert2link(l)
    sl.convert2link(l)
    sl.link_print()
    sl.link_remove(3)
    sl.link_print()
    print(h)
    # print(aa)
