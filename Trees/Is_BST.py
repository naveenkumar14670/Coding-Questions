from CBT_From_Array import CBT
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
# Is BST ?


def is_BST(root, minimum, maximum):
    if(root == None):
        return True
    if(minimum < root.data < maximum):
        left = is_BST(root.left, minimum, root.data)
        right = is_BST(root.right, root.data, maximum)
        return left and right
    return False


# Reading Input
n = get_int()
l = list_ints()

# Creating Tree from the given array
obj = CBT(n, l)
root = obj.createTree()

print('Tree:', end=' ')
obj.inorder(root)
print()

print('Valid BST:', is_BST(root, -math.inf, math.inf))

'''
    Sample Input:
        3
        10 5 40
    Sample Output:
        Tree: 5 10 40 
        Valid BST: True
'''
