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
# 2.4) Class AVL_TREE :


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL_TREE:
    def getHeight(self, root):
        if(root == None):
            return 0
        return root.height

    def updateHeight(self, root):
        return 1+max(self.getHeight(root.left), self.getHeight(root.right))

    def getBalanceFactor(self, root):
        if(root == None):
            return 0
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        return (lh-rh)

    def getMinValueNode(self, root):
        if(root is None or root.left is None):
            return root
        return self.getMinValueNode(root.left)

    def rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.height = self.updateHeight(root)
        new_root.height = self.updateHeight(new_root)
        return new_root

    def rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.height = self.updateHeight(root)
        new_root.height = self.updateHeight(new_root)
        return new_root

    def insert(self, root, value):
        if(root == None):
            return Node(value)
        elif(value < root.data):
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        root.height = self.updateHeight(root)
        BF = self.getBalanceFactor(root)
        left_BF = self.getBalanceFactor(root.left)
        right_BF = self.getBalanceFactor(root.right)
        if(BF > 1 and left_BF >= 0):
            return self.rotate_right(root)
        if(BF < 1 and right_BF <= 0):
            return self.rotate_left(root)
        if(BF > 1 and left_BF < 0):
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if(BF < 1 and right_BF > 0):
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def delete(self, root, value):
        if(root == None):
            return root
        if(value < root.data):
            root.left = self.delete(root.left, value)
        elif(value > root.data):
            root.right = self.delete(root.right, value)
        else:
            if(root.left == None):
                temp = root.right
                root = None
                return temp
            elif(root.right == None):
                temp = root.left
                root = None
                return temp
            else:
                temp = self.getMinValueNode(root.right)
                root.data = temp.data
                root.right = self.delete(root.right, temp.data)
        root.height = self.updateHeight(root)
        BF = self.getBalanceFactor(root)
        left_BF = self.getBalanceFactor(root.left)
        right_BF = self.getBalanceFactor(root.right)
        if(BF > 1 and left_BF >= 0):
            return self.rotate_right(root)
        if(BF < 1 and right_BF <= 0):
            return self.rotate_left(root)
        if(BF > 1 and left_BF < 0):
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if(BF < 1 and right_BF > 0):
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def preOrder(self, root):
        if(root == None):
            return
        print(root.data, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)


# Reading Input
l = list_ints()
tree = AVL_TREE()
root = None

for val in l:
    root = tree.insert(root, val)

print('Initial Tree:', end=' ')
tree.preOrder(root)
print()

root = tree.delete(root, 5)
print('Tree after Deletion:', end=' ')
tree.preOrder(root)
print()
