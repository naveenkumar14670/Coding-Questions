from BST_From_Array import BST
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
# Level Of A Node


def Level(root, key, level):
    if(root == None):
        return -1
    if(root.data == key):
        return level
    x = Level(root.left, key, level+1)
    y = Level(root.right, key, level+1)
    return max(x, y)


# Reading Input
n = get_int()
l = list_ints()
key = get_int()

# Creating Tree from the given array
obj = BST(n, l)
root = obj.createTree()

print('Tree:', end=' ')
obj.inorder(root)
print()

print('Level of', key, ':', Level(root, key, 0))

'''
    Sample Input:
        3
        20 10 30
        10
    Sample Output:
        Tree: 10 20 30 
        Level of 10 : 1
'''
