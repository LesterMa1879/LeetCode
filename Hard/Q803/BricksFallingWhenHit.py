from typing import List
import Test


# IMPORTANT QUESTION !!! REVIEW !!!
# disjoint set union-find

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        parent = [0] * (m * n)
        size = [0] * (m * n)
        empty = []
        ans = []
        for h in hits:
            if grid[h[0]][h[1]] == 1:
                empty.append(1)
                grid[h[0]][h[1]] = 0
            else:
                empty.append(0)
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    parent[x * m + y] = x * m + y
                    size[x * m + y] = 1
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    for a, b in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:
                        if -1 < a < n and -1 < b < m and grid[a][b] == 1:
                            self.union(x * m + y, a * m + b, m, parent, size)
        hits.reverse()
        empty.reverse()
        for t in range(len(hits)):
            fall = 0
            visit = set()
            x, y = hits[t]
            if empty[t] == 0:
                ans.append(0)
                continue
            else:
                grid[x][y] = 1
                parent[x * m + y] = x * m + y
                size[x * m + y] = 1
            for a, b in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:
                if -1 < a < n and -1 < b < m and grid[a][b] == 1:
                    pare = self.find(a * m + b, parent)
                    if pare >= m and pare not in visit:
                        visit.add(pare)
                        fall += size[pare]
                    self.union(x * m + y, a * m + b, m, parent, size)
            if self.find(x * m + y, parent) < m:
                ans.append(fall)
            else:
                ans.append(0)
        return ans[::-1]

    def find(self, x, parent):
        if parent[x] == x:
            return x
        else:
            parent[x] = self.find(parent[x], parent)
            return parent[x]

    def union(self, x, y, m, parent, size):
        x, y = self.find(x, parent), self.find(y, parent)
        if x == y:
            return 0
        if x < m:
            x, y = x, y
        elif y < m:
            x, y = y, x
        elif size[x] < size[y]:
            x, y = y, x
        parent[y] = x
        size[x] += size[y]


g5 = [[1, 1, 1, 0, 0],
      [0, 1, 1, 1, 0],
      [0, 0, 1, 1, 1],
      [0, 1, 1, 1, 0]]

h5 = [[1, 2], [2, 3]]

sol = Solution()
print(sol.hitBricks(Test.g5, Test.h5))
