from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = [0 for _ in range(len(nums)+1)]
        for num in nums:
            if 0 < num < len(nums)+1:
                ans[num-1] = 1
        for x in range(0, len(nums)+1):
            if ans[x] == 0:
                return x+1
        return -1
n1 = [7,8,9,11,12]
sol = Solution()
print(sol.firstMissingPositive(n1))
