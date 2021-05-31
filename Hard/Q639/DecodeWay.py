import math

# always try to solve question with dp or other computer science method instead of math


class Solution:
    def numDecodings(self, s):
        mod = 1000000007
        ans = [0 for _ in range(len(s))]
        for x in range(len(s)):
            if x == 0:
                if s[x] == "0":
                    return 0
                elif s[x] == "*":
                    ans[x] = 9
                else:
                    ans[x] = 1
                continue

            solo = ans[x - 1]
            if x == 1:
                doub = 1
            else:
                doub = ans[x - 2]

            if s[x] == "0":
                if s[x-1] == "*":
                    ans[x] = doub * 2
                elif s[x-1] == "1" or s[x-1] == "2":
                    ans[x] = doub
                else:
                    return 0
            elif s[x-1] == "*":
                if s[x] == "*":
                    ans[x] = doub * 15 + solo * 9
                elif int(s[x]) <= 6:
                    ans[x] = doub * 2 + solo
                else:
                    ans[x] = doub + solo
            elif int(s[x-1]) == 1:
                if s[x] == "*":
                    ans[x] = doub * 9 + solo * 9
                else:
                    ans[x] = doub + solo
            elif int(s[x-1]) == 2:
                if s[x] == "*":
                    ans[x] = doub * 6 + solo * 9
                elif int(s[x]) <= 6:
                    ans[x] = doub + solo
                else:
                    ans[x] = solo
            else:
                if s[x] == "*":
                    ans[x] = solo * 9
                else:
                    ans[x] = solo
            ans[x] = ans[x] % mod
        # print (ans)
        return ans[-1]



s1 = "12034*43217102*01221*20128891*811258112342412*241234123*1342134213041*123122121211*1234123412"
s2 = "12*1*2"
s3 = "*1"
s4 = "1*"
s5 = "3*"
s5 = "**"
s6 = "0"
sol = Solution()
print(sol.numDecodings(s6))
