from collections import deque
from typing import List


# important question review!
# self solution use dp without shifting the question to reduce time complexity
# list the properties first and imply then

class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)
        ans = N + 1
        print(P)
        monoq = deque()
        for y, Py in enumerate(P):
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N + 1 else -1

    def shortestSubarray_other(self, A: List[int], K: int) -> int:
        length = len(A)
        result = [[0 for _ in range(length + 1)] for _ in range(length + 1)]
        for i in range(length):
            result[0][i + 1] = A[i]
            result[i + 1][0] = A[i]
        output = []
        for y in range(1, length + 1):
            for x in range(y, length + 1):
                if x == y:
                    result[x][y] = A[y-1]
                else:
                    result[x][y] = result[x][0] + result[x - 1][y]
                if result[x][y] >= K:
                    output.append(x-y+1)
                    break
        # print(result)
        if len(output) == 0:
            return -1
        else:
            return min(output)
                    




A =[4934,72728,28459,17172,13090,93563,50447,-9866,-32292,30383,
    95736,-22858,20416,65242,-22343,-1736,56869,-24816,80113,-48157,
    49145,-7403,71979,24726,-21065,61149,54446,13294,25720,69296,
    84135,58611,34369,-14809,-33419,-36757,-34981,11341,-34333,79748,
    21005,-41146,21232,88408,63856,58004,-39644,23613,31001,94396]
K = 202456

sol = Solution()
print(sol.shortestSubarray(A, K))
