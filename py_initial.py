import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
from itertools import combinations, permutations, product, accumulate, groupby
from collections import defaultdict, deque, Counter
from functools import reduce
from operator import add, mul
import heapq as hq
import bisect
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
# = input().strip()
# = int(input())
# = map(int,input().split())
# = list(map(int,input().split()))
# = [input().strip() for i in range(H)]
# = [list(map(int,input().split())) for i in range(N)]
