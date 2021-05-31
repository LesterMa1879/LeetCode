import bisect
from typing import List
# need optimizing

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        s, p, ans, sums = [], [], 0, 0
        for x in range(n):
            s.append((efficiency[x], speed[x]))
        s = sorted(s, key=lambda a: a[0])
        s.reverse()
        for x in range(n):
            bisect.insort(p, s[x][1])
            if len(p) <= k:
                sums += s[x][1]
            else:
                if p[-k] <= s[x][1]:
                    sums = sums + s[x][1] - p[-k-1]
            ans = max(ans, s[x][0]*sums)
        return ans % 1000000007


n1 = 6
s1 = [2, 10, 3, 1, 5, 8]
e1 = [5, 4, 3, 9, 7, 2]
k1 = 2

n2 = 6
s2 = [2, 10, 3, 1, 5, 8]
e2 = [5, 4, 3, 9, 7, 2]
k2 = 4
sol = Solution()
print(sol.maxPerformance(n2, s2, e2, k2))
