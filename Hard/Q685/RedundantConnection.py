from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        v = set(x for x in range(1, len(edges)+1))
        ans = -1
        for x in range(len(edges)):
            if edges[x][1] in v:
                v.discard(edges[x][1])
            else:
                ans = x
                break
        if ans == -1:
            return 0

edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
sol = Solution()
print(sol.findRedundantDirectedConnection(edges))