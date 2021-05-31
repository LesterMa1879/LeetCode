import collections
from typing import List
# excellent job

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        d2 = collections.defaultdict(int)
        d1 = collections.defaultdict(set)
        for x in nums:
            if x in d2:
                d2[x] += 1
            else:
                d2[x] = 1
        for k, v in d2.items():
            d1[v].add(k)
        for x in range(len(nums) - 1, -1, -1):
            if len(d1.keys()) == 2:
                k1 = list(sorted(d1.keys()))
                if (k1[1] - k1[0] == 1 and len(d1[k1[1]]) == 1) or (k1[0] == 1 and len(d1[k1[0]]) == 1):
                    return x + 1
            elif len(d1.keys()) == 1 and (list(d1.keys())[0] == 1 or len(d1[list(d1.keys())[0]]) == 1):
                return x + 1
            k = d2[nums[x]]
            d2[nums[x]] -= 1
            if len(d1[k]) == 1:
                del d1[k]
            else:
                d1[k].remove(nums[x])
            if k != 1:
                d1[k - 1].add(nums[x])
        return 1


n1 = [10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6]
n2 = [2, 2, 1, 1, 5, 3, 3, 5]
n3 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5]
n4 = [1, 1, 1, 2, 2, 2]
n5 = [1, 1]
sol = Solution()
print(sol.maxEqualFreq(n3))
