from random import random, randint, choice
from typing import List


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.b = set(blacklist)
        self.N = N
        if not len(self.b) <= self.N // 3:
            self.c = [x for x in range(N) if x not in self.b]

    def pick(self) -> int:
        if len(self.b) <= self.N // 3:
            ans = randint(0, self.N - 1)
            while ans in self.b:
                ans = randint(0, self.N - 1)
        else:
            ans = choice(self.c)
        return ans


sol = Solution(3, [0])
x = 0
while x < 20:
    print(sol.pick())
    x += 1
