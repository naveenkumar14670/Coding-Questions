from BST_From_Array import BST
from itertools import permutations, combinations, combinations_with_replacement
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
import copy
import heapq
import math
import sys
sys.path.append('C:\\Users\\Naveen\Desktop\\Coding\\Coding-Questions')
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
# Functions for Inorder Predecessor and Successor


def Min_In_RightTree(root):
    if(root.left == None):
        return root.data
    return Min_In_RightTree(root.left)


def Max_In_LeftTree(root):
    if(root.right == None):
        return root.data
    return Max_In_LeftTree(root.right)


def find_Inorder_Successor(root, ans, target):
    if(root == None):
        return ans
    if(root.data == target):
        if((ans != -1 and root.right == None) or root.right == None):
            return ans
        else:
            return Min_In_RightTree(root.right)
    elif(target < root.data):
        ans = root.data
        return find_Inorder_Successor(root.left, ans, target)
    else:
        return find_Inorder_Successor(root.right, ans, target)


def find_Inorder_Predecessor(root, ans, target):
    if(root == None):
        return ans
    if(root.data == target):
        if((ans != -1 and root.left == None) or root.left == None):
            return ans
        else:
            return Max_In_LeftTree(root.left)
    elif(target > root.data):
        ans = root.data
        return find_Inorder_Predecessor(root.right, ans, target)
    else:
        return find_Inorder_Predecessor(root.left, ans, target)


# Reading input array
n = get_int()
l = list_ints()
k = get_int()

# Creating Tree from the given array
obj = BST(n, l)
root = obj.createTree()
print('Tree:', end=' ')
obj.inorder(root)
print()

print('Inorder Predecessor:', find_Inorder_Predecessor(root, -1, k))
print('Inorder Successor:', find_Inorder_Successor(root, -1, k))

'''
    Sample Input:
        7
        50 30 70 20 40 60 80
        65
    Sample Output:
        Tree: 20 30 40 50 60 70 80 
        Inorder Predecessor: 60
        Inorder Successor: 70
'''
