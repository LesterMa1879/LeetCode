from typing import List
# amazing job

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s, c, ans = str(n), len(digits), 0
        s0, e0 = 0, 1
        for x in range(len(s)):
            s1, e1 = 0, 0
            for d in digits:
                if int(d) < int(s[x]):
                    s1 += 1
                elif int(d) == int(s[x]):
                    e1 += 1
            s0 = s0 * c + e0 * s1
            e0 = e0 * e1
        for x in range(1, len(s)):
            ans += pow(c, x)
        return ans + s0 + e0


d1 = ["1", "3", "5", "7"]
n1 = 100

d2 = ["1","4","9"]
n2 = 1000000000
sol = Solution()
print(sol.atMostNGivenDigitSet(d2, n2))
