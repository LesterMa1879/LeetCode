# good job

class Solution:
    def lastSubstring(self, s: str) -> str:
        start, repeat = "", []
        for x in range(len(s)):
            if s[x] > start:
                start = s[x]
                repeat = [x]
            else:
                if len(repeat) > 1:
                    distance = (x-repeat[0]) % (repeat[1]-repeat[0])
                    if s[repeat[0]+distance] > s[x]:
                        repeat = [repeat[0]]
                    elif s[repeat[0]+distance] < s[x]:
                        repeat = [x-distance]
                elif s[x] == s[repeat[0]]:
                    repeat.append(x)
        return s[repeat[0]:]


s1 = "leetcode"
s2 = "aaaaabaaaaaaa"
s3 = "t"
s4 = "cacacb"
s5 = "cddcddcddcdda"
sol = Solution()
print(sol.lastSubstring(s5))



