import sys
import math
import heapq
import copy
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from functools import cmp_to_key
from itertools import permutations, combinations, combinations_with_replacement
# sys.setrecursionlimit(10**6)
sys.stdin = open('Input.txt', 'r')
sys.stdout = open('Output.txt', 'w')
mod = 1000000007
# Reading Single Input
def get_int(): return int(sys.stdin.readline().strip())
def get_str(): return sys.stdin.readline().strip()
def get_float(): return float(sys.stdin.readline().strip())
# Reading Multiple Inputs
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_strs(): return map(str, sys.stdin.readline().strip().split())
def get_floats(): return map(float, sys.stdin.readline().strip().split())
# Reading List Of Inputs
def list_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def list_strs(): return list(map(str, sys.stdin.readline().strip().split()))
def list_floats(): return list(map(float, sys.stdin.readline().strip().split()))
# -------------------------------------------------------------------------------------
# 2.11) Trie Data Structure


class Trie_Node:
    def __init__(self, size):
        self.child = [False for i in range(size)]
        self.isEnd = False


class Trie:
    def __init__(self, size):
        self.size = size
        self.root = Trie_Node(self.size)

    def insert(self, word):
        root = self.root
        for i in word:
            value = ord(i)-ord('a')
            if(root.child[value] == False):
                root.child[value] = Trie_Node(self.size)
            root = root.child[value]
        root.isEnd = True

    def search(self, word):
        root = self.root
        for i in word:
            value = ord(i)-ord('a')
            if(root.child[value] == False):
                return False
            root = root.child[value]
        return root.isEnd

    def isEmpty(self, arr):
        for i in range(self.size):
            if(arr[i] != False):
                return False
        return True

    def remove_util(self, root, word, i):
        if(i == len(word)):
            root.isEnd = False
            if(self.isEmpty(root.child)):
                del root
                root = False
            return root
        value = ord(word[i])-ord('a')
        root.child[value] = self.remove_util(root.child[value], word, i+1)
        if(self.isEmpty(root.child) and root.isEnd == False):
            del root
            root = False
        return root

    def remove(self, word):
        if(self.search(word) == False):
            return
        else:
            root = self.root
            self.root = self.remove_util(root, word, 0)

    def display_util(self, root, s):
        if(root.isEnd == True):
            print(s, end=' ')
        for i in range(self.size):
            if(root.child[i] != False):
                letter = chr(ord('a')+i)
                self.display_util(root.child[i], s+letter)
        return

    def display(self):
        root = self.root
        self.display_util(root, "")


# Reading Input
size = get_int()
l = list_strs()

# Initializing Trie
obj = Trie(size)

# Insertion in Trie
for word in l:
    obj.insert(word)

# Displaying Trie
print('Words in Trie:')
obj.display()
print()

# Searching in Trie
print('Searcing for word "world" :', obj.search('world'))

# Deletion in Trie
obj.remove('world')
print('Searcing for word "world" :', obj.search('world'))

'''
    Sample Input:
        26
        welcome to competitive world
    Sample Output:
        Words in Trie:
        competitive to welcome world 
        Searcing for word "world" : True
        Searcing for word "world" : False
'''
