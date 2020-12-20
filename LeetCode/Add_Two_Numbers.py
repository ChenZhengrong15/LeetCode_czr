# coding: UTF-8
# 求两数之和


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumyHead = ListNode(0)
        cur = dumyHead
        carry = 0
        while l1 or l2:
            vall1 = l1.val if l1 else 0
            vall2 = l2.val if l2 else 0
            total = vall1 + vall2 + carry
            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            cur.next = ListNode(carry)
        return dumyHead.next



