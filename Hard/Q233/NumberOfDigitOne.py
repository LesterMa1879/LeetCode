# kinda great job
# remember the complexity of library function

class Solution:
    def countDigitOne(self, n: int) -> int:
        n = str(n)
        visit = int(n[-1])
        if visit == 0:
            ans = 0
        else:
            ans = 1
        n = n[::-1]
        for x in range(1, len(n)):
            base = x * pow(10, x - 1)
            num = int(n[x])
            if num == 0:
                ans = ans
            elif num == 1:
                ans = base * num + (visit + 1) + ans
            else:
                ans = base * num + pow(10, x) + ans
            visit = num * pow(10, x) + visit
        return int(ans)


sol = Solution()
print(sol.countDigitOne(100))
