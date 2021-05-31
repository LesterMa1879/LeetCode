import math
from typing import List

# excellent job, AC one time

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]):
        angles = []
        original = 0
        for x in points:
            if x[0] == location[0] and x[1] == location[1]:
                original += 1
                continue
            angles.append(self.angleOfLine(location[0], location[1], x[0], x[1]))
        angles.sort()
        angles = angles + list(map(lambda _: _ + 360, angles))
        ans = 0
        visited = 0
        for x in range(len(points)):
            for y in range(visited, len(angles)):
                if angles[y] <= angles[x] + angle:
                    continue
                else:
                    visited = y
                    break
            if ans < visited - x:
                ans = visited - x
        return ans + original

    def angleOfLine(self, x1, y1, x2, y2):
        angle = math.degrees(math.atan2(x2 - x1, y2 - y1))
        if angle >= 0:
            return angle
        else:
            return 360 + angle


p0 = [[2, 1], [2, 2], [3, 4], [1, 1]]
a0 = 90
l0 = [1, 1]

p1 = [[2, 1], [2, 2], [3, 3]]
a1 = 90
l1 = [1, 1]
sol = Solution()
print(sol.visiblePoints(p0, a0, l0))
# print(sol.angle_of_line(0, 0, -1, -1))
