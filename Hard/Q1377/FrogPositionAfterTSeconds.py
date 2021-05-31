import collections
from typing import List
# excellent job


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        d = collections.defaultdict(set)
        ans = collections.defaultdict(float)
        for x in edges:
            d[x[0]].add(x[1])
            d[x[1]].add(x[0])
        self.dp(d, ans, {1}, 1, 0, 1, t)
        return ans[target]

    def dp(self, d: dict, ans: dict, v: set, c: int, t: int, p: float, T: int):
        n = d[c] - v
        if t == T or len(n) == 0:
            ans[c] += p
            return 0
        for x in n:
            v.add(x)
            self.dp(d, ans, v, x, t + 1, p / len(n), T)
            v.remove(x)
        return 0


n1 = 7
edges1 = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
t1 = 1
target1 = 7

n2 = 7
edges2 = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
t2 = 20
target2 = 6

sol = Solution()
print(sol.frogPosition(n1, edges1, t1, target1))
