#Problem: Implement n stacks using a single array

class Stacks(object):
    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.stack_pointers = [-1] * self.num_stacks
        self.stack_array = [None] * self.num_stacks * self.stack_size

    def abs_index(self, stack_index):
        return stack_index * self.stack_size + self.stack_pointers[stack_index]
    
    def push(self, stack_index, data):
        if self.stack_pointers[stack_index]  == self.stack_size - 1:
            raise Exception("Stack is full")
        self.stack_pointers[stack_index] += 1
        array_index = self.abs_index(stack_index)
        self.stack_array[array_index] = data

    def pop(self, stack_index):
        if self.stack_pointers[stack_index] == -1:
            raise Exception("Stack is Empty")
        array_index = self.abs_index(stack_index)
        data = self.stack_array[array_index]
        self.stack_array[array_index] = None
        self.stack_pointers[stack_index] -= 1
        return data


# Array Is Unique

class unique(object):
    def isunique(str):
        str = str.lower()
        seen = set()
        for char in str:
            if char in seen:
                return False
            else:
                seen.add(char)
        return True

# Array Check Permutation
#The input is two strings. Check if the first string is a permutation of the second string.

class permutation(object):
    def checkpermutation(self, str1, str2):
        if len(str1) != len(str2):
            return False

        count = {} #creates a dictionery
        for i in str1:
            count[i] = count.get(i,0) + 1
        for i in str2:
            count[i] -= 1
            if count[i] == 0:
                del count[i]
            else:
                return False
        return len(count) == 0


#Problem: Implement n stacks using a single array

class Stack(object):
    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.stack_pointers = [-1] * self.num_stacks
        self.stack_array = [None] * self.num_stacks * self.stack_size

    def abs_index(self, stack_index):
        return stack_index * self.stack_size + self.stack_pointers[stack_index]
    
    def push(self, stack_index, data):
        if self.stack_pointers[stack_index] == self.stack_size - 1:
            raise Exception('Stack is full')
        self.stack_pointers[stack_index] += 1
        array_index = self.abs_index(stack_index)
        self.stack_array[array_index] = data
        
    def pop(self, stack_index):
        if self.stack_pointers[stack_index] == -1:
            raise Exception('Stack is empty')
        array_index = self.abs_index(stack_index)
        data = self.stack_array[array_index]
        self.stack_array[array_index] = None
        self.stack_pointers[stack_index] -=1
        return data



#Problem: Implement a stack with push, pop, and min methods running O(1) time.

import sys

class StackMin(Stack):
    def __init__(self, top= None):
        super(StackMin, self).__init__(top)
        self.stack_of_mins = Stack()

    def minimum(self):
        if self.stack_of_mins.top is None:
            return sys.maxsize
        else:
            return self.stack_of_mins.peek()

    def push(self, data):
        super(StackMin, self).push(data)
        if data < self.minimum():
            self.stack_of_mins.push(data)
            
    def pop(self):
        data = super(StackMin, self).pop()
        if data == self.minimum():
            self.stack_of_mins.pop()
            return data








