import sys
sys.setrecursionlimit(10**7)

from functools import reduce
from collections import deque
# function : append,appendleft,pop,popleft
from collections import defaultdict
# g = defaultdict(list)
from collections import Counter
from itertools import accumulate
from itertools import product, permutations, combinations
# list(itertools.permutations([1,2,3],2)) # => [(1,2),(1,3),(2,3),...]
# list(itertools.product(["","+"],repeat=3))
import bisect
# v = bisect_right(seq, x) => x < a[v:], a[:v] <= x
from heapq import heappop, heappush
# heappush(h, (5, 'type'))

# memos

# dp[a][b] : dp = [[0]*b for i in range(a)]
