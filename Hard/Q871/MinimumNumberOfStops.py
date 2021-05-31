from typing import List
# take sometime to finish the question
# anyway nice job

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if target <= startFuel:
            return 0
        f = lambda a, b, c: a + b - c if a >= c and a != -1 else -1
        g = lambda a, b, c, d: (a, b) if b >= d else (c, d)
        ans = [[-1 for _ in range(len(stations))] for _ in range(len(stations))]
        for k in range(len(stations)):
            cur = k - 1
            for n in range(k, len(stations)):
                if k == 0:
                    ans[k][n] = f(startFuel, stations[n][1], stations[n][0])
                elif k == n:
                    ans[k][n] = f(ans[k - 1][n - 1], stations[n][1], stations[n][0] - stations[n - 1][0])
                else:
                    cur, ans[k][n] = g(cur, f(ans[k - 1][cur], stations[n][1], stations[n][0] - stations[cur][0]),
                                       n - 1, f(ans[k - 1][n - 1], stations[n][1], stations[n][0] - stations[n - 1][0]))
                if target - stations[n][0] <= ans[k][n]:
                    return k+1
        return -1


t1 = 100
sf1 = 10
st1 = [[10, 60], [20, 30], [30, 30], [60, 40]]

t2 = 100
sf2 = 1
st2 = [[10,100]]
sol = Solution()
print(sol.minRefuelStops(t2, sf2, st2))
