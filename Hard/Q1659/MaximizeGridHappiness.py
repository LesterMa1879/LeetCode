from typing import List
import copy

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        ans = [[[] for _ in range(introvertsCount+1)] for _ in range(extrovertsCount+1)]
        grid = [[0 for _ in range(m)] for _ in range(n)]
        for x in range(len(ans)):
            for y in range(len(ans[0])):
                if x == 0 and y == 0:
                    ans[x][y].append(copy.deepcopy(grid))
                    continue
                elif x == 0:
                    for g in ans[x][y-1]:
                        continue
        return 0

    def dp0(self, grid: List[List[int]], value: int) -> (int, set):
        ans = set()
        max_inc = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    increase = self.update(grid, x, y, value)
                    if max_inc < increase:
                        max_inc = increase
                        ans = {(x, y)}
                    elif max_inc == increase:
                        ans.add((x, y))
        return max_inc, ans

    def dp1(self, grid: List[List[int]]) -> (int, set):
        ans = set()
        min_pos = float("inf")
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    increase = self.update(grid, x, y, 1)
                    if increase == 120 and x+y < min_pos:
                        ans = {(x, y)}
                        min_pos = x+y
                    elif increase == 120 and x+y == min_pos:
                        ans.add((x, y))
        return min_pos, ans

    def update(self, grid: List[List[int]], x: int, y: int, value: int) -> int:
        neighbour1 = 0
        neighbour2 = 0
        for a, b in {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}:
            if -1 < a < len(grid) and -1 < b < len(grid[0]) and grid[a][b] > 0:
                if grid[a][b] == 1:
                    neighbour1 += 1
                elif grid[a][b] == 2:
                    neighbour2 += 1
        if value == 1:
            return 120 - 30*(neighbour1+neighbour2) - 30*neighbour1 + 20*neighbour2
        if value == 2:
            return 60 + 20*(neighbour1+neighbour2) - 30*neighbour1 + 20*neighbour2






