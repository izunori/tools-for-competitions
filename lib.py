import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline
input = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**7)

#### functools
from functools import reduce
from functools import lru_cache
@lru_cache(maxsize=None)
def f(i):
    pass

#### collections
from collections import deque # function : append,appendleft,pop,popleft
from collections import defaultdict # g = defaultdict(list)
from collections import Counter

#### itertools
from itertools import accumulate
from itertools import permutations
from itertools import product
from itertools import combinations
# list(itertools.permutations([1,2,3],2)) # => [(1,2),(1,3),(2,3),...]
# list(itertools.product(["","+"],repeat=3))

#### bisect
import bisect # v = bisect_right(seq, x) => x < a[v:], a[:v] <= x
print(bisect.bisect([1,2,2,3],2))# => 3
print(bisect.bisect_left([1,2,2,3],2))# => 1
print(bisect.bisect([1,3],2))# => 1
print(bisect.bisect_left([1,3],2))# => 1

#### heapq 
from heapq import heappop, heappush
h = []
heappush(h, (5, '3rd'))
heappush(h, (4, '2nd'))
heappush(h, (7, '1st'))
heappop(h) # (7,'1st')->(4,'2nd')->(5,'3rd')

#### numpy
import numpy as np
#inds, cnts = np.unique(residue, return_counts=True) # <= not work in atcoder!!
np.bitwise_xor.reduce([[2,2],[3,3],[4,5]])

#### line profiler
kernprof -l xxx.py
python -m line_profiler xxx.py.lprof

#### memos
dp = [[0]*b for i in range(a)] # dp[a][b]

AB = [list(map(int,input().split())) for i in range(N)]
A, B = map(list,zip(*AB)) # flatten

def dpinit(ps, val=0):
    import copy
    res = [val for i in [0]*ps[-1]]
    for i in ps[:-1][::-1]:
        res = [copy.deepcopy(res) for k in [0]*i]
    return res

def dprint(*args,dic=globals()):
    p = []
    for arg in args:
        for k,v in dic.items():
            if id(v) == id(arg):
                p.append(f"{k}:{v}")
    print(*p)
class M1:
    def __init__(self, dims):
        self.offset = [1]
        for d in dims[::-1][:-1]:
            self.offset.append(self.offset[-1]*d)
        self.offset.reverse()
    def getIndex(self, pt):
        return sum(starmap(mul, zip(pt,self.offset)))
    def getPoint(self, index):
        res = []
        for ofs in self.offset:
            res.append(index//ofs)
            index -= res[-1]*ofs
        return res


# power set
from itertools import chain, combinations
s = [1,2,3]
chain.from_iterable(combinations(s,r) for r in range(len(s)+1))
