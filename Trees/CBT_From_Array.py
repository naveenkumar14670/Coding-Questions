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
# Creation Of Complete Binary Tree From An Array


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, n, l):
        self.n = n
        self.l = l
        self.l.insert(0, 0)

    def createTree(self):
        root = Node(self.l[1])
        q = [root]
        x = self.n//2
        for i in range(1, x+1):
            temp = q.pop(0)
            if(2*i <= self.n):
                temp.left = Node(self.l[2*i])
                q.append(temp.left)
            if(2*i+1 <= self.n):
                temp.right = Node(self.l[2*i+1])
                q.append(temp.right)
        return root

    def inorder(self, root):
        if(root == None):
            return
        self.inorder(root.left)
        print(root.data, end=' ')
        self.inorder(root.right)
        return


# Reading input array
n = get_int()
l = list_ints()

# Creating Tree from the given array
obj = BST(n, l)
root = obj.createTree()

# Verifying tree by inorder traversal
obj.inorder(root)

'''
Sample Input:
3
2 1 3

Sample Output:
1 2 3

'''
