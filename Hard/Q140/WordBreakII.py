from typing import List


class Solution:
    def wordBreak(self, s: str, w: List[str]) -> List[str]:
        d = set()
        w = set(w)
        for word in w:
            for x in range(1, len(word) + 1):
                d.add(word[:x])
        ans = []
        for x in range(len(s)):
            ans2 = []
            for a in ans:
                if s[a[-1] + 1:x + 1] in w:
                    ans2.append(a + [x])
                if s[a[-1] + 1:x + 1] in d and x != len(s) - 1:
                    ans2.append(a)
            if s[:x + 1] in w:
                ans2.append([x])
            ans = ans2
            print(len(ans))
        result = []
        for x in ans:
            match = ""
            x = set(x)
            for y in range(len(s)):
                if y in x and y != len(s) - 1:
                    match += s[y] + " "
                else:
                    match += s[y]
            result.append(match)
        return result


s1 = "catsanddog"
wordDict1 = ["cat", "cats", "and", "sand", "dog"]

s2 = "pineapplepenapple"
wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]

s3 = "bb"
wordDict3 = ["a", "b", "bbb", "bbbb"]

s4 = "abcd"
wordDict4 = ["a", "abc", "b", "cd"]

s5 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict5 = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

sol = Solution()
sol.wordBreak(s5, wordDict5)
