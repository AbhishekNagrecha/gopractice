# Problem: Remove duplicates from a linked list

class LinkedList(object):
    pass


class MyLinkedList(LinkedList):
    def remove_duplicates(self):
        if self.head is  None:
            return
        node = self.head
        seen_data = set()
        while node is not None:
            if node.data  not in seen_data:
                seen_data.add(node.data)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next
    def remove_duplicates_single_pointer(self):
        if self.head is  None:
            return
        node = self.head
        seen_data = set({node.data})
        while node.next is not None:
            if node.next.data in seen_data:
                node.next = node.next.next
            else:
                seen_data.add(node.next.data)
                node = node.next.next

    def remove_duplicates_in_place(self):
        curr = self.head
        while curr is not None:
            runner = curr
            while runner.next is not None:
                if runner.next.data == curr.data:
                    runner.next = runner.next.next
                else:
                    runner.next = runner.next
            curr = curr.next


# Problem: Find the kth to last element of a linked list.

class MyLinkedList(LinkedList):
    def kth_to_last(self, k):
        if self.head is None:
            return None
        fast = self.head
        slow = self.head

        for _ in range(k):
            fast = fast.next
            if fast is None:
                return None

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.data

#Problem: Delete a node in the middle, given only access to that node.

class MyLinkedLis(LinkedList):
    def delete_node(self, node):
        if node is None:
            return
        if node.next is None:
            node.data = None
        else:
            node.data = node.next
            node.next = node.next.next

#Problem: Partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x

class MyLinkedList(LinkedList):
    def partition(self, data):
        if self.head is None:
            return
        left = MyLinkedList(None)
        right = MyLinkedList(None)
        curr = self.head

        while curr is not None:
            if curr.data < data:
                left.append(curr.data)
            elif curr.data == data:
                right.insert_to_front(curr.data)
            else:
                right.append(curr.data)
                curr = curr.next
        curr_left = left.head
        if curr_left is None:
            return right
        else:
            while curr_left is not None:
                curr_left = curr_left.next
                curr_left.next = right.head
                return left

