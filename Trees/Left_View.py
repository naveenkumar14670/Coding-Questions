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

# Left View Of A Tree


def left_view_iterative(root):
    if(root == None):
        return
    q = deque()
    q.append(root)
    while(q):
        n = len(q)
        for i in range(n):
            Node = q.popleft()
            if(i == 0):
                print(Node.data, end=' ')
            if(Node.left != None):
                q.append(Node.left)
            if(Node.right != None):
                q.append(Node.right)
    print()
    return


def left_view_recursive(root, level, max_level):
    if(root == None):
        return
    if(max_level[0] < level):
        print(root.data, end=' ')
        max_level[0] = level
    left_view_recursive(root.left, level+1, max_level)
    left_view_recursive(root.right, level+1, max_level)
    return


# Reading Input
n = get_int()
l = list_ints()

# Creating Tree from the given array
obj = BST(n, l)
root = obj.createTree()

print('Iterative Method:', end=' ')
left_view_iterative(root)
mx = [-1]
print('Recursive Method:', end=' ')
left_view_recursive(root, 0, mx)

'''
    Sample Input:
        3
        20 10 30
        10
    Sample Output:
        Iterative Method: 20 10
        Recursive Method: 20 10 
'''
