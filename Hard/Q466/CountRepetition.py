class Solution:
    # trying to iterate the string to get repeat pattern instead of just assuming start-end problem no exist
    # Important Question Review!!!

    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if len(s1) * n1 < 1000000:
            return self.getMaxRepetitions_sp(s1, n1, s2, n2)
        else:
            start, end = self.getSingleRepetition(s1, s2, n2)
            num = end // len(s1)
            left = end % len(s1)
            print(start)
            print(end)
            print(num)
            print(left)
            print("=======")
            if left < start:
                return n1 // num
            else:
                return n1 // (num+1)
        return -1

    def getSingleRepetition(self, s1, s2, n2):
        merge1 = s1 * len(s2) * n2
        merge2 = s2 * n2
        index = 0
        start = 0
        for x in range(len(merge1)):
            if merge1[x] == merge2[index]:
                if index == 0:
                    start = x
                if index == len(merge2) - 1:
                    return start + 1, x + 1
                index += 1
        return -1

    def getMaxRepetitions_sp(self, s1, n1, s2, n2):
        merge1 = s1 * n1
        merge2 = s2 * n2
        index = 0
        ans = 0
        for x in range(len(merge1)):
            if merge1[x] == merge2[index]:
                if index == len(merge2) - 1:
                    ans += 1
                    index = 0
                    continue
                index += 1
        return ans


s11 = "aabaabaab"
n11 = 4
s21 = "aba"
n21 = 2

s12 = "phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenzkycxf"
n12 = 1000000
s22 = "xtlsgypsfadpooefxzbcoejuvpvaboygpoeylfpbnpljvrvipyamyehwqnqrqpmxujjloovaowuxwhmsncbxcoksfzkvatxdknly"
n22 = 100

s13 = "aaa"
n13 = 3
s23 = "aa"
n23 = 1

s14 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
n14 = 1000000
s24 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
n24 = 103

sol = Solution()
# print(len(s12))
# print(len(s22))
print(sol.getMaxRepetitions(s14, n14, s24, n24))
