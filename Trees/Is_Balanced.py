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
# Is Balanced Tree ?


def is_balanced(root):
    if(root == None):
        return 0
    lh = is_balanced(root.left)
    if(lh == -1):
        return -1
    rh = is_balanced(root.right)
    if(rh == -1):
        return -1
    x = abs(lh-rh)
    if(x > 1):
        return -1
    return max(lh, rh)+1


# Reading Input
n = get_int()
l = list_ints()

# Creating Tree from the given array
obj = BST(n, l)
root = obj.createTree()

print('Not Balanced') if(is_balanced(root) == -1) else print('Balanced')

'''
    Sample Input:
        3
        20 10 30
    Sample Output:
        Balanced
'''
