from collections import deque
from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        s = [[], [], []]
        for d in digits:
            s[d % 3].append(d)
        s = [sorted(x, reverse=True) for x in s]
        if len(digits) == 0:
            return ""
        if sum(digits) % 3 == 1:
            if len(s[1]) > 0:
                s[1] = s[1][:-1]
            else:
                s[2] = s[2][:-2]
        elif sum(digits) % 3 == 2:
            if len(s[2]) > 0:
                s[2] = s[2][:-1]
            else:
                s[1] = s[1][:-2]
        ans = ""
        for d in sorted(s[0] + s[1] + s[2], reverse=True):
            ans += str(d)
        if len(ans) > 0 and ans[0] == "0":
            return "0"
        return ans


d1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 3, 4]
d2 = []
d3 = [0, 0, 0, 0]
d4 = [8, 6, 7, 1, 0]
d5 = [1]
sol = Solution()
print(sol.largestMultipleOfThree(d5))
