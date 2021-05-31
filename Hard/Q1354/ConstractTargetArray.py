from typing import List
# quit nice job
# review special cases

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            if target[0] == 1:
                return True
            else:
                return False
        target.sort()
        while 1:
            if target[-1] == 1:
                return True
            cur = target[-1]
            target.pop()
            s = sum(target)
            if s > 0 and cur // s > 1:
                cur = cur % s + s
            else:
                cur -= s
            if cur < 1:
                return False
            pos = self.bs(target, cur, 0, len(target)-1)
            target.insert(pos, cur)

    def bs(self, t, v, x, y):
        if x == y:
            if t[x] > v:
                return x
            else:
                return x + 1
        if x > y:
            return x
        m = (x + y) // 2
        if t[m] < v:
            return self.bs(t, v, m + 1, y)
        elif t[m] > v:
            return self.bs(t, v, x, m - 1)
        else:
            return m


t1 = [9, 3, 5]
t2 = [1, 1, 1, 2]
t3 = [8, 5]
t4 = [5, 2]
t5 = [1,1000000000]
t6 = [2]
sol = Solution()
print(sol.isPossible(t2))
