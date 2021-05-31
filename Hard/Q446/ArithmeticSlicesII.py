import math
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = [set() for _ in range(len(A))]
        for x in range(2, len(ans)):
            p = set()
            f = lambda a, b: (a+b)//2 if (b-a) % 2 == 0 else math.pi
            for y in range(x):
                p.add(f(A[y], A[x]))
                if A[y] in p:
                    ans[x].add()




