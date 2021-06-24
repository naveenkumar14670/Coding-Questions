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
# Level Order Traversal Of A Tree


def level_order_traversal(root):
    if(root == None):
        return
    q = deque()
    q.append(root)
    while(q):
        n = len(q)
        for i in range(n):
            Node = q.popleft()
            print(Node.data, end=' ')
            if(Node.left != None):
                q.append(Node.left)
            if(Node.right != None):
                q.append(Node.right)
        print()
    return


# Reading Input
n = get_int()
l = list_ints()

# Creating Tree from the given array
obj = BST(n, l)
root = obj.createTree()

level_order_traversal(root)

'''
    Sample Input:
        3
        20 10 30
        10
    Sample Output:
        20 
        10 30 
'''
