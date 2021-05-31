from typing import List
# kinda good job
# need further optimizing

class Solution:
    def candy(self, ratings: List[int]) -> int:
        value = [x[0] for x in sorted(enumerate(ratings), key=lambda a: a[1])]
        rank = [0 for _ in range(len(ratings))]
        f = lambda a: ratings[a] if -1 < a < len(ratings) else float("inf")
        g = lambda a, b: rank[a] if f(a) < f(b) else 0
        for x in range(len(ratings)):
            rank[value[x]] = max(g(value[x]-1, value[x]), g(value[x]+1, value[x])) + 1
        return sum(rank)


c1 = [100]
sol = Solution()
sol.candy(c1)
