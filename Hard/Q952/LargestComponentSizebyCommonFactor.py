import math
from typing import List


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        p = [x for x in range(len(A))]
        n = [1 for _ in range(len(A))]
        for x in range(len(A) - 1):
            for y in range(x + 1, len(A)):
                if math.gcd(A[x], A[y]) > 1:
                    self.union(x, y, p, n)
        return max(n)

    def findParent(self, x: int, p: List[int]):
        if p[x] == x:
            return x
        p[x] = self.findParent(p[x], p)
        return p[x]

    def union(self, x: int, y: int, p: List[int], n: List[int]):
        x, y = self.findParent(x, p), self.findParent(y, p)
        if x == y:
            return 0
        if n[x] < n[y]:
            x, y = y, x
        p[y] = x
        n[x] = n[y] + n[x]


A1 = [2, 3, 6, 7, 4, 12, 21, 39]
sol = Solution()
sol.largestComponentSize(A1)
