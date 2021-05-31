import collections
from typing import List

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        cur = collections.deque()
        ans = float("inf")
        pre = 0
        for x in range(len(nums)):
            if nums[x] == 1:
                cur.append(x)
            if len(cur) > k + 1:
                cur.popleft()
            if len(cur) >= k and nums[x] == 1:
                pre = self.calculate(cur, k, pre)
                ans = min(ans, pre)
            if ans <= 0:
                return 0
        return ans

    def calculate(self, cur, k, ans):
        if len(cur) == k:
            for x in range(k // 2):
                ans += (cur[k - 1 - x] - cur[x]) - (k - 1 - 2 * x)
        else:
            d = k // 2
            ans = (cur[k] - cur[k - d]) - (cur[d] - cur[0]) + ans
        return ans


n1 = [1, 0, 0, 0, 0, 0, 1, 1, 0, 1]
k1 = 3

n2 = [1, 0, 0, 1, 0, 1]
k2 = 2

n3 = [1, 1, 0, 0, 1, 1, 1, 1, 0, 1,
      1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
      0, 0, 0, 1, 0, 1, 1, 1, 1, 1,
      1, 1, 0, 0, 0, 1, 0, 1, 1, 1,
      0, 1, 0, 1, 1, 1, 0]
k3 = 13

sol = Solution()
print(sol.minMoves(n2, k2))
