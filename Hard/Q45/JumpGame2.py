from typing import List
# beautiful job
# while a little bit improvement in speed could be better

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = [0 for _ in range(len(nums))]
        p = {(0, 0 + nums[0])}
        for x in range(1, len(ans)):
            p = set(filter(lambda v: v[1] >= x, p))
            ans[x] = min(ans[x[0]] for x in p) + 1
            if len(set(filter(lambda v: v[1] >= x + nums[x], p))) == 0:
                p.add((x, x + nums[x]))
        return ans[-1]


n1 = [2, 3, 0, 1, 4, 3, 2, 4, 3, 2, 1, 2, 7, 4, 4, 3]
sol = Solution()
print(sol.jump(n1))
