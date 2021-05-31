from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # courses = sorted(courses, key=lambda a: a[1]-a[0])
        ans = [[0 for _ in range(len(courses))] for _ in range(len(courses)+1)]
        for k in range(1, len(courses)+1):
            for x in range(k-1, len(courses)):
                continue
        return ans[-1][0]


c1 = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
c2 = [[7, 16], [2, 3], [3, 12], [3, 14], [10, 19], [10, 16], [6, 8], [6, 11], [3, 13], [6, 16]]
c3 = [[7, 17], [3, 12], [10, 20], [9, 10], [5, 20], [10, 19], [4, 18]]
sol = Solution()
sol.scheduleCourse(c3)
