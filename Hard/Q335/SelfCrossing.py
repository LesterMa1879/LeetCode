from typing import List

# pure math problem
# make six element a pack

class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        shrink = -1
        check1 = -1
        for index in range(2, len(x)):
            if shrink == -1:
                if x[index] > x[index - 2]:
                    continue
                else:
                    shrink = index
                    if index < 3 or (index == 3 and x[index] != x[index - 2]) or (index >= 4 and x[index] < x[index - 2] - x[index - 4]):
                        continue
                    else:
                        check1 = 1
            else:
                if index == shrink + 1:
                    if check1 == 1:
                        if x[index] < x[index - 2] - x[index - 4]:
                            continue
                        else:
                            return True
                    else:
                        if x[index] < x[index - 2]:
                            continue
                        else:
                            return True
                else:
                    if x[index] < x[index - 2]:
                        continue
                    else:
                        return True
        return False


x = [1,1,1,1]
sol = Solution()
print(sol.isSelfCrossing(x))
