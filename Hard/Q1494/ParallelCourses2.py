from typing import List
import itertools

# kinda boring question while still important
# try to use the stupid way sometimes

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        s = set(x for x in range(1, n + 1))
        d = set((v[0], v[1]) for v in dependencies)
        i = s - set(e[1] for e in d) - set(e[0] for e in d)
        return self.recursive(s - i, d, k, len(i))

    def recursive(self, s, d, k, i):
        if len(s) == 0 and i == 0:
            return 0
        elif len(s) == 0:
            return i // k + min(1, i % k)
        visit = s - set(e[1] for e in d)
        if len(visit) <= k:
            d = set(filter(lambda e: e[0] not in visit, d))
            return 1 + self.recursive(s - visit, d, k, max(i - (k - len(visit)), 0))
        else:
            comb = itertools.combinations(visit, k)
            ans = float("inf")
            for c in comb:
                d2 = set(filter(lambda e: e[0] not in c, d))
                ans = min(ans, 1 + self.recursive(s - set(c), d2, k, i))
            return ans


n1 = 5
d1 = [[2, 1], [3, 1], [4, 1], [1, 5]]
k1 = 2

n2 = 4
d2 = [[2, 1], [3, 1], [1, 4]]
k2 = 2

n3 = 15
d3 = [[2, 1]]
k3 = 4

n4 = 2
d4 = []
k4 = 2

sol = Solution()
print(sol.minNumberOfSemesters(n4, d4, k4))
