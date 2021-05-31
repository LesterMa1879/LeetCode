from typing import List
import itertools


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        sets = set(nums)
        cap = len(nums) // k



nums = [6, 3, 8, 1, 3, 1, 2, 2]
print(set(nums))

k = 4
sol = Solution()
