class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ans = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        f = lambda a, b: ans[a][b] if -1 < a < len(s1)+1 and -1 < b < len(s2)+1 else False
        g = lambda a: s3[a] if -1 < a < len(s3) else "~"
        if len(s1) + len(s2) != len(s3):
            return False
        for x in range(len(s1)+1):
            for y in range(len(s2)+1):
                if x == 0 and y == 0:
                    ans[x][y] = True
                    continue
                ans[x][y] = (f(x-1, y) and s1[x-1] == g(x+y-1)) or (f(x, y-1) and s2[y-1] == g(x+y-1))
        return ans[-1][-1]


s11 = "aabcc"
s21 = "dbbcaa"
s31 = "aadbbacbcac"

s12 = ""
s22 = ""
s32 = ""
sol = Solution()
print(sol.isInterleave(s12, s22, s32))
