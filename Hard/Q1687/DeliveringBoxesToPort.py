import collections
from typing import List


# Important Question, Review!!!

class Solution:

    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        que = collections.deque([(-1, 0)])
        pre = -1
        ws = 0
        for i, (p, w) in enumerate(boxes):
            ws += w
            while i - pre > maxBoxes or ws > maxWeight:
                pre += 1
                ws -= boxes[pre][1]
            while que[0][0] < pre: que.popleft()
            mn = (2 if i + 1 < n and p == boxes[i + 1][0] else 1) + que[0][1]
            while que[-1][1] >= mn: que.pop()
            que.append((i, mn))

        base_trip = 1
        for i in range(n - 1):
            if boxes[i][0] != boxes[i + 1][0]: base_trip += 1

        return base_trip + que[-1][1]

    def boxDelivering_self(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        ans = [0 for _ in range(len(boxes) + 1)]
        ans[0] = 0
        ans[1] = 2
        visit = 0
        for index in range(2, len(boxes) + 1):
            ans[index] = float('inf')
            weight = 0
            box = 0
            for x in range(visit, index + 1):
                weight += boxes[x - 1][1]
                box += 1
                if box <= maxBoxes and weight <= maxWeight:
                    print(index)
                    print(x)
                    print(self.countOneLegalDelivery(boxes[x: index]))
                    print(visit)
                    print("=======")
                    temp = ans[x] + self.countOneLegalDelivery(boxes[x: index])
                    if ans[index] > temp:
                        visit = x
                        ans[index] = temp
        print(ans)
        return ans[-1]

    def countOneLegalDelivery(self, boxes):
        trips = 0
        port = -1
        for box in boxes:
            if box[0] == port:
                continue
            else:
                trips += 1
                port = box[0]
        return trips + 1


b1 = [[2, 4], [2, 5], [3, 1], [3, 2], [3, 7], [3, 1], [4, 4], [1, 3], [5, 2]]
p1 = 5
m1 = 5
w1 = 7

b2 = [[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]]
p2 = 3
m2 = 6
w2 = 7

b3 = [[1, 1], [2, 1], [1, 1]]
p3 = 2
m3 = 3
w3 = 3

sol = Solution()
print(sol.boxDelivering(b1, p1, m1, w1))
# print(sol.countOneLegalDelivery([[1, 4], [1, 2]]))
