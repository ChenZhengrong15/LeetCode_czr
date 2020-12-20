# coding: UTF-8
# 队列


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, element):
        p = Node(element)
        if self.is_empty():
            self.front = p
            self.rear = p
        else:
            self.rear.next = p
            self.rear = p

    def dequeue(self):
        if self.is_empty():
            raise IndexError("delete from empty queue")
        else:
            temp = self.front.data
            self.front = self.front.next
        return temp

    def peek(self):
        if self.is_empty():
            raise IndexError("Not found, empty queue")
        else:
            return self.front.data

    def queue_print(self):
        temp = self.front
        lst = []
        while temp is not None:
            lst.append(temp.data)
            temp = temp.next
        print("Queue: ", lst)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(21)
    queue.enqueue(35)
    queue.enqueue(58)
    queue.enqueue(13)
    queue.queue_print()
    print(queue.peek())
    queue.dequeue()
    queue.queue_print()
    print(queue.peek())
