import collections
import math


class Solution:
    def __init__(self):
        self.d = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
                  46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465,
                  14930352]

    def findIntegers(self, num: int) -> int:
        n = bin(num)[2:]
        if n == "0":
            return 1
        if n == "1":
            return 2
        ans = self.d[len(n)-2]
        for x in range(1, len(n)):
            if x > 1 and n[x-1] == n[x-2] == "1":
                break
            if x != len(n)-1:
                if n[x] == "1":
                    ans += self.d[len(n)-2-x]
            else:
                if n[-2] == "0" and n[-1] == "1":
                    ans += 2
                else:
                    ans += 1
        if ans == self.d[len(n)-2]:
            return ans + 1
        return ans


n1 = 10
sol = Solution()
# print(sol.findIntegers(n1))
for x in range(1, 100):
    print(sol.findIntegers(x))
    print("------------")


