import collections
from typing import List
# anyway, good job

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        di, ds, ans = collections.defaultdict(int), collections.defaultdict(set), []
        for x in range(len(words)):
            di[words[x]] = x
        for x in words:
            ds[len(x)].add(x)
        kl, ks = list(ds.keys()), set(ds.keys())
        kl.reverse()
        for k in kl:
            for x in ds[k]:
                for y in range(0, len(x)):
                    if y in ks:
                        if x[y:] == x[y:][::-1] and x[:y][::-1] in ds[y]:
                            ans.append([di[x], di[x[:y][::-1]]])
                        if x[:len(x) - y] == x[:len(x) - y][::-1] and x[len(x) - y:][::-1] in ds[y]:
                            ans.append([di[x[len(x) - y:][::-1]], di[x]])
                if x[::-1] in ds[k] and x != x[::-1]:
                    ans.append([di[x], di[x[::-1]]])
        return ans


w1 = ["abcd", "dcba", "lls", "s", "sssll"]
w2 = ["bat", "tab", "cat"]
w3 = ["a", ""]
w4 = ["a", "abc", "aba", ""]
w4 = ["bb", "bababab", "baab", "abaabaa", "aaba", "", "bbaa", "aba", "baa", "b"]
test = ["bababab", ""]
sol = Solution()
sol.palindromePairs(w1)
