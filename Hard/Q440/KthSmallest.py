from random import random

# IMPORTANT QUESTION
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        elevens = []
        lmax = len(str(n))
        for num in range(1, n+1):
            elevens.append(self.convert(num, lmax))
        elevens.sort()
        elven = elevens[k-1]
        ans = ""
        for x in elven:
            if x == "A":
                ans += "9"
            elif 9 >= int(x) >= 1:
                ans += str(int(x)-1)
            elif x == "0":
                break
        return int(ans)

    def convert(self, num, lmax):
        ten = str(num)
        eleven = ""
        lcur = len(ten)
        for x in range(lmax):
            if x < lcur:
                eleven += self.switch(ten[x])
            else:
                eleven += "0"
        return eleven

    def switch(self, char):
        if int(char) < 9:
            return str(int(char)+1)
        else:
            return "A"







sol = Solution()
#rint(sol.findKthNumber(13, 13))

