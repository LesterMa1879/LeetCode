import collections
from typing import List


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        d = collections.defaultdict(set)
        for x in blocked:
            d[x[1]].add(x[0])
        k = sorted(list(d.keys()))
