# Problem: Add two numbers whose digits are stored in a linked list in reverse order
from lib2to3.pytree import Node

from Day3 import LinkedList


class MyLinkedList(LinkedList):
    def add_reverse(self, first_node, second_node, carry):
        if first_node is None and second_node is None and not carry:
            return None

        value = carry
        value += first_node.data if first_node is not None else 0
        value += second_node.data if second_node is not None else 0
        carry = 1 if value >= 10 else 0
        value %= 10
        node = Node(value)
        node.next = self._add_reverse(
            first_node.next if first_node is not None else None,
            second_node.next if second_node is not None else None, carry)
        return node
    def add_reverse(self, first_list, second_list):
        if first_list is None or second_list is None:
            return None
        head = self._add_reverse(first_list.head, second_list.head, 0)
        return MyLinkedList(head)


#Problem: Find the start of a linked list loop

class MyLinkedList(LinkedList):
    def find_loop_start(self):
        if self.head is None or self.head.next is None:
            return None
        slow = self.head
        fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                return None
            if slow == fast:
                break
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
        return slow

#Problem: Determine if a linked list is a palindrome.

from __future__ import division


def iterations(args):
    pass


class MyLinkedList(LinkedList):
    def is_palindrome(self, reversed_list):
        if self.head is None or self.head.next is None:
            return False
        curr = self.head
        reverse_list = MyLinkedList()
        length = 0

        while curr is not None:
            reverse_list.insert_to_front(curr.data)
            length += 1
            curr = curr.next

        iteration = length // 2
        curr = self.head
        curr_reversed = reversed_list.head
        for __ in range(iterations):
            if curr.data != curr.reversed.data:
                return False
            curr = curr.next
            curr_reversed = curr_reversed.next
            return True



