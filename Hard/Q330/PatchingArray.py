from typing import List
import itertools


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        sums, empty = {0}, set()
        for x in range(1, len(nums) + 1):
            for y in itertools.combinations(nums, x):
                sums.add(sum(y))
        empty = set(range(1, n+1)) - sums
        ans = 0
        while len(empty) > 0:
            element, increase = 0, 0
            for x in range(1, 21):
                count = 0
                for y in sums:
                    if y + x in empty:
                        count += 1
                    if y + x > n:
                        break
                if count > increase:
                    element, increase = x, count
            change = set()
            for y in sums:
                if y + element in empty:
                    change.add(y + element)
                    empty.remove(y + element)
            sums = set.union(sums, change)
            ans += 1
        return ans


nums1 = [1, 5, 10]
n1 = 20

nums2 = [1, 3]
n2 = 6

nums3 = [1, 2, 2]
n3 = 5
sol = Solution()
print(sol.minPatches(nums2, n2))
