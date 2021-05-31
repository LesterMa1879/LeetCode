# tricky problem

class Solution:
    def minCut_tle(self, s: str) -> int:
        length = len(s)
        ans = float("inf")
        for x in range(1, length + 1):
            if s[:x] == s[:x][::-1]:
                if x == length:
                    return 0
                ans = min(ans, 1 + self.minCut_tle(s[x:]))
        return ans

    def minCut_tle_count(self, s: str) -> int:
        length = len(s)
        ans = 0
        for x in range(1, length + 1):
            if s[:x] == s[:x][::-1]:
                if x == length:
                    return ans + 1
                ans += 1 + self.minCut_tle_count(s[x:])
        return ans

    def minCut(self, s):
        length = len(s)
        ans = [0 for _ in range(length+1)]
        for x in range(1, length+1):
            tmp = float("inf")
            for y in range(x):
                if s[y:x] == s[y:x][::-1]:
                    tmp = min(tmp, ans[y]+1)
            ans[x] = tmp
        return ans[-1]-1


s = "aaaaaaaaaa"
sol = Solution()
print(sol.minCut(s))
