# kinda good job
# try to improve dp complexity with cumulative sum

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        ans = [[0 for _ in range(k+1)] for _ in range(n+1)]
        for t in range(1, n+1):
            ans[t][0] = 1
        for x in range(1, n+1):
            for y in range(1, k+1):
                if (x-1)*x//2 < y:
                    continue
                b = max(0, y-(x-1))
                ans[x][y] = sum(ans[x-1][b:y+1]) % 1000000007
        return ans[-1][-1]


sol = Solution()
print(sol.kInversePairs(999, 628))