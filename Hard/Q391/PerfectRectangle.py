from typing import List

import numpy as np
# IMPORTANT QUESTION

class Solution:
    def isRectangleCover_tle(self, rectangles: List[List[int]]) -> bool:
        t = [0, 0]
        b = [float("inf"), float("inf")]
        m = [float("inf"), float("inf"), 0, 0]
        for r in rectangles:
            if b[0] >= r[0] and b[1] >= r[1]:
                b = r[0:2]
            if t[0] <= r[2] and t[1] <= r[3]:
                t = r[2:4]
            m = [min(m[0], r[0]), min(m[1], r[1]), max(m[2], r[2]), max(m[3], r[3])]
        if m[0:2] != b or m[2:4] != t:
            return False
        ans = np.zeros((t[1] - b[1], t[0] - b[0]), dtype=np.int8)
        for r in rectangles:
            ans[r[1] - b[1]:r[3] - b[1], r[0] - b[0]:r[2] - b[0]] += np.ones((r[3] - r[1], r[2] - r[0]), dtype=np.int8)
        return np.array_equal(ans, np.ones((t[1] - b[1], t[0] - b[0]), dtype=np.int8))


rectangles1 = [
    [1, 1, 3, 3],
    [3, 1, 4, 2],
    [3, 2, 4, 4],
    [1, 3, 2, 4],
    [2, 3, 3, 4]
]

rectangles2 = [
    [1, 1, 2, 3],
    [1, 3, 2, 4],
    [3, 1, 4, 2],
    [3, 2, 4, 4]
]

rectangles3 = [
    [1, 1, 3, 3],
    [3, 1, 4, 2],
    [1, 3, 2, 4],
    [2, 2, 4, 4]
]

rectangles4 = [
    [1, 1, 2, 2],
     [0, 1, 1, 2],
     [1, 0, 2, 1],
     [0, 2, 3, 3],
     [2, 0, 3, 3]
]

sol = Solution()
print(sol.isRectangleCover_tle(rectangles3))
