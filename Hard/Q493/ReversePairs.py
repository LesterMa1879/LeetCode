import bisect
from typing import List

# important question review!!!
# how to use sort reducing comparing time (n*log(n))


class Solution:
    def reversePairs_simple(self, nums):
        return sum([nums[j] > 2 * nums[i] for i in range(len(nums)) for j in range(0, i)])

    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans = 0
        sorted_nums = [nums[0]]
        for i in range(1, len(nums)):
            index = bisect.bisect_right(sorted_nums, 2 * nums[i])
            ans += len(sorted_nums) - index

            bisect.insort(sorted_nums, nums[i])

        return ans


sol = Solution()
nums = [2, 4, 3, 3, 5, 1, 3]
sol.reversePairs(nums)
