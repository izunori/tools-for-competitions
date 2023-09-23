MOD=998244353
import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
from itertools import combinations, permutations, product, accumulate, groupby
from more_itertools import chunked, windowed, distribute, powerset
from collections import defaultdict, deque, Counter
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter
import array as ar
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
