
# review for dp and how to imply it
# build a matrix of result
class Solution(object):
    def isMatch(self, s, p):
        p = self.clean(p)
        return self.match_dp(s, p)

    def clean(self, p):
        result = ""
        status = 0
        for i in p:
            if i != "*" and status == 0:
                result += i
            elif i != "*" and status == 1:
                result += "*" + i
                status = 0
            else:
                status = 1
        if status == 1:
            result += "*"

        return result

    def match_dp(self, s, p):
        if (len(p) is 0 and len(s) is 0) or p == "*":
            return True
        elif len(p) is 0 or len(s) is 0:
            return False
        b = [[False for i in range(len(s))] for j in range(len(p))]
        for i in range(len(p)):
            if i is 0:
                if p[i] is "*":
                    for j in range(len(s)):
                        b[i][j] = True
                elif p[i] is "?":
                    b[i][i] = True
                elif p[i] is s[i]:
                    b[i][i] = True
                else:
                    return False
            else:
                if i is 1 and p[i - 1] is "*":
                    if p[i] is "?":
                        b[i][i - 1] = True
                    elif p[i] is s[i-1]:
                        b[i][i - 1] = True
                if p[i] is "*":
                    work = False
                    for j in range(len(s)):
                        if work is False and b[i - 1][j] is True:
                            work = True
                            b[i][j] = True
                        elif work is True:
                            b[i][j] = True
                elif p[i] is "?":
                    for j in range(1, len(s)):
                        if b[i - 1][j - 1] is True:
                            b[i][j] = True
                else:
                    for j in range(1, len(s)):
                        if b[i - 1][j - 1] is True and p[i] is s[j]:
                            b[i][j] = True
        return b[len(p) - 1][len(s) - 1]

    def match_rec(self, s, p):
        if len(p) == 0 and len(s) == 0:
            return True
        elif p == "*":
            return True
        elif len(p) == 0 or len(s) == 0:
            return False

        elif p[0] == "?":
            return self.match_rec(s[1:], p[1:])

        elif p[0] == "*":
            for index in range(len(s) + 1):
                if self.match_rec(s[index:], p[1:]):
                    return True
            return False
        elif s[0] == p[0]:
            return self.match_rec(s[1:], p[1:])

        else:
            return False


sol = Solution()
s = "b"
p = "*b*"

"abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb"
"**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"

"b"
"*a*"

print(sol.isMatch(s, p))

# T = [[False for i in range(5)] for j in range(4)]
# T[0][1] = True

# print(T)
