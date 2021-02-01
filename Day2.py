#Problem: Implement a function to reverse a string (a list of characters), in-place

from __future__ import division

from operator import index


class ReverseString(object):
    def reverse(self, char):
        if char:
            size = len(char)
            for i in range(size // 2):
                char[i], char[size-1 - i] = \
                char[size-1 - i], char[i]
                return char


#Pythonic-Code

class reversestring(object):
    def reverse(string):
        if string:
            return string[::, -1]
        return string

    def reversestring2(string):
        if string:
            return ''.join(reversed(string))
        return string

#Problem: Find the single different char between two strings

class solution(object):
    def find_different(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError("str1 or str2 cannot be None")
        seen = {}
        for char in str1:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        for char in str2:
            try:
                seen[char] -= 1
            except KeyError:
                return char
            if seen[char] < 0:
                return char
        for char, count in seen.items():
            return char

    def diff_xors(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError("It cannot be None")
        result = 0
        for char in str1:
            result ^= ord(char)
        for char in str2:
            result ^= ord(char)
        return char(result)

#Problem: Given an array, find the two indices that sum to a specific value

class solutio(object):
    def two_sum(self, nums, target):
        if nums is None or target is None:
            raise TypeError("it cannot be none")
        if not nums:
            raise ValueError("it cannot be empty")
        cache = {}
        for index, num in enumerate(nums):
            cache_target = target - num
            if num in cache:
                return[ cache[num], index ]
            else:
                cache[cache_target] = index
        return None

# Problem: Implement a hash table with set, get, and remove methods

class item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
class HashTable(object):
    def __init__(self, size):
        self.size =size
        self.type = [ [] for _ in range (self.size)]

    def _hash_function(self, key):
        return key % self.size

    def set (self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(item(key, value))

    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
            raise KeyError("key not found")

    def remove(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                del self.table[hash_index][index]
                return
            raise KeyError("key not found")

#Problem: Implement Fizz Buzz

class solution(object):
    def fizzbuzz(self, num):
        if num is None:
            raise TypeError("Please enter a valid number")
        if num < 1:
            raise ValueError("number cannot be less than 1")
        results = []
        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                results.append('FizzBuzz')
            elif i % 3 == 0:
                results.append('Fizz')
            elif i % 5 == 0:
                results.append('Buzz')
            else:
                results.append(str(i))
        return results




