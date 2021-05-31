class Solution:
    # o(n^2)
    def shortestPalindrome_bf(self, s: str) -> str:
        length = len(s)
        for x in range(length, 0, -1):
            if s[:x] == s[:x][::-1]:
                return s[x:][::-1] + s
        return ""

    

s = "abcd"
sol = Solution()
print(sol.shortestPalindrome(s))

