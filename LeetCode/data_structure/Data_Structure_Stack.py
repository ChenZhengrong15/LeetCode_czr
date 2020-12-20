# coding: UTF-8
# python 实现一个栈


class Stack:
    def __init__(self, limit=100):
        self.stack = []  # 存放元素
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            raise IndexError("StackOverflowError")
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")  # 空栈

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)


def balanced_parentheses(parentheses):
    stack = Stack(len(parentheses))
    for c in parentheses:
        if c == "(":
            stack.push(c)
        elif c == ")":
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return stack.is_empty()


if __name__ == "__main__":
    examples = ["((((())))", "((()))", "((()))))(("]

    for example in examples:
        print(example + ": " + str(balanced_parentheses(example)))

