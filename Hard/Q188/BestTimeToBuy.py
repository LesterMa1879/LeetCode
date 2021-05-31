from typing import List


# IMPORTANT QUESTION, the first one i have no idea how to do it in the first try
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buys = [0]
        sells = [0]
        x = 0
        while x < len(prices) - 1:
            for y in range(1, len(prices)-x+1):
                if y == len(prices)-x or prices[x+y-1] > prices[x+y]:
                    if y != 1:
                        buys.append(x)
                        sells.append(x + y - 1)
                    x += y
                    break

        print(buys)
        print(sells)

        ans = [[0 for _ in range(len(buys)+1)] for _ in range(k+1)]

        return 0


prices = [1, 2, 3, 4, 5, 5, 4, 3, 6, 7, 8, 3, 7, 37, 5, 2, 3, 4, 5, 6, 9]
sol = Solution()
sol.maxProfit(3, prices)
