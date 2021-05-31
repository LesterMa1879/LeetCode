from typing import List
from collections import deque
# need optimizing

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        order, n, m = [[0, 0, 1]], len(forest), len(forest[0])
        for x in range(n):
            for y in range(m):
                if forest[x][y] > 1:
                    order.append([x, y, forest[x][y]])
        order = sorted(order, key=lambda a: a[2])
        ans = 0
        for x in range(1, len(order)):
            s, t = (order[x - 1][0], order[x - 1][1]), (order[x][0], order[x][1])
            d = self.bfs(forest, deque([(s[0], s[1], 0)]), {s}, t)
            if d == -1:
                return -1
            else:
                ans += d
            forest[t[0]][t[1]] = 1
        return ans

    def bfs(self, forest: List[List[int]], q: deque, v: set, t: tuple):
        while len(q) > 0:
            s = q.popleft()
            if s[0] == t[0] and s[1] == t[1]:
                return s[2]
            for x, y in [(s[0], s[1] + 1), (s[0], s[1] - 1), (s[0] + 1, s[1]), (s[0] - 1, s[1])]:
                if -1 < x < len(forest) and -1 < y < len(forest[0]) and forest[x][y] > 0 and (x, y) not in v:
                    v.add((x, y))
                    q.append((x, y, s[2] + 1))
        return -1


f1 = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]
f2 = [[1, 2, 3], [0, 0, 0], [7, 6, 5]]
f3 = [[2, 3, 4], [0, 0, 5], [8, 7, 6]]
f4 = [[54581641, 64080174, 24346381, 69107959], [86374198, 61363882, 68783324, 79706116],
      [668150, 92178815, 89819108, 94701471], [83920491, 22724204, 46281641, 47531096],
      [89078499, 18904913, 25462145, 60813308]]
test = [[1, 1, 1], [1, 3, 3], [2, 1, 1]]
sol = Solution()
# print(sol.bfs(test, deque([(0, 0, 0)]), {(0, 0)}, (2, 1)))
print(sol.cutOffTree(f4))
